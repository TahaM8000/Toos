# Generated by Django 3.2.8 on 2021-10-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_code',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
