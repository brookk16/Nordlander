# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0077_auto_20190507_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('Doing', 'Doing'), ('To do', 'To do'), ('Available', 'Available')], default='To do', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Quests', 'Quests'), ('Items', 'Items'), ('Skills', 'Skills')], default='Items', max_length=6),
        ),
    ]
