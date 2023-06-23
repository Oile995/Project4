# Generated by Django 3.2.19 on 2023-06-23 12:04

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_auto_20230620_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='exercise_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='exercise_video',
        ),
        migrations.AddField(
            model_name='post',
            name='number_of_exercises',
            field=models.IntegerField(default=3),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('exercise_number', models.IntegerField()),
                ('content', models.TextField()),
                ('exercise_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('exercise_video', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='video')),
                ('workout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workout.post')),
            ],
            options={
                'ordering': ['exercise_number'],
            },
        ),
    ]
