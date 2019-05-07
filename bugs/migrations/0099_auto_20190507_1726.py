# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0098_auto_20190507_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Doing', 'Doing'), ('To do', 'To do'), ('Fixed', 'Fixed')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Quests', 'Quests'), ('Skills', 'Skills'), ('Base game', 'Base game'), ('Items', 'Items'), ('Worlds', 'Worlds')], default='Base game', max_length=10),
        ),
    ]
