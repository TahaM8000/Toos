# Generated by Django 3.2.9 on 2022-01-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_rename_lesson_teacher_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='giude',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
