# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_hostrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='Services_Code',
        ),
        migrations.RemoveField(
            model_name='host',
            name='cabinet',
        ),
        migrations.RemoveField(
            model_name='host',
            name='guarantee_date',
        ),
        migrations.RemoveField(
            model_name='host',
            name='number',
        ),
        migrations.RemoveField(
            model_name='host',
            name='room_number',
        ),
        migrations.RemoveField(
            model_name='host',
            name='server_cabinet_id',
        ),
        migrations.RemoveField(
            model_name='host',
            name='server_sn',
        ),
        migrations.RemoveField(
            model_name='host',
            name='system_version',
        ),
        migrations.RemoveField(
            model_name='host',
            name='type',
        ),
        migrations.AlterField(
            model_name='host',
            name='brand',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u670d\u52a1\u5668\u5e94\u7528', choices=[('\u6570\u636e\u5e93\u670d\u52a1\u5668', '\u6570\u636e\u5e93\u670d\u52a1\u5668'), ('\u5e94\u7528\u670d\u52a1\u5668', '\u5e94\u7528\u670d\u52a1\u5668')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='system_cpuarch',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7cfb\u7edf\u7248\u672c', choices=[('x86_64', 'x86_64'), ('x64', 'x64')]),
            preserve_default=True,
        ),
    ]
