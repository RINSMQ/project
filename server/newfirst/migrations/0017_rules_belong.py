# Generated by Django 3.1.1 on 2020-10-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfirst', '0016_auto_20201031_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='rules',
            name='belong',
            field=models.TextField(default=''),
        ),
    ]
