# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0007_auto_20150730_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstripe',
            name='user',
            field=models.OneToOneField(default=b'fail', to=settings.AUTH_USER_MODEL),
        ),
    ]
