# Generated by Django 3.2.8 on 2022-03-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_cover_giude_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeFromKonkur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('days', models.IntegerField()),
                ('code', models.IntegerField(unique=True)),
            ],
        ),
    ]
