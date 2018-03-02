# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 06:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0006_auto_20180226_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 1, 6, 18, 45, 877864, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_details.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
