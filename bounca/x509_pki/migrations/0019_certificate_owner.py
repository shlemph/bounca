# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 20:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('x509_pki', '0018_auto_20160517_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
