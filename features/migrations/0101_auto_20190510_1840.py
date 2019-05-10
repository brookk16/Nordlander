# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0100_auto_20190510_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Available', 'Available'), ('Doing', 'Doing')], default='To do', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Quests', 'Quests'), ('Items', 'Items'), ('Skills', 'Skills'), ('Worlds', 'Worlds')], default='Items', max_length=10),
        ),
    ]
