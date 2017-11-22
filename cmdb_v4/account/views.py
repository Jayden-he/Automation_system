#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response,HttpResponseRedirect,redirect,get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, Group, Permission

def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username='%s' % username, password='%s' % password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(request.GET['next'])
	return render(request,'account/login.html', locals())

	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def user_registration(request):
    """注册操作"""
    if request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        try:
            User.objects.get(username=username)
            emg = u"%s用户已经存在" % username
        except User.DoesNotExist:
            user = User.objects.create_user(username,email,password)
            groups = Group.objects.get(name='Access_ticket')
            user.groups.add(groups)
            smg = u'%s用户创建成功' % username
    return render(request, 'account/registration.html', locals())

@login_required
def basic_info(request):
    user = request.user.username
    email = request.user.email
    create_time = request.user.date_joined
    group_list = User.objects.get(username=user).groups.all()
    if request.method == 'POST':
        oldpassword = request.POST.get('oldpassword', '')
        newpassword = request.POST.get('newpassword', '')
        User_Name = authenticate(username=user,password=oldpassword)
        if User_Name is not None:
            Password = User.objects.get(username=user)
            Password.set_password(newpassword)
            Password.save()
            smg = u'修改成功'
        else:
            emg = u'旧密码错误'
    return render(request,'account/basic_info.html',locals())

@login_required
@permission_required('account.access_role_manage')
def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        try:
            User.objects.get(username=username)
            emg = u"%s用户存在" % username
        except User.DoesNotExist:
            user = User.objects.create_user(username,email,password)
            groups = Group.objects.get(name='Access_ticket')
            user.groups.add(groups)
            smg = u'%s用户创建成功' % username
            return render(request, 'account/create_user.html', locals())
    return render(request,'account/create_user.html',locals())

@permission_required('account.access_role_manage')
@login_required
def del_user(request):
    user_list = User.objects.all()
    if request.method == 'POST':
        get_users_list = request.REQUEST.getlist("get_users")
        for get_user in get_users_list:
            try:
                del_username = User.objects.get(username=get_user)
                del_username.delete()
                data = u'该用户已删除'
            except User.DoesNotExist:
                data = u"该用户不存在"
        return render(request, 'account/del_user.html', locals())
    return render(request,'account/del_user.html',locals())

@login_required
@permission_required('account.access_role_manage')
def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('name','')
        cmdb_manage = request.POST.get('cmdb_manage', '')
        role_manage = request.POST.get('role_manage', '')
        user_manage = request.POST.get('user_manage', '')
        ticket_manage = request.POST.get('ticket_manage', '')
        get_users = request.POST.get('get_users','None')
        try:
            Group.objects.get(name=group_name)
            emg = u'存在%s组' % group_name
        except Group.DoesNotExist:
            groups = Group.objects.create(name=group_name)
            if cmdb_manage == 'true':
                permission = Permission.objects.get(codename='access_cmdb')
                groups.permissions.add(permission)
            if role_manage == 'true':
                permission = Permission.objects.get(codename='access_role_manage')
                groups.permissions.add(permission)
            if user_manage == 'true':
                permission = Permission.objects.get(codename='access_user_manage')
                groups.permissions.add(permission)
            if ticket_manage == 'true':
                permission = Permission.objects.get(codename='access_ticket')
                groups.permissions.add(permission)
            smg = u'%s组创建成功'% group_name
            return render(request,'account/create_group.html',locals())
    return render(request,'account/create_group.html',locals())

@login_required
@permission_required('account.access_role_manage')
def del_group(request):
    group_list = Group.objects.all()
    permissions_dict = {}
    for i in group_list:
        b = i.permissions.all()
        permissions_list = []
        if b:
            for k in b:
                permissions_list.append(k.name)
            permissions_dict[i] = permissions_list
        else:
            permissions_dict[i] = 'None'

    if request.method == 'POST':
        get_groups_list = request.REQUEST.getlist("get_groups")
        for get_group in get_groups_list:
            try:
                del_groupname = Group.objects.get(name=get_group)
                del_groupname.delete()
                emg = u'该用户组已删除'
            except Group.DoesNotExist:
                smg = u'该用户组不存在'
    return render(request,'account/del_group.html',locals())

@login_required
@permission_required('account.access_role_manage')
def user_to_group(request):
    group_list = Group.objects.all()
    user_list = User.objects.all()
    if request.method == 'POST':
        group_name = request.POST.get('group_name',None)
        get_users_list = request.REQUEST.getlist("get_users")
        groups = Group.objects.get(name=group_name)
        for get_user in get_users_list:
            try:
                db_user = User.objects.get(username=get_user)
                db_user.groups.add(groups)
                smg = u'添加成功'
            except User.DoesNotExist:
                emg = u'%s用户不存在' % get_user
    return render(request,'account/user_to_group.html',locals())

@login_required
@permission_required('account.access_role_manage')
def group_del_user(request):
    group_list = Group.objects.all()
    user_list = User.objects.all()
    if request.method == 'POST':
        group_name = request.POST.get('group_name', None)
        get_users_list = request.REQUEST.getlist("get_users")
        groups = Group.objects.get(name=group_name)
        for get_user in get_users_list:
            try:
                db_user = User.objects.get(username=get_user)
                db_user.groups.remove(groups)
                smg = u'从组内删除用户成功'
            except User.DoesNotExist:
                emg = u'%s用户不存在' % get_user
    return render(request, 'account/group_del_user.html', locals())

@login_required
@permission_required('account.access_role_manage')
def group_permission_modif(request):
    group_name = request.GET.get('group_name',None)
    Group_Name = Group.objects.get(name=group_name)
    Permission_list = Group_Name.permissions.all()
    Permission_all = Permission.objects.all()
    if request.method == 'POST':
        want_del = request.POST.get('want_del',None)
        want_add = request.POST.get('want_add',None)
        if want_add is not None:
            permission = Permission.objects.get(codename=want_add)
            Group_Name.permissions.add(permission)
        if want_del is not None:
            permission = Permission.objects.get(codename=want_del)
            Group_Name.permissions.remove(permission)
        return HttpResponseRedirect('account/permission_info')
    return render(request,'account/group_permission_modif.html',locals())

@login_required
@permission_required('account.access_role_manage')
def permission_info(request):
    group_dict = {}
    permissions_dict = {}
    group_list = Group.objects.all()
    for i in group_list:
        a = i.user_set.all()
        user_list = []
        if a:
            for j in a:
                user_list.append(j.username)
            group_dict[i] = user_list
        else:
            group_dict[i] = 'None'

        b = i.permissions.all()
        permissions_list = []
        if b:
            for k in b:
                permissions_list.append(k.name)
            permissions_dict[i] = permissions_list
        else:
            permissions_dict[i] = 'None'
    return render(request,'account/permission_info.html',locals())