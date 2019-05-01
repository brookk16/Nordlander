# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0049_auto_20190428_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Doing', 'Doing'), ('To do', 'To do')], default='To do', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Quests', 'Quests'), ('Skills', 'Skills'), ('Worlds', 'Worlds'), ('Items', 'Items')], default='Items', max_length=6),
        ),
    ]