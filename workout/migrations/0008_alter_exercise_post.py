# Generated by Django 3.2.19 on 2023-06-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0007_rename_content_exercise_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workout.post'),
        ),
    ]
