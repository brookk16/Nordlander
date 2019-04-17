# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0006_auto_20190417_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('DOING', 'Doing'), ('TODO', 'To do'), ('FIXED', 'Fixed!')], default='TODO', max_length=6),
        ),
    ]
