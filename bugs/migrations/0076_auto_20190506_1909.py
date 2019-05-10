# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-06 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0075_auto_20190506_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('Doing', 'Doing'), ('To do', 'To do')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Quests', 'Quests'), ('Worlds', 'Worlds'), ('Skills', 'Skills'), ('Items', 'Items'), ('Base game', 'Base game')], default='Base game', max_length=10),
        ),
    ]