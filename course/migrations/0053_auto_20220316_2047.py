# Generated by Django 3.2.8 on 2022-03-16 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0052_delete_plan_weeks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cover',
        ),
        migrations.DeleteModel(
            name='giude',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
