# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_auto_20171102_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='user_oracle',
            field=models.CharField(max_length=30, null=True, verbose_name='user_oracle\u5bc6\u7801', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='user_wls81',
            field=models.CharField(max_length=30, null=True, verbose_name='user_wls81\u5bc6\u7801', blank=True),
            preserve_default=True,
        ),
    ]
