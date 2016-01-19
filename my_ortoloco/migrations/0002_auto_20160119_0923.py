# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_ortoloco', '0001_initial'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='jobtype',
            name='bereicht',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='my_ortoloco.Taetigkeitsbereich'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobtype',
            name='descriptiont',
            field=models.TextField(default=b'', max_length=1000, verbose_name=b'Beschreibung'),
        ),
        migrations.AddField(
            model_name='jobtype',
            name='displayed_namet',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Angezeigter Name'),
        ),
        migrations.AddField(
            model_name='jobtype',
            name='durationt',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Dauer in Stunden'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobtype',
            name='locationt',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Ort'),
        ),
        migrations.AddField(
            model_name='jobtype',
            name='namet',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onetimejob',
            name='bereichp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='my_ortoloco.Taetigkeitsbereich'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onetimejob',
            name='descriptionp',
            field=models.TextField(default=b'', max_length=1000, verbose_name=b'Beschreibung'),
        ),
        migrations.AddField(
            model_name='onetimejob',
            name='displayed_namep',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Angezeigter Name'),
        ),
        migrations.AddField(
            model_name='onetimejob',
            name='durationp',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Dauer in Stunden'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onetimejob',
            name='locationp',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Ort'),
        ),
        migrations.AddField(
            model_name='onetimejob',
            name='namep',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Name'),
            preserve_default=False,
        ),
        
    ]
