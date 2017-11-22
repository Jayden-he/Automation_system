# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('node_name', models.CharField(max_length=100, null=True, verbose_name='\u4e3b\u673a\u540d', blank=True)),
                ('eth1', models.IPAddressField(null=True, verbose_name='\u7f51\u53611', blank=True)),
                ('eth2', models.IPAddressField(null=True, verbose_name='\u7f51\u53612', blank=True)),
                ('mac', models.CharField(max_length=20, null=True, verbose_name='MAC', blank=True)),
                ('internal_ip', models.IPAddressField(null=True, verbose_name='\u8fdc\u63a7\u5361', blank=True)),
                ('brand', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u786c\u4ef6\u5382\u5546', choices=[('\u963f\u91cc\u4e91', '\u963f\u91cc\u4e91'), ('\u7269\u7406\u673a', '\u7269\u7406\u673a')])),
                ('cpu', models.CharField(max_length=64, null=True, verbose_name='CPU', blank=True)),
                ('hard_disk', models.CharField(max_length=128, null=True, verbose_name='\u786c\u76d8', blank=True)),
                ('memory', models.CharField(max_length=128, null=True, verbose_name='\u5185\u5b58', blank=True)),
                ('system', models.CharField(default=b'CentOS', choices=[('CentOS', 'CentOS'), ('Windows', 'Windows')], max_length=32, blank=True, null=True, verbose_name='\u7cfb\u7edf\u7c7b\u578b')),
                ('system_cpuarch', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7cfb\u7edf\u7248\u672c', choices=[('x86_64', 'x86_64')])),
                ('system_version', models.CharField(max_length=8, null=True, verbose_name='\u7248\u672c\u53f7', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('cabinet', models.CharField(max_length=32, null=True, verbose_name='\u673a\u67dc\u53f7', blank=True)),
                ('server_cabinet_id', models.IntegerField(null=True, verbose_name='\u673a\u5668\u4f4d\u7f6e', blank=True)),
                ('number', models.CharField(max_length=32, null=True, verbose_name='\u8d44\u4ea7\u7f16\u53f7', blank=True)),
                ('editor', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('bandwidth', models.CharField(max_length=64, null=True, verbose_name='\u673a\u623f\u5e26\u5bbd', blank=True)),
                ('phone', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('linkman', models.CharField(max_length=32, null=True, verbose_name='\u8054\u7cfb\u4eba')),
                ('address', models.CharField(max_length=128, null=True, verbose_name='\u673a\u623f\u5730\u5740', blank=True)),
                ('network', models.TextField(null=True, verbose_name='IP\u5730\u5740\u6bb5', blank=True)),
                ('create_time', models.DateField(auto_now=True)),
                ('operator', models.IntegerField(blank=True, max_length=32, null=True, verbose_name='\u8fd0\u8425\u5546', choices=[(0, '\u7535\u4fe1'), (1, '\u8054\u901a'), (2, '\u79fb\u52a8'), (3, '\u94c1\u901a'), (4, '\u5c0f\u5e26\u5bbd')])),
                ('type', models.IntegerField(blank=True, max_length=32, null=True, verbose_name='\u673a\u623f\u7c7b\u578b', choices=[(0, 'CDN'), (1, '\u6838\u5fc3')])),
                ('comment', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': 'IDC\u673a\u623f',
                'verbose_name_plural': 'IDC\u673a\u623f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('service_name', models.CharField(max_length=60, null=True, verbose_name='\u9879\u76ee\u540d', blank=True)),
                ('aliases_name', models.CharField(max_length=60, null=True, verbose_name='\u522b\u540d\uff0c\u7528\u4e8e\u76d1\u63a7', blank=True)),
                ('project_contact', models.CharField(max_length=60, null=True, verbose_name='\u4e3b\u8981\u8d1f\u8d23\u4eba', blank=True)),
                ('project_contact_backup', models.CharField(max_length=60, null=True, verbose_name='\u7b2c\u4e8c\u8d1f\u8d23\u4eba', blank=True)),
                ('description', models.TextField(null=True, verbose_name='\u4e1a\u52a1\u8bf4\u660e', blank=True)),
                ('project_doc', models.TextField(null=True, verbose_name='\u4e1a\u52a1\u7ef4\u62a4\u8bf4\u660e', blank=True)),
                ('sort', models.IntegerField(default=0, max_length=100, null=True, verbose_name='\u6392\u5e8f', blank=True)),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1',
                'verbose_name_plural': '\u4e1a\u52a1',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='host',
            name='business',
            field=models.ManyToManyField(to='assets.Project', null=True, verbose_name='\u6240\u5c5e\u4e1a\u52a1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u673a\u623f', blank=True, to='assets.IDC', null=True),
            preserve_default=True,
        ),
    ]
