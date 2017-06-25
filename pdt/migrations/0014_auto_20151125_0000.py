# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0012_auto_20151124_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizemetric',
            name='actEffort',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='sizemetric',
            name='estmEffort',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
