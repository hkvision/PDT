# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0015_auto_20151126_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defectmetric',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='defectmetric',
            name='reqType',
        ),
        migrations.AddField(
            model_name='defectmetric',
            name='density',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='defectmetric',
            name='dyield',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='defectmetric',
            name='injected',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='defectmetric',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='defectmetric',
            name='removed',
            field=models.IntegerField(default=0),
        ),
    ]
