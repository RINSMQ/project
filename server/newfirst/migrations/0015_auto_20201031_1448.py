# Generated by Django 3.1.1 on 2020-10-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfirst', '0014_auto_20201028_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='rules',
            name='name',
            field=models.TextField(default=''),
        ),
    ]