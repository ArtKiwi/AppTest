# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170427_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
