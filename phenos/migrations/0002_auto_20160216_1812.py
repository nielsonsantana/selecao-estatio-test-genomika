# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phenos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='disease',
            name='genes',
            field=models.ManyToManyField(through='phenos.DiseaseGene', to='phenos.Gene'),
        ),
    ]