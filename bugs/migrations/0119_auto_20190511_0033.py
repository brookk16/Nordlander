# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0118_auto_20190511_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('Doing', 'Doing'), ('To do', 'To do')], default='To do', max_length=255),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Skills', 'Skills'), ('Items', 'Items'), ('Base game', 'Base game'), ('Worlds', 'Worlds'), ('Quests', 'Quests')], default='Base game', max_length=255),
        ),
    ]