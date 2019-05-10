# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0100_auto_20190507_1727'),
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
            field=models.CharField(choices=[('Base game', 'Base game'), ('Worlds', 'Worlds'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Items', 'Items')], default='Base game', max_length=10),
        ),
    ]