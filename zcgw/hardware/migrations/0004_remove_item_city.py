# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-30 09:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0003_auto_20160630_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='city',
        ),
    ]