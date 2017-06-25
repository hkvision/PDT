# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0002_auto_20151118_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemetric',
            name='interrupt',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='timerecord',
            name='duration',
            field=models.DurationField(),
        ),
    ]
