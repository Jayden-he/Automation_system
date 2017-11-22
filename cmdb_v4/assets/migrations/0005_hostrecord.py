# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_host_guarantee_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostRecord',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('user', models.CharField(max_length=30, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('host', models.ForeignKey(to='assets.Host')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
