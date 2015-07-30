# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'profiles', '0001_initial'), (b'profiles', '0002_profile_description'), (b'profiles', '0003_profile_location'), (b'profiles', '0004_auto_20150707_0120'), (b'profiles', '0005_profile_job'), (b'profiles', '0006_auto_20150707_0125'), (b'profiles', '0007_auto_20150730_0820'), (b'profiles', '0008_userstripe_user'), (b'profiles', '0009_auto_20150730_1833'), (b'profiles', '0010_remove_userstripe_user')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1200)),
                ('description', models.TextField(default=b'description default')),
                ('location', models.CharField(default=b'My Location', max_length=1200, blank=True)),
                ('job', models.CharField(max_length=1200, null=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userStripe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stripe_id', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
