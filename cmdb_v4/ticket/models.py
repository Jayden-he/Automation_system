# -*- coding: UTF-8 -*-
from django.db import models

from uuidfield import UUIDField
from assets.models import Project

##Project = [
##   (i,i) for i in
#    (
#        u'CMS',
#        u'BCS',
#    )
#]

class WorkSheet(models.Model):
    uuid = UUIDField(auto=True, primary_key=True)
    stream_num = models.CharField(max_length=60, blank=True, verbose_name=u'工单编号')
    user = models.CharField(max_length=60,blank=True, verbose_name=u'提单人')
    work_title = models.CharField(max_length=200, blank=True, verbose_name=u'工单标题')
    project_name = models.CharField(max_length=200, blank=True, verbose_name=u'项目名称')
    version = models.CharField(max_length=100, blank=True, verbose_name=u'版本编号')
    script_path = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'脚本路径')
    version_path = models.CharField(max_length=200, blank=True, verbose_name=u'版本路径')
    online_date = models.CharField(max_length=100,blank=True, verbose_name=u'上线时间')
    version_update_content = models.CharField(max_length=500, blank=True, null=True,verbose_name=u'版本升级详情')
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'工单类型')
    initial_state = models.IntegerField(default=0, blank=True,verbose_name=u'初始状态', null=True)
    opinion = models.CharField(max_length=500, blank=True, null=True,verbose_name=u'审批意见')
    test_report = models.CharField(max_length=500, blank=True, null=True, verbose_name=u'测试报告路径')
    approval_user = models.CharField(max_length=60,blank=True, null=True, verbose_name=u'审批人')
    malfunction_content = models.CharField(max_length=500, blank=True, verbose_name=u'故障详情')
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.stream_num

    class Meta:
        verbose_name = u"工单申请"
        verbose_name_plural = verbose_name
