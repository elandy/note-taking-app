# Generated by Django 5.0.3 on 2024-04-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
