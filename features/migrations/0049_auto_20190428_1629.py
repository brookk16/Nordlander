# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0048_auto_20190428_1623'),
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
            field=models.CharField(choices=[('Worlds', 'World'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Items', 'Item')], default='Items', max_length=6),
        ),
    ]