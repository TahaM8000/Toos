# Generated by Django 4.0.1 on 2022-01-26 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20220124_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='text',
            new_name='lesson',
        ),
    ]
