# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mybasicmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('something', models.CharField(max_length=100)),
            ],
        ),
    ]
