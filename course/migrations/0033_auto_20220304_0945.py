# Generated by Django 3.2.8 on 2022-03-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0032_course_video_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='text',
            new_name='lesson',
        ),
        migrations.AddField(
            model_name='teacher',
            name='reshte_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
