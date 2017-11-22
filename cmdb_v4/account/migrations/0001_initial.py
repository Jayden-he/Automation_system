# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'permissions': (('access_cmdb', 'access_cmdb'), ('access_ticket', 'access_ticket'), ('access_user_manage', 'access_user_manage'), ('access_role_manage', 'access_role_manage')),
            },
            bases=(models.Model,),
        ),
    ]
