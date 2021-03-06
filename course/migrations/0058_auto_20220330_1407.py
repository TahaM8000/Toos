# Generated by Django 3.2.8 on 2022-03-30 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0057_course_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='session_coruse',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='session_coruse',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
