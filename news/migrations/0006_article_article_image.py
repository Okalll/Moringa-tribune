# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='IMAGE', upload_to='articles/'),
        ),
    ]
