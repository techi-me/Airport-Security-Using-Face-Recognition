# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-02-24 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face_detection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=256)),
                ('bank_address', models.CharField(max_length=256)),
                ('bank_contact_number', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BankCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.FloatField(verbose_name=b'current_balance')),
                ('loan_status', models.CharField(max_length=256)),
                ('loan_date', models.DateField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_detection.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('crime_status', models.CharField(max_length=256)),
                ('crime_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('contact_number', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default=b'User', max_length=200),
        ),
        migrations.AddField(
            model_name='crime',
            name='polic_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_detection.PoliceStation'),
        ),
        migrations.AddField(
            model_name='crime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_detection.User'),
        ),
        migrations.AddField(
            model_name='bankcustomer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_detection.User'),
        ),
    ]
