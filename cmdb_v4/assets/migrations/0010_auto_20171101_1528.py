# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_auto_20171101_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='eth2',
        ),
        migrations.AlterField(
            model_name='host',
            name='eth1',
            field=models.IPAddressField(null=True, verbose_name='\u7f51\u5361', blank=True),
            preserve_default=True,
        ),
    ]
