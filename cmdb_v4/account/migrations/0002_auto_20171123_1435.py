# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accesscontrol',
            options={'permissions': (('access_cmdb', 'access_cmdb'), ('access_ticket', 'access_ticket'), ('access_role_manage', 'access_role_manage'))},
        ),
    ]
