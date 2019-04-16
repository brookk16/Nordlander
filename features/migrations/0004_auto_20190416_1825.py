# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-16 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20190416_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('DOING', 'Doing'), ('AVAILABLE', 'Available'), ('TODO', 'To do')], default='TODO', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('QUESTS', 'Quests'), ('WORLD', 'World'), ('ITEM', 'Item'), ('SKILLS', 'Skills')], default='ITEM', max_length=6),
        ),
    ]
