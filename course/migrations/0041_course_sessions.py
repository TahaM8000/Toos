# Generated by Django 3.2.8 on 2022-03-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0040_remove_course_sessions'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sessions',
            field=models.ManyToManyField(related_name='course', to='course.Session_coruse'),
        ),
    ]