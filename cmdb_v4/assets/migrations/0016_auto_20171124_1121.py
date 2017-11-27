# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_host_mac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='mac',
            field=models.CharField(max_length=64, null=True, verbose_name='mac\u5730\u5740', blank=True),
            preserve_default=True,
        ),
    ]
