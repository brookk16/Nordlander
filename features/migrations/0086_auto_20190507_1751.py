# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0085_auto_20190507_1727'),
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
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Items', 'Items')], default='Items', max_length=6),
        ),
    ]
