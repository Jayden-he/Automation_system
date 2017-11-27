# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0014_auto_20171106_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='mac',
            field=models.IPAddressField(null=True, verbose_name='mac\u5730\u5740', blank=True),
            preserve_default=True,
        ),
    ]
