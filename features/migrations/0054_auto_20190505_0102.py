# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-05 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0053_auto_20190502_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Available', 'Available'), ('Doing', 'Doing')], default='To do', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Items', 'Items'), ('Quests', 'Quests'), ('Skills', 'Skills')], default='Items', max_length=6),
        ),
    ]
