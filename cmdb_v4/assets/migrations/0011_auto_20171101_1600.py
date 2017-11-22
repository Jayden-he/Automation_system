# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_auto_20171101_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='user_bqadm',
            field=models.CharField(max_length=30, null=True, verbose_name='user_bqadm\u5bc6\u7801', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='user_deploy',
            field=models.CharField(max_length=30, null=True, verbose_name='user_deploy\u5bc6\u7801', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='user_root',
            field=models.CharField(max_length=30, null=True, verbose_name='user_root\u5bc6\u7801', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='user_weblogic',
            field=models.CharField(max_length=30, null=True, verbose_name='user_weblogic\u5bc6\u7801', blank=True),
            preserve_default=True,
        ),
    ]
