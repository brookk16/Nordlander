# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-06 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0062_auto_20190506_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Doing', 'Doing'), ('Available', 'Available')], default='To do', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Items', 'Items'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Worlds', 'Worlds')], default='Items', max_length=6),
        ),
    ]
