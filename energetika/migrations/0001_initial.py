# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-23 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iranyitoszam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irSzam', models.IntegerField()),
                ('varos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Megrendeles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azonosito', models.CharField(max_length=10, verbose_name='Azonosító')),
                ('megrendeloNeve', models.CharField(max_length=100, verbose_name='Megrendelő neve')),
                ('ingatlanIrszam', models.IntegerField(verbose_name='Ingatlan irányítószám')),
                ('ingatlanVaros', models.CharField(max_length=100, verbose_name='Ingatlan város')),
                ('ingatlanCim', models.CharField(max_length=100, verbose_name='Ingatlan Cím')),
                ('felmeresIdopontja', models.DateTimeField()),
                ('felmeresDija', models.IntegerField(verbose_name='Felmérés díja')),
            ],
        ),
    ]