# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0012_auto_20171102_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='brand',
            new_name='host_application',
        ),
    ]
