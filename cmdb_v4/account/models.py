# -*- coding: UTF-8 -*-
from django.db import models

class AccessControl(models.Model):
    """
    自定义权限控制
    """
    class Meta:
        permissions = (
            ("access_cmdb",u'access_cmdb'),
            ("access_ticket", u'access_ticket'),
            #("access_user_manage", u'access_user_manage'),
            ("access_role_manage", u'access_role_manage'),
        )
