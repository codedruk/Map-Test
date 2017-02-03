# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('zip_code', models.CharField(default='90051', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='GasStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=200)),
                ('gas_price', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ['station_name'],
            },
        ),
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_name', models.CharField(max_length=200)),
                ('rest_rating', models.CharField(max_length=1)),
            ],
            options={
                'ordering': ['rest_name'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=200)),
                ('store_type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['store_name'],
            },
        ),
        migrations.AddField(
            model_name='arealocation',
            name='rests',
            field=models.ManyToManyField(to='map_app.Rest'),
        ),
        migrations.AddField(
            model_name='arealocation',
            name='stations',
            field=models.ManyToManyField(to='map_app.GasStation'),
        ),
        migrations.AddField(
            model_name='arealocation',
            name='stores',
            field=models.ManyToManyField(to='map_app.Store'),
        ),
    ]