# Generated by Django 3.2.19 on 2023-06-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0013_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='slug',
            field=models.SlugField(default='placeholder', unique=True),
        ),
    ]
