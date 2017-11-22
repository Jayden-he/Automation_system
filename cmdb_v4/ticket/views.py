# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse, StreamingHttpResponse
from ticket.models import WorkSheet
from assets.models import Project
from forms import WorkSheetForm
from django.contrib.auth.decorators import login_required,permission_required
import time,os, sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
reload(sys)
sys.setdefaultencoding('utf-8')

upload = '/data/cmdb_v4/upload/'
#user = u'jayden'
#approval_user = u'zhihui'

#receiver = "zhihui.he@bqrzzl.com"
#subject = u"test python"
#text = u"this is python test email"
def SendEmail(receiver,subject,text):
    HOST = "smtp.exmail.qq.com"
    username = 'zhihui.he@bqrzzl.com'
    password = 'Qq346593733.'
    sender = "zhihui.he@bqrzzl.com"
    msg = MIMEText(text, 'utf-8')
    #msg['Subject'] = Header(subject, 'utf-8')
    # 中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # 连接SMTP服务器，然后发送信息
    smtp = smtplib.SMTP()
    smtp.connect(HOST)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def uploadfile(srcpath, descpath):
    for chunk in srcpath.chunks():
        descpath.write(chunk)
    descpath.close()

@login_required
@permission_required('account.access_ticket')
def downloadfile(request):
    def ReadFile(filename,chunk_size=512):
        with open(filename,'rb+') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    filename = request.GET.get('url')

    if filename:
        file = filename.split('/')[-1]
        response = StreamingHttpResponse(ReadFile(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
        return response

@login_required
@permission_required('account.access_ticket')
def release_apply(request):
    uf = WorkSheetForm()
    project_list = Project.objects.all()
    stream_num = str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
    if request.method == 'POST':
        version_num = request.POST.get('version','')
        version_num_str = str(version_num)
        #return HttpResponse(request.POST.get('online_date'))
        uf_post = WorkSheetForm(request.POST)
        if WorkSheet.objects.filter(version=version_num_str):
            emg = u'提交版本发布申请失败，该版本号%s已存在' % version_num_str
            return render(request, 'ticket/release_apply.html', locals())
        test_report = request.FILES.get('test_report', None)
        if not test_report:
            pass
        else:
            date = time.strftime("%Y_%m_%d", time.localtime())
            test_report_path = os.path.join(upload,"test_report/%s" % date )
            if os.path.isdir(test_report_path):
                pass
            else:
                os.makedirs(test_report_path)
            destination = open(os.path.join(test_report_path,test_report.name), 'wb')
            uploadfile(test_report,destination)
        if uf_post.is_valid():
            uf_post.save()
            initial = WorkSheet.objects.get(stream_num=request.POST.get('stream_num'))
            initial.initial_state = 0
            if test_report:
                initial.test_report = os.path.join(test_report_path,test_report.name)
            #initial.type = u'版本发布'
            initial.save()
            smg = u'提交版本发布申请成功'
            return render(request,'ticket/release_apply.html', locals())
    return render(request,'ticket/release_apply.html',locals())

@login_required
@permission_required('account.access_ticket')
def database_update_apply(request):
    uf = WorkSheetForm()
    project_list = Project.objects.all()
    stream_num = str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
    if request.method == 'POST':
        version_num = request.POST.get('version','')
        version_num_str = str(version_num)
        uf_post = WorkSheetForm(request.POST)
        if WorkSheet.objects.filter(version=version_num_str):
            emg = u'提交数据库更新申请失败，该版本号%s已存在' % version_num_str
            return render(request, 'ticket/database_update_apply.html', locals())
        db_script = request.FILES.get('db_script', None)
        if not db_script:
            pass
        else:
            date = time.strftime("%Y_%m_%d", time.localtime())
            db_script_path = os.path.join(upload,"db_script/%s" % date )
            if os.path.isdir(db_script_path):
                pass
            else:
                os.makedirs(db_script_path)
            destination = open(os.path.join(db_script_path,db_script.name), 'wb')
            uploadfile(db_script,destination)
        if uf_post.is_valid():
            uf_post.save()
            initial = WorkSheet.objects.get(stream_num=request.POST.get('stream_num'))
            initial.initial_state = 0
            if db_script:
                initial.script_path = os.path.join(db_script_path,db_script.name)
            initial.type = u'数据库更新'
            initial.save()
            smg = u'提交脚本申请成功'
            return render(request,'ticket/database_update_apply.html', locals())

    return render(request,'ticket/database_update_apply.html', locals())

@login_required
@permission_required('account.access_ticket')
def database_select_apply(request):
    uf = WorkSheetForm()
    project_list = Project.objects.all()
    stream_num = str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
    if request.method == 'POST':
        version_num = request.POST.get('version', '')
        version_num_str = str(version_num)
        #return HttpResponse(request.POST.get('project_name'))
        uf_post = WorkSheetForm(request.POST)
        if WorkSheet.objects.filter(version=version_num_str):
            emg = u'提交数据库查询申请失败，该版本号%s已存在' % version_num_str
            return render(request, 'ticket/database_select_apply.html', locals())
        db_script = request.FILES.get('db_script', None)
        if not db_script:
            pass
        else:
            date = time.strftime("%Y_%m_%d", time.localtime())
            db_script_path = os.path.join(upload, "db_script/%s" % date)
            if os.path.isdir(db_script_path):
                pass
            else:
                os.makedirs(db_script_path)
            destination = open(os.path.join(db_script_path, db_script.name), 'wb')
            uploadfile(db_script, destination)
        if uf_post.is_valid():
            uf_post.save()
            initial = WorkSheet.objects.get(stream_num=request.POST.get('stream_num'))
            initial.initial_state = 0
            if db_script:
                initial.script_path = os.path.join(db_script_path, db_script.name)
            initial.type = u'数据库查询'
            initial.save()
            smg = u'提交脚本申请成功'
            return render(request, 'ticket/database_select_apply.html', locals())
    return render(request,'ticket/database_select_apply.html', locals())

@login_required
@permission_required('account.access_ticket')
def malfunction_apply(request):
    uf = WorkSheetForm()
    project_list = Project.objects.all()
    stream_num = str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
    if request.method == 'POST':
        uf_post = WorkSheetForm(request.POST)
        if uf_post.is_valid():
            uf_post.save()
            initial = WorkSheet.objects.get(stream_num=request.POST.get('stream_num'))
            initial.initial_state = 0
            initial.type = u'故障申报'
            initial.save()
            smg = u'提交故障申报成功'
            return render(request, 'ticket/malfunction_apply.html', locals())
    return render(request,'ticket/malfunction_apply.html', locals())

@login_required
@permission_required('account.access_ticket')
@permission_required('account.access_role_manage')
def todo_worksheet(request):
    todo_list_WorkSheet = WorkSheet.objects.filter(initial_state=0)
    todo_list_count = todo_list_WorkSheet.count()
    return render(request,'ticket/todo_worksheet.html',locals())

@login_required
@permission_required('account.access_ticket')
def worksheet_detail(request):
    uuid = request.GET.get('uuid',None)
    version = get_object_or_404(WorkSheet, uuid=uuid)
    i = WorkSheet.objects.get(uuid=uuid)
    if request.method == 'POST':
        opinion = request.POST.get('opinion','')
        i.opinion = opinion
        i.initial_state = 1
        i.approval_user = request.user.username
        i.save()
        return HttpResponseRedirect('/ticket/todo_worksheet/')
    return render(request,'ticket/worksheet_detail.html',locals())

@login_required
@permission_required('account.access_ticket')
def create_detail(request):
    uuid = request.GET.get('uuid', None)
    version = get_object_or_404(WorkSheet, uuid=uuid)
    i = WorkSheet.objects.get(uuid=uuid)
    return render(request, 'ticket/create_detail.html', locals())

@login_required
@permission_required('account.access_ticket')
def create_worksheet(request):
    create_list = WorkSheet.objects.filter(user=request.user.username)
    create_list_count = create_list.count()
    return render(request,'ticket/create_worksheet.html',locals())

@login_required
@permission_required('account.access_ticket')
@permission_required('account.access_role_manage')
def approval_worksheet(request):
    """我审批的工单"""
    create_list = WorkSheet.objects.filter(approval_user=request.user.username)
    create_list_count = create_list.count()
    return render(request, 'ticket/create_worksheet.html', locals())