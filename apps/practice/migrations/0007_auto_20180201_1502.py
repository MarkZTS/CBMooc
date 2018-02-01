# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-01 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_bannercourse'),
        ('practice', '0006_auto_20180201_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicequestion',
            name='Course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='programming',
            name='Course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程'),
        ),
    ]