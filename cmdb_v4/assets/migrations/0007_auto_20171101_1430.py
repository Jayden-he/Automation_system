# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20171101_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='mac',
        ),
        migrations.AddField(
            model_name='host',
            name='remote_port',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u8fdc\u7a0b\u7aef\u53e3', choices=[(22, 22), (10022, 10022), (8922, 8922)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='env',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u73af\u5883', choices=[('PRD', 'PRD'), ('UAT\u516c\u5171\u73af\u5883', 'UAT\u516c\u5171\u73af\u5883'), ('UAT\u72ec\u7acb\u73af\u5883', 'UAT\u72ec\u7acb\u73af\u5883'), ('SIT\u516c\u5171\u73af\u5883', 'SIT\u516c\u5171\u73af\u5883'), ('SIT\u72ec\u7acb\u73af\u5883', 'SIT\u72ec\u7acb\u73af\u5883'), ('DEV', 'DEV')]),
            preserve_default=True,
        ),
    ]
