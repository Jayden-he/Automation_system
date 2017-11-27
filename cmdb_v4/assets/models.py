# -*- coding: UTF-8 -*-
from django.db import models
from uuidfield import UUIDField

 

System_os = [(i, i) for i in (u"CentOS", u"Windows")]
system_arch = [(i,i) for i in (u"x86_64", u"x64")]
Ssh_Port = [(i,i) for i in ("22","10022","8922")]
Server_Type = [
    (i, i) for i in
    (
        u"DB_Server",
        u"APP_Server",
    )
    ]

idc_type = (
    (0, u"CDN"),
    (1, u"核心")
)
	
idc_operator = (
    (0, u"电信"),
    (1, u"联通"),
    (2, u"移动"),
    (3, u"铁通"),
    (4, u"小带宽"),
)

SERVER_STATUS = (
    (0, u"未安装系统"),
    (1, u"已安装系统"),
    (2, u"正在安装系统"),
    (3, u"报废"),
)
ENVIRONMENT = [(i, i) for i in (u"PRD", u"UAT_public", u"UAT_independent", u"SIT_public", u"SIT_independent", u"DEV", u"int")]
BOOL_CHOICES = ((True, '使用中'), (False, '空闲'))
class IDC(models.Model):
	uuid = UUIDField(auto=True, primary_key=True)
	name = models.CharField(max_length=64, verbose_name=u'机房名称')
	bandwidth = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'机房带宽')
	phone = models.CharField(max_length=32, verbose_name=u'联系电话')
	linkman = models.CharField(max_length=32, null=True, verbose_name=u'联系人')
	address = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"机房地址")
	network = models.TextField(blank=True, null=True, verbose_name=u"IP地址段")
	create_time = models.DateField(auto_now=True)
	operator = models.IntegerField(verbose_name=u"运营商", choices=idc_operator, max_length=32, blank=True, null=True)
	type = models.IntegerField(verbose_name=u"机房类型", choices=idc_type, max_length=32, blank=True, null=True)
	comment = models.TextField(blank=True, null=True, verbose_name=u"备注")
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = u"IDC机房"
		verbose_name_plural = verbose_name
		app_label = 'assets'
	
class Project(models.Model):
	uuid = UUIDField(auto=True, primary_key=True)
	service_name = models.CharField(max_length=60, blank=True, null=True, verbose_name=u'项目名')
	aliases_name = models.CharField(max_length=60, blank=True, null=True, verbose_name=u'别名，用于监控')
	project_contact = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"主要负责人", )
	project_contact_backup = models.CharField(max_length=60, blank=True, null=True, verbose_name=u"第二负责人")
	description = models.TextField(blank=True, null=True, verbose_name=u'业务说明')
	project_doc = models.TextField(blank=True, null=True, verbose_name=u'业务维护说明')
	sort = models.IntegerField(max_length=100, blank=True, null=True, default=0, verbose_name=u"排序")
	
	def __unicode__(self):
		return self.service_name
	
	class Meta:
		verbose_name = u"业务"
		verbose_name_plural = verbose_name
	
	
class Service(models.Model):
	"""
    基础服务，如nginx, haproxy, php....
    """
	uuid = UUIDField(auto=True, primary_key=True)
	name = models.CharField(max_length=30, unique=True, verbose_name=u"服务名称",help_text=u'注意，所有服务操作全部期于linux服务操作，如: "service iptables restart"')
	port = models.IntegerField(null=True, blank=True, verbose_name=u"端口")
	remark = models.TextField(null=True, blank=True, verbose_name=u"备注")
	
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = u"服务"
		verbose_name_plural = verbose_name
		
class Host(models.Model):
	uuid = UUIDField(auto=True, primary_key=True)
	node_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"主机名")
	idc = models.ForeignKey(IDC, blank=True, null=True, verbose_name=u'机房', on_delete=models.SET_NULL)
	eth1 = models.IPAddressField(blank=True, null=True, verbose_name=u'内网地址')
	remote_port = models.CharField(max_length=64, choices=Ssh_Port, blank=True, null=True, verbose_name=u'远程端口')
	internal_ip = models.IPAddressField(blank=True, null=True, verbose_name=u'外网地址')
	mac = models.CharField(max_length=64,blank=True, null=True, verbose_name=u'mac地址')
	host_application = models.CharField(max_length=64, choices=Server_Type, blank=True, null=True, verbose_name=u'主机应用')
	cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'CPU')
	hard_disk = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'硬盘')
	memory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'内存')
	system = models.CharField(verbose_name=u"系统类型", max_length=32, blank=True,null=True, )
	system_cpuarch = models.CharField(max_length=32, blank=True, null=True, choices=system_arch, verbose_name=u"系统版本")
	system_kernel = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"系统内核")
	cpu_info = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"cpu信息")
	mount_all = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u"挂载信息")
	create_time = models.DateTimeField(auto_now_add=True)
	editor = models.TextField(blank=True, null=True, verbose_name=u'备注')
	business = models.ManyToManyField(Project, blank=True, null=True, verbose_name=u'所属业务')
	u"""
    0   未安装系统
    1   已安装系统
    2   正在安装中
    3   报废
    """
	status = models.IntegerField(verbose_name=u"机器状态", choices=SERVER_STATUS, default=0, blank=True)
	vm = models.ForeignKey("self", blank=True, null=True, verbose_name=u"虚拟机父主机")
	env = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"所属环境", choices=ENVIRONMENT)
	switch_port = models.CharField(verbose_name=u"端口号", max_length=12, blank=True, null=True)
	service = models.ManyToManyField(Service, verbose_name=u'运行服务', blank=True, null=True)
	idle = models.BooleanField(verbose_name=u'主机状态', default=1, choices=BOOL_CHOICES)
	user_root = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"user_root密码")
	user_weblogic = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"user_weblogic密码")
	user_bqadm = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"user_bqadm密码")
	user_deploy = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"user_deploy密码")
	user_wls81 = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"user_wls81密码")
	user_oracle = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"user_oracle密码")
	def __unicode__(self):
		return self.node_name
		
	class Meta:
		verbose_name = u"服务器"
		verbose_name_plural = verbose_name
		
class HostRecord(models.Model):
	""" 主机修改记录model """
	uuid = UUIDField(auto=True, primary_key=True)
	host = models.ForeignKey(Host)
	user = models.CharField(max_length=30, null=True)
	time = models.DateTimeField(auto_now_add=True)
	content = models.TextField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
