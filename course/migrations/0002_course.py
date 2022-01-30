# Generated by Django 3.2.9 on 2022-01-15 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_persion', models.CharField(max_length=30)),
                ('title_en', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='')),
                ('link', models.TextField()),
                ('video', models.FileField(upload_to='')),
                ('video_preview', models.FileField(blank=True, null=True, upload_to='')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='course.grade')),
            ],
        ),
    ]
