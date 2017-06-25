# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefectMetric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reqType', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DefectRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtype', models.CharField(default='default', max_length=20)),
                ('desc', models.TextField(default='(None)')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pin', models.CharField(default='default', max_length=20)),
                ('name', models.CharField(default='default', max_length=100)),
                ('email', models.EmailField(default='none@default.com', max_length=254)),
                ('online', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.TextField(default='(None)')),
                ('status', models.CharField(default='default', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pin', models.CharField(default='default', max_length=20)),
                ('name', models.CharField(default='default', max_length=100)),
                ('email', models.EmailField(default='none@default.com', max_length=254)),
                ('online', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default', max_length=20)),
                ('desc', models.TextField(default='(None)')),
                ('status', models.CharField(default='default', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default', max_length=100)),
                ('desc', models.TextField(default='(None)')),
                ('status', models.CharField(default='default', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('did', models.ForeignKey(to='pdt.DefectMetric', default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='SizeMetric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estimated', models.IntegerField(default=0)),
                ('actual', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TimeMetric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('interrupt', models.DurationField()),
                ('offtask', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('devID', models.ForeignKey(to='pdt.Developer', default=-1)),
                ('iterID', models.ForeignKey(to='pdt.Iteration', default=-1)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='sid',
            field=models.ForeignKey(to='pdt.SizeMetric', default=-1),
        ),
        migrations.AddField(
            model_name='report',
            name='tid',
            field=models.ForeignKey(to='pdt.TimeMetric', default=-1),
        ),
        migrations.AddField(
            model_name='project',
            name='report',
            field=models.ForeignKey(to='pdt.Report', default=-1),
        ),
        migrations.AddField(
            model_name='phase',
            name='projID',
            field=models.ForeignKey(to='pdt.Project', default=-1),
        ),
        migrations.AddField(
            model_name='phase',
            name='report',
            field=models.ForeignKey(to='pdt.Report', default=-1),
        ),
        migrations.AddField(
            model_name='manager',
            name='project',
            field=models.ManyToManyField(to='pdt.Project'),
        ),
        migrations.AddField(
            model_name='iteration',
            name='phaseID',
            field=models.ForeignKey(to='pdt.Phase', default=-1),
        ),
        migrations.AddField(
            model_name='iteration',
            name='report',
            field=models.ForeignKey(to='pdt.Report', default=-1),
        ),
        migrations.AddField(
            model_name='developer',
            name='iteration',
            field=models.ManyToManyField(to='pdt.Iteration'),
        ),
        migrations.AddField(
            model_name='defectrecord',
            name='devID',
            field=models.ForeignKey(to='pdt.Developer', default=-1),
        ),
        migrations.AddField(
            model_name='defectrecord',
            name='iterID',
            field=models.ForeignKey(to='pdt.Iteration', default=-1),
        ),
    ]
