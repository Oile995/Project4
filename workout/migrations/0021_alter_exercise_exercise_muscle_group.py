# Generated by Django 3.2.19 on 2023-06-28 17:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0020_alter_exercise_exercise_muscle_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_muscle_group',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
