# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0005_auto_20151118_1526'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='project',
        #     name='manager',
        #     field=models.ForeignKey(to='pdt.Manager', default=1),
        # ),

        migrations.RenameField(
            model_name='sizemetric',
            old_name='actual',
            new_name='actSLOC',
        ),
        migrations.RenameField(
            model_name='sizemetric',
            old_name='estimated',
            new_name='estmSLOC',
        ),
        migrations.RenameField(
            model_name='timemetric',
            old_name='offtask',
            new_name='delta',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='project',
        ),
        migrations.RemoveField(
            model_name='timemetric',
            name='used',
        ),
        migrations.RemoveField(
            model_name='timerecord',
            name='end',
        ),
        migrations.RemoveField(
            model_name='timerecord',
            name='start',
        ),
        migrations.AddField(
            model_name='iteration',
            name='name',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='currIter',
            field=models.ForeignKey(default=2, to='pdt.Iteration'),
        ),
        migrations.AddField(
            model_name='sizemetric',
            name='SperE',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='sizemetric',
            name='actEffort',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='sizemetric',
            name='estmEffort',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='phase',
            name='name',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(default=0, to='pdt.Manager'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='--', max_length=100),
        ),
    ]
