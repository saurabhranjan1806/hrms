# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrms',
            name='CurrentTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
