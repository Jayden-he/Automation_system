# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0011_auto_20171101_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='brand',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u4e3b\u673a\u5e94\u7528', choices=[('DB_Server', 'DB_Server'), ('APP_Server', 'APP_Server')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='env',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u6240\u5c5e\u73af\u5883', choices=[('PRD', 'PRD'), ('UAT_public', 'UAT_public'), ('UAT_independent', 'UAT_independent'), ('SIT_public', 'SIT_public'), ('SIT_independent', 'SIT_independent'), ('DEV', 'DEV'), ('int', 'int')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='eth1',
            field=models.IPAddressField(null=True, verbose_name='\u5185\u7f51\u5730\u5740', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='idle',
            field=models.BooleanField(default=1, verbose_name='\u4e3b\u673a\u72b6\u6001', choices=[(True, b'\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad'), (False, b'\xe7\xa9\xba\xe9\x97\xb2')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='internal_ip',
            field=models.IPAddressField(null=True, verbose_name='\u5916\u7f51\u5730\u5740', blank=True),
            preserve_default=True,
        ),
    ]
