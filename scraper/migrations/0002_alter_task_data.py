# Generated by Django 5.0.6 on 2024-06-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
