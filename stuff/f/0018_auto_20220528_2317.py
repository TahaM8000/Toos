# Generated by Django 3.2.8 on 2022-05-28 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0017_alter_receipt_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
