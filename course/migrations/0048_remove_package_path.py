# Generated by Django 3.2.8 on 2022-03-07 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0047_auto_20220307_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='path',
        ),
    ]
