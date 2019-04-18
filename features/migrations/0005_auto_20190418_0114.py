# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_auto_20190418_0013'),
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
            field=models.CharField(choices=[('Item', 'Item'), ('Quests', 'Quests'), ('World', 'World'), ('Skills', 'Skills')], default='Item', max_length=6),
        ),
    ]
