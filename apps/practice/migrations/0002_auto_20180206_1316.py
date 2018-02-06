# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-06 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='right_choice',
            field=models.SmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')], default=0, verbose_name='正确答案'),
        ),
        migrations.AlterField(
            model_name='choicequestion',
            name='name',
            field=models.CharField(max_length=50, verbose_name='题库名'),
        ),
    ]
