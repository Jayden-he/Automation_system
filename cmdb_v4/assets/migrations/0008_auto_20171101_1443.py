# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20171101_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='internal_ip',
            field=models.IPAddressField(null=True, verbose_name='\u5916\u7f51IP', blank=True),
            preserve_default=True,
        ),
    ]
