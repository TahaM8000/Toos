# Generated by Django 3.2.8 on 2022-02-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0004_stuff_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_peyment',
            field=models.IntegerField(),
        ),
    ]
