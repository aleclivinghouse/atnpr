# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-04 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]