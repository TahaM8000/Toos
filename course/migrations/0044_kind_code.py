# Generated by Django 3.2.8 on 2022-03-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0043_remove_grade_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='kind',
            name='code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
