# Generated by Django 5.2.3 on 2025-06-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
