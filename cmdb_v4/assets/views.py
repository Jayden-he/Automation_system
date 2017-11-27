# -*- coding: UTF-8 -*-
import ast
from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required
from django.template import RequestContext
from forms import HostForm, IdcForm, ProjectForm, ServiceForm
from django.shortcuts import get_object_or_404
from assets.models import Host, IDC, Service, Project, HostRecord
from assets.models import SERVER_STATUS, Server_Type
from new_api import pages
import sys,json,shlex,subprocess,os,re,ast
reload(sys)
sys.setdefaultencoding('utf-8')

def server_info(uuid):
    host = Host.objects.get(uuid=uuid)
    ip = host.eth1
    port = host.remote_port

    file = open("/etc/ansible/hosts", 'a+')
    a = file.read()
    if re.search("%s:%s" % (ip, port), a):
        pass
    else:
        file.write("%s:%s \n" % (ip, port))
    file.close()
    cmd = "/usr/bin/ansible %s -m setup" % ip
    raw_info = subprocess.check_output(shlex.split(cmd))
    base_info = json.loads(raw_info.split('=>')[1])['ansible_facts']
    hostname = base_info['ansible_hostname']
    ip = base_info['ansible_default_ipv4']["address"]
    mac = base_info["ansible_default_ipv4"]['macaddress']
    cpu = base_info['ansible_processor_vcpus']
    memory = round(int(base_info['ansible_memtotal_mb'])/1024.0,1)
    disk_info = base_info['ansible_devices']
    disk_volume = sum([int(disk_info[disk]['sectors'])*int(disk_info[disk]['sectorsize']) for disk in disk_info])/1024**3
    ansible_distribution = base_info["ansible_distribution"] + base_info["ansible_distribution_major_version"]
    os_machine = base_info["ansible_machine"]
    system_kernel = base_info["ansible_kernel"]
    cpu_info = base_info["ansible_processor"]
    mount_info = base_info["ansible_mounts"]
    mount_all = {}
    for i in range(len(mount_info)):
        print i
        mount_all["mount_info_%s" % i] = {"device": mount_info[i]["device"], "mount": mount_info[i]["mount"],
                                          "size_total": mount_info[i]["size_total"], }

    host.node_name = hostname
    host.eth1 = ip
    host.cpu = cpu
    host.mac = mac
    host.memory = memory
    host.hard_disk = disk_volume
    host.system_cpuarch = os_machine
    host.system = ansible_distribution
    host.system_kernel = system_kernel
    host.cpu_info = cpu_info
    host.mount_all = mount_all
    host.save()


    return hostname,ip,mac,cpu,memory,disk_volume,os_machine,ansible_distribution,system_kernel,cpu_info,mount_all



def my_render(template, data, request):
    return render_to_response(template, data, context_instance=RequestContext(request))


def get_diff(obj1, obj2):
    fields = ['service', 'business']
    no_check_fields = ['cpu', 'core_num', 'hard_disk', 'memory']
    d1, d2 = obj1, dict(obj2.iterlists())
    info = {}
    for k, v in d1.items():
        if k in fields:
            if d2.get(k):
                d2_value = d2[k]
            else:
                d2_value = u''
        elif k in no_check_fields:
            continue
        else:
            d2_value = d2[k][0]
        if not v:
            if v == False:
                pass
            else:
                v = u''
        if isinstance(v, list):
            v.sort()
            if not d2_value:
                d2_value = []
            d2_value.sort()
            if v != d2_value:
                info.update({k: [v, d2_value]})
        else:
            if str(v) != str(d2_value):
                info.update({k: [v, d2_value]})

    for k, v in info.items():
        if v == [None, u'']:
            info.pop(k)
    return info

#@login_required
#@permission_required('account.access_cmdb')
def db_to_record(username, host, info):
    text_list = []
    for k, v in info.items():
        field = Host._meta.get_field_by_name(k)[0].verbose_name
        if k == 'idc':
            old = IDC.objects.filter(uuid=v[0])
            new = IDC.objects.filter(uuid=v[1])
            if old:
                name_old = old[0].name
            else:
                name_old = u'无'
            if new:
                name_new = new[0].name
            else:
                name_new = u'无'
            text = field + u'由 ' + name_old + u' 更改为 ' + name_new

        elif k == 'service':
            old, new = [], []
            for s in v[0]:
                service_name = Service.objects.get(uuid=s).name
                old.append(service_name)
            for s in v[1]:
                service_name = Service.objects.get(uuid=s).name
                new.append(service_name)
            text = field + u'由 ' + ','.join(old) + u' 更改为 ' + ','.join(new)

        elif k == 'business':
            old, new = [], []
            for s in v[0]:
                project_name = Project.objects.get(uuid=s).service_name
                old.append(project_name)
            for s in v[1]:
                project_name = Project.objects.get(uuid=s).service_name
                new.append(project_name)
            text = field + u'由 ' + ','.join(old) + u' 更改为 ' + ','.join(new)

        elif k == 'vm':
            old = Host.objects.filter(uuid=v[0])
            new = Host.objects.filter(uuid=v[1])
            if old:
                name_old = old[0].eth1
            else:
                name_old = u'无'
            if new:
                name_new = new[0].eth1
            else:
                name_new = u'无'
            text = field + u'父主机由 ' + name_old + u' 更改为 ' + name_new

        else:
            text = field + u'由 ' + str(v[0]) + u' 更改为 ' + str(v[1])
        text_list.append(text)

    if len(text_list) != 0:
        HostRecord.objects.create(host=host, user=username, content=text_list)


# 主机

@login_required
@permission_required('account.access_cmdb')
def host_list(request):
    """ 主机列表 """
    hosts = Host.objects.all().order_by("-create_time")
    idcs = IDC.objects.filter()
    Server_Type = Project.objects.all()
    services = Service.objects.all()
    host_applications = Server_Type
    server_status = SERVER_STATUS
    server_list_count = hosts.count()
    physics = Host.objects.filter(vm__isnull=True).count()
    vms = Host.objects.filter(vm__isnull=False).count()
    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(hosts, request)
    return render(request, 'assets/host_list.html', locals())


@login_required
@permission_required('account.access_cmdb')
def host_add(request):
    """ 添加主机 """
    uf = HostForm()
    projects = Project.objects.all()
    services = Service.objects.all()
    if request.method == 'POST':
        uf_post = HostForm(request.POST)
        physics = request.POST.get('physics', '')
        ip = request.POST.get('eth1', '')
        if Host.objects.filter(eth1=ip):
            emg = u'添加失败, 该IP %s 已存在!' % ip
            return my_render('assets/host_add.html', locals(), request)
        if uf_post.is_valid():
            zw = uf_post.save(commit=False)
            # zw.mac = str(request.POST.getlist("mac")[0]).replace(':', '-').strip(" ")
            status = uf_post.cleaned_data['status']
            if physics:
                physics_host = get_object_or_404(Host, eth1=physics)
                zw.vm = physics_host
                zw.type = 1
            else:
                zw.type = 0
            zw.save()
            uf_post.save_m2m()
            host = Host.objects.get(eth1=ip)
            server_info(host.uuid)
            smg = u'主机%s添加成功!' % ip

            return render_to_response('assets/host_add.html', locals(), context_instance=RequestContext(request))
    return render_to_response('assets/host_add.html', locals(), context_instance=RequestContext(request))


@login_required
@permission_required('account.access_cmdb')
def host_add_batch(request):
    """ 批量添加主机 """
    if request.method == 'POST':
        multi_hosts = request.POST.get('batch').split('\n')
        for host in multi_hosts:
            if host == '':
                break
            node_name, eth1, remote_port, idc, host_application, hard_info, comment = host.split()
            hard_info = ast.literal_eval(hard_info)
            cpu, memory, hard_disk = hard_info[0:3]
            if Host.objects.filter(eth1=eth1):
                emg = u'添加失败, 该eth1的IP %s 已存在!' % eth1
                return my_render('assets/host_add_batch.html', locals(), request)
            idc = IDC.objects.get(name=idc)
            asset = Host(node_name=node_name, eth1=eth1, remote_port=remote_port, idc=idc,
                         host_application=host_application, cpu=cpu, memory=memory, hard_disk=hard_disk, editor=comment)
            asset.save()
        smg = u'批量添加成功.'
        return my_render('assets/host_add_batch.html', locals(), request)

    return my_render('assets/host_add_batch.html', locals(), request)


@login_required
@permission_required('account.access_cmdb')
def host_detail(request):
    """ 主机详情 """
    uuid = request.GET.get('uuid', '')
    ip = request.GET.get('ip', '')
    if uuid:
        host = get_object_or_404(Host, uuid=uuid)
    elif ip:
        host = get_object_or_404(Host, eth1=ip)
    mount_info = ast.literal_eval(host.mount_all)
    #return HttpResponse(host.mount_all)
    #mount_info_json = json.loads(mount_info)
    host_record = HostRecord.objects.filter(host=host).order_by('-time')
    return render_to_response('assets/host_detail.html', locals(), context_instance=RequestContext(request))

def host_update(request):
    """主机硬件信息更新"""
    uuid = request.GET.get('uuid','')

    #hostname, ip, mac, cpu, memory, disk_volume, os_machine,ansible_distribution,system_kernel,cpu_info,mount_all = server_info(ip, port)
    server_info(uuid)
    return HttpResponseRedirect("/assets/host_list/")


@login_required
@permission_required('account.access_cmdb')
def host_edit(request):
    """ 修改主机 """
    uuid = request.GET.get('uuid')
    host = get_object_or_404(Host, uuid=uuid)
    uf = HostForm(instance=host)
    project_all = Project.objects.all()
    project_host = host.business.all()
    projects = [p for p in project_all if p not in project_host]

    service_all = Service.objects.all()
    service_host = host.service.all()
    services = [s for s in service_all if s not in service_host]
    username = request.user.username

    if request.method == 'POST':
        physics = request.POST.get('physics', '')
        uf_post = HostForm(request.POST, instance=host)
        if uf_post.is_valid():
            zw = uf_post.save(commit=False)
            request.POST = request.POST.copy()
            # return HttpResponse(username)
            if physics:
                #physics_host = get_object_or_404(Host, eth1=physics)
				
                request.POST['vm'] = physics_host.uuid
                if host.vm:
                    if str(host.vm.eth1) != str(physics):
                        zw.vm = physics_host
                else:
                    zw.vm = physics_host
                zw.type = 1
            else:
                request.POST['vm'] = ''
                zw.type = 0

            zw.save()
            uf_post.save_m2m()
            new_host = get_object_or_404(Host, uuid=uuid)
            info = get_diff(uf_post.__dict__.get('initial'), request.POST)
            db_to_record(username, host, info)
            return HttpResponseRedirect('/assets/host_detail/?uuid=%s' % uuid)

    return render(request,'assets/host_edit.html', locals())


@login_required
@permission_required('account.access_cmdb')
def host_edit_batch(request):
    """ 批量修改主机 """
    uf = HostForm()
    username = request.user.username
    projects = Project.objects.all()
    services = Service.objects.all()
    if request.method == 'POST':
        ids = str(request.GET.get('uuid', ''))
        env = request.POST.get('env', '')
        idc = request.POST.get('idc', '')
        host_application = request.POST.get('host_application', '')
        business = request.POST.getlist('business', '')
        services = request.POST.getlist('service', '')
        cabinet = request.POST.get('cabinet', '')
        editor = request.POST.get('editor', '')
        uuid_list = ids.split(",")

        for uuid in uuid_list:
            record_list = []
            host = get_object_or_404(Host, uuid=uuid)
            if env:
                if not host.env:
                    info = u'无'
                else:
                    info = host.env
                if env != host.env:
                    text = u'环境' + u'由 ' + info + u' 更改为 ' + env
                    record_list.append(text)
                    host.env = env

            if idc:
                get_idc = get_object_or_404(IDC, uuid=idc)

                if host.idc != get_idc.name:
                    if not host.idc:
                        text = u'IDC' + u'由 ' + "none" + u' 更改为 ' + get_idc.name
                    else:
                        text = u'IDC' + u'由 ' + host.idc.name + u' 更改为 ' + get_idc.name
                    record_list.append(text)
                    host.idc = get_idc

            if host_application:
                if host_application != host.host_application:
                    text = u'主机应用' + u'由 ' + host.host_application + u' 更改为 ' + host_application
                    record_list.append(text)
                    host.host_application = host_application

            if business:
                old, new, project_list = [], [], []
                for s in host.business.all():
                    project_name = s.service_name
                    old.append(project_name)
                for s in business:
                    project = Project.objects.get(uuid=s)
                    project_name = project.service_name
                    new.append(project_name)
                    project_list.append(project)
                if old != new:
                    text = u'所属业务' + u'由 ' + ','.join(old) + u' 更改为 ' + ','.join(new)
                    record_list.append(text)
                    host.business = project_list

            if services:
                old, new, service_list = [], [], []
                for s in host.service.all():
                    service_name = s.name
                    old.append(service_name)
                for s in services:
                    service = Service.objects.get(uuid=s)
                    service_name = service.name
                    new.append(service_name)
                    service_list.append(service)
                if old != new:
                    text = u'运行服务' + u'由 ' + ','.join(old) + u' 更改为 ' + ','.join(new)
                    record_list.append(text)
                    host.service = service_list

            if cabinet:
                if not host.cabinet:
                    info = u'无'
                else:
                    info = host.cabinet
                if cabinet != host.cabinet:
                    text = '机柜号' + u'由 ' + info + u' 更改为 ' + cabinet
                    record_list.append(text)
                    host.cabinet = cabinet

            if editor:
                if editor != host.editor:
                    text = '备注' + u'由 ' + host.editor + u' 更改为 ' + editor
                    record_list.append(text)
                    host.editor = editor

            if len(record_list) != 0:
                host.save()
                HostRecord.objects.create(host=host, user=username, content=record_list)

        return my_render('assets/host_edit_batch_ok.html', locals(), request)
    return my_render('assets/host_edit_batch.html', locals(), request)


@login_required
@permission_required('account.access_cmdb')
def host_del(request):
    """ 删除主机 """
    uuid = request.GET.get('uuid', '')
    host = get_object_or_404(Host, uuid=uuid)
    Host.objects.filter(uuid=uuid).delete()
    return HttpResponseRedirect('/assets/host_list/')


@login_required
@permission_required('account.access_cmdb')
def host_del_batch(request):
    """ 批量删除主机 """

    ids = str(request.GET.get('uuid', ''))

    for id in ids.split(','):
        host = get_object_or_404(Host, uuid=id)
        Host.objects.filter(uuid=id).delete()
    return HttpResponseRedirect('/assets/host_list/')


@login_required
@permission_required('account.access_cmdb')
def server_application(request):
    """该主机应用下的服务器"""
    application_name = request.GET.get("application_name")
    server_list = Host.objects.filter(host_application=application_name)
    server_list_count = server_list.count()
    return render_to_response('assets/host_project_host.html', locals(), context_instance=RequestContext(request))


# 机房
@login_required
@permission_required('account.access_cmdb')
def idc_list(request):
    """机房列表"""
    idcs = IDC.objects.all()
    # Server_Type = Project.objects.all()
    return render(request, 'assets/idc_list.html', locals(), )


@login_required
@permission_required('account.access_cmdb')
def idc_add(request):
    """ 添加IDC """
    if request.method == 'POST':
        init = request.GET.get("init", False)
        uf = IdcForm(request.POST)
        if uf.is_valid():
            idc_name = uf.cleaned_data['name']
            if IDC.objects.filter(name=idc_name):
                emg = u'添加失败, 此IDC %s 已存在!' % idc_name
                return my_render('assets/idc_add.html', locals(), request)
            uf.save()
            if not init:
                return HttpResponseRedirect("/assets/idc_list/")
            # else:
            #	return HttpResponseRedirect('/assets/server/type/add/?init=true')
    else:
        uf = IdcForm()
    return render(request, 'assets/idc_add.html', locals())


@login_required
@permission_required('account.access_cmdb')
def idc_edit(request):
    """修改机房"""
    uuid = request.GET.get('uuid', '')
    idc = get_object_or_404(IDC, uuid=uuid)
    if request.method == 'POST':
        uf = IdcForm(request.POST, instance=idc)
        if uf.is_valid():
            uf.save()
            return HttpResponseRedirect("/assets/idc_list/")
    else:
        uf = IdcForm(instance=idc)
        return my_render('assets/idc_edit.html', locals(), request)


@login_required
@permission_required('account.access_cmdb')
def idc_del(request):
    """删除idc机房"""
    uuid = request.GET.get('uuid', '')
    idc = get_object_or_404(IDC, uuid=uuid)
    idc.delete()
    return HttpResponseRedirect('/assets/idc_list/')


@login_required
@permission_required('account.access_cmdb')
def idc_type_item(request):
    """
    查看该IDC机房下的服务器
    """
    idc_name = request.GET.get("idc_name")
    IDC_name = IDC.objects.get(name=idc_name)
    server_list = IDC_name.host_set.all()
    server_list_count = server_list.count()
    return render_to_response('assets/host_project_host.html', locals(), context_instance=RequestContext(request))


# 项目
@login_required
@permission_required('account.access_cmdb')
def server_type_list(request):
    """项目列表"""
    business_list = Project.objects.all()
    return render_to_response('assets/server_type_list.html', locals(), context_instance=RequestContext(request))


@login_required
@permission_required('account.access_cmdb')
def server_type_add(request):
    """添加项目"""
    if request.method == 'POST':  # 验证post方法
        init = request.GET.get("init", False)
        uf = ProjectForm(request.POST)
        if uf.is_valid():
            project_name = uf.cleaned_data['service_name']
            if Project.objects.filter(service_name=project_name):
                emg = u'添加失败, 此项目 %s 已存在!' % project_name
                return my_render('assets/server_type_add.html', locals(), request)
            uf.save()
            if not init:
                return HttpResponseRedirect("/assets/server/type/list/")
    else:
        uf = ProjectForm()
    return render(request, 'assets/server_type_add.html', locals())


@login_required
@permission_required('account.access_cmdb')
def server_type_edit(request, uuid):
    """修改项目"""
    Server_Type = Project.objects.all()
    business_name = Project.objects.get(uuid=uuid)
    uf = ProjectForm(instance=business_name)
    if request.method == 'POST':
        uf = ProjectForm(request.POST, instance=business_name)
        if uf.is_valid():
            myform = uf.save()
            return render_to_response('assets/server_type_edit_ok.html', locals(),context_instance=RequestContext(request))
    return render(request, 'assets/server_type_edit.html', locals())


@login_required
@permission_required('account.access_cmdb')
def server_type_del(request, uuid):
    """业务删除"""
    if Project.objects.filter(uuid=uuid).count() > 0:
        business_name = Project.objects.get(uuid=uuid)
        business_name.delete()
    return HttpResponseRedirect("/assets/server/type/list/")


@login_required
@permission_required('account.access_cmdb')
def server_type_item(request):
    """此项目下的服务器"""
    service_name = request.GET.get("service_name")
    business_name = Project.objects.get(service_name=service_name)
    server_list = business_name.host_set.all()
    server_list_count = server_list.count()
    return render_to_response('assets/host_project_host.html', locals(), context_instance=RequestContext(request))


@login_required
@permission_required('account.access_cmdb')
def env(request):
    """此所属环境下的服务器"""
    env_name = request.GET.get("env_name")
    server_list = Host.objects.filter(env=env_name)
    server_list_count = server_list.count()
    return render_to_response('assets/host_project_host.html', locals(), context_instance=RequestContext(request))


@login_required
@permission_required('account.access_cmdb')
def service_add(request):
    """ 添加服务 """
    sf = ServiceForm()
    if request.method == 'POST':
        sf_post = ServiceForm(request.POST)
        if sf_post.is_valid():
            service_port = sf_post.cleaned_data.get('port')
            sf_post.save()
            return HttpResponseRedirect('/assets/service_list/')
    return my_render('assets/service_add.html', locals(), request)


@login_required
@permission_required('account.access_cmdb')
def service_list(request):
    """ 列出服务 """
    services = Service.objects.all()
    return my_render('assets/service_list.html', locals(), request)


@login_required
@permission_required('account.access_cmdb')
def service_edit(request):
    """ 编辑服务 """
    uuid = request.GET.get('uuid', '')
    service = get_object_or_404(Service, uuid=uuid)
    if request.method == 'POST':
        sf = ServiceForm(request.POST, instance=service)
        if sf.is_valid():
            sf.save()
            return HttpResponseRedirect("/assets/service_list/")
    else:
        sf = ServiceForm(instance=service)
        return my_render('assets/service_edit.html', locals(), request)


@login_required
@permission_required('account.access_cmdb')
def service_del(request):
    """ 删除服务 """
    uuid = request.GET.get('uuid')
    if uuid:
        service = get_object_or_404(Service, uuid=uuid)
        service.host_set.clear()
        service.delete()
        return HttpResponseRedirect('/assets/service_list/')
