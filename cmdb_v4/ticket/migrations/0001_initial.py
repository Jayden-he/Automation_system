# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSheet',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('stream_num', models.CharField(max_length=60, verbose_name='\u5de5\u5355\u7f16\u53f7', blank=True)),
                ('user', models.CharField(max_length=60, verbose_name='\u63d0\u5355\u4eba', blank=True)),
                ('work_title', models.CharField(max_length=200, verbose_name='\u5de5\u5355\u6807\u9898', blank=True)),
                ('project_name', models.CharField(max_length=200, verbose_name='\u9879\u76ee\u540d\u79f0', blank=True)),
                ('version', models.CharField(max_length=100, verbose_name='\u7248\u672c\u7f16\u53f7', blank=True)),
                ('script_path', models.CharField(max_length=200, null=True, verbose_name='\u811a\u672c\u8def\u5f84', blank=True)),
                ('version_path', models.CharField(max_length=200, verbose_name='\u7248\u672c\u8def\u5f84', blank=True)),
                ('online_date', models.CharField(max_length=100, verbose_name='\u4e0a\u7ebf\u65f6\u95f4', blank=True)),
                ('version_update_content', models.CharField(max_length=500, null=True, verbose_name='\u7248\u672c\u5347\u7ea7\u8be6\u60c5', blank=True)),
                ('type', models.CharField(max_length=50, null=True, verbose_name='\u5de5\u5355\u7c7b\u578b', blank=True)),
                ('initial_state', models.IntegerField(default=0, null=True, verbose_name='\u521d\u59cb\u72b6\u6001', blank=True)),
                ('opinion', models.CharField(max_length=500, null=True, verbose_name='\u5ba1\u6279\u610f\u89c1', blank=True)),
                ('test_report', models.CharField(max_length=500, null=True, verbose_name='\u6d4b\u8bd5\u62a5\u544a\u8def\u5f84', blank=True)),
                ('approval_user', models.CharField(max_length=60, null=True, verbose_name='\u5ba1\u6279\u4eba', blank=True)),
                ('malfunction_content', models.CharField(max_length=500, verbose_name='\u6545\u969c\u8be6\u60c5', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u5de5\u5355\u7533\u8bf7',
                'verbose_name_plural': '\u5de5\u5355\u7533\u8bf7',
            },
            bases=(models.Model,),
        ),
    ]
