# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='Services_Code',
            field=models.CharField(max_length=16, null=True, verbose_name='\u5feb\u901f\u670d\u52a1\u7f16\u7801', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='env',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u73af\u5883', choices=[('st', 'st'), ('aws', 'aws'), ('prod', 'prod'), ('pub', 'pub')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='idle',
            field=models.BooleanField(default=1, verbose_name='\u72b6\u6001', choices=[(True, b'\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad'), (False, b'\xe7\xa9\xba\xe9\x97\xb2')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='room_number',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u623f\u95f4\u53f7', choices=[('3-2', '3-2')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='server_sn',
            field=models.CharField(max_length=32, null=True, verbose_name='SN\u7f16\u53f7', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='service',
            field=models.ManyToManyField(to='assets.Service', null=True, verbose_name='\u8fd0\u884c\u670d\u52a1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='status',
            field=models.IntegerField(default=0, blank=True, verbose_name='\u673a\u5668\u72b6\u6001', choices=[(0, '\u672a\u5b89\u88c5\u7cfb\u7edf'), (1, '\u5df2\u5b89\u88c5\u7cfb\u7edf'), (2, '\u6b63\u5728\u5b89\u88c5\u7cfb\u7edf'), (3, '\u62a5\u5e9f')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='switch_port',
            field=models.CharField(max_length=12, null=True, verbose_name='\u7aef\u53e3\u53f7', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='type',
            field=models.IntegerField(default=1, max_length=2, verbose_name='\u4e3b\u673a\u7c7b\u578b', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='vm',
            field=models.ForeignKey(verbose_name='\u865a\u62df\u673a\u7236\u4e3b\u673a', blank=True, to='assets.Host', null=True),
            preserve_default=True,
        ),
    ]
