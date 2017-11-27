# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0016_auto_20171124_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='cpu_info',
            field=models.CharField(max_length=200, null=True, verbose_name='cpu\u4fe1\u606f', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='mount_all',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u6302\u8f7d\u4fe1\u606f', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='system_kernel',
            field=models.CharField(max_length=32, null=True, verbose_name='\u7cfb\u7edf\u5185\u6838', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='system',
            field=models.CharField(max_length=32, null=True, verbose_name='\u7cfb\u7edf\u7c7b\u578b', blank=True),
            preserve_default=True,
        ),
    ]
