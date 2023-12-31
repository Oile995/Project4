# Generated by Django 3.2.19 on 2023-06-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0021_alter_exercise_exercise_muscle_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='workout_done',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_completed',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
