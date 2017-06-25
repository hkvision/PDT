# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0003_auto_20151118_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='timemetric',
            name='used',
            field=models.DurationField(),
            preserve_default=False,
        ),
    ]
