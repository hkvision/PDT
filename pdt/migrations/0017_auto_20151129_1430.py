# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0016_auto_20151126_2140'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='project',
            name='developerList',
            field=models.ManyToManyField(to='pdt.Developer'),
        ),
        # migrations.AddField(
        #     model_name='project',
        #     name='manager',
        #     field=models.ForeignKey(to='pdt.Manager', default=-1),
        # ),
    ]
