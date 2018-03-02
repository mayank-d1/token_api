# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 06:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0007_auto_20180227_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 4, 6, 46, 10, 495276, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(blank=True, default=uuid.UUID('18a739aa-8c75-4caf-a881-a37b8b98c0ff'), max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='user_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]