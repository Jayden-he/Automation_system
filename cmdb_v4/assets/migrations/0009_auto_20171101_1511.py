# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_auto_20171101_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='remote_port',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u8fdc\u7a0b\u7aef\u53e3', choices=[(b'22', b'22'), (b'10022', b'10022'), (b'8922', b'8922')]),
            preserve_default=True,
        ),
    ]
