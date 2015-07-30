# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20150730_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstripe',
            name='user',
        ),
    ]
