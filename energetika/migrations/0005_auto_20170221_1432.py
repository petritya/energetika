# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energetika', '0004_felmeres_szla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='felmeres',
            name='szla',
            field=models.CharField(default='0', max_length=1),
        ),
    ]