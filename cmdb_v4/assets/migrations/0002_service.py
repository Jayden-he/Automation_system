# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('name', models.CharField(help_text='\u6ce8\u610f\uff0c\u6240\u6709\u670d\u52a1\u64cd\u4f5c\u5168\u90e8\u671f\u4e8elinux\u670d\u52a1\u64cd\u4f5c\uff0c\u5982: "service iptables restart"', unique=True, max_length=30, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('port', models.IntegerField(null=True, verbose_name='\u7aef\u53e3', blank=True)),
                ('remark', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1',
                'verbose_name_plural': '\u670d\u52a1',
            },
            bases=(models.Model,),
        ),
    ]
