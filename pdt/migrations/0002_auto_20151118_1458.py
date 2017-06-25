# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timerecord',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='timemetric',
            name='interrupt',
            field=models.DurationField(),
        ),
    ]
