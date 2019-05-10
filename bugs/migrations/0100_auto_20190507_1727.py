# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0099_auto_20190507_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Base game', 'Base game'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Worlds', 'Worlds'), ('Items', 'Items')], default='Base game', max_length=10),
        ),
    ]