# Generated by Django 4.1.1 on 2022-10-04 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 10, 4, 7, 41, 43, 2322, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 10, 4, 7, 41, 43, 2396, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
