# Generated by Django 3.2.8 on 2022-03-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0048_remove_package_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kind',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]
