# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20171030_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='guarantee_date',
            field=models.DateField(null=True, verbose_name='\u4fdd\u4fee\u65f6\u95f4', blank=True),
            preserve_default=True,
        ),
    ]
