# Generated by Django 5.1 on 2024-08-19 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='stories.story'),
        ),
    ]
