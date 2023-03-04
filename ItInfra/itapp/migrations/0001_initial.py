# Generated by Django 4.1.5 on 2023-01-22 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('Id_Numbeer', models.CharField(blank=True, max_length=100)),
                ('Class', models.CharField(blank=True, max_length=50)),
                ('Description', models.TextField(default='no remarks')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Itdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Device_Name', models.CharField(blank=True, max_length=100)),
                ('Device_Serial', models.CharField(blank=True, max_length=100)),
                ('Issued_To', models.CharField(blank=True, max_length=100)),
                ('other', models.TextField(default='no remarks')),
                ('Remarks', models.TextField(default='no remarks')),
            ],
        ),
    ]
