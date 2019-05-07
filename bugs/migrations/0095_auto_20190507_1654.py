# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0094_auto_20190507_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Doing', 'Doing'), ('Fixed', 'Fixed')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Items', 'Items'), ('Base game', 'Base game'), ('Skills', 'Skills'), ('Quests', 'Quests')], default='Base game', max_length=10),
        ),
    ]
