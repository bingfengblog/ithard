# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-29 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(default=b'i3\xe4\xb8\xbb\xe6\x9c\xba', max_length=20)),
            ],
        ),
    ]
