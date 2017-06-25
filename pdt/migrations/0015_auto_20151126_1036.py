# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0014_auto_20151125_0000'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='defectrecord',
        #     name='iterID',
        # ),
        # migrations.AddField(
        #     model_name='defectrecord',
        #     name='injectIter',
        #     field=models.ForeignKey(related_name='injectIter', to='pdt.Iteration', default=-1),
        # ),
        # migrations.AddField(
        #     model_name='defectrecord',
        #     name='removeIter',
        #     field=models.ForeignKey(related_name='removeIter', to='pdt.Iteration', default=-1),
        # ),
        # migrations.AddField(
        #     model_name='project',
        #     name='manager',
        #     field=models.ForeignKey(to='pdt.Manager', default=-1),
        # ),
    ]
