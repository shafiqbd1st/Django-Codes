# Generated by Django 5.0.3 on 2024-03-24 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmusician',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]