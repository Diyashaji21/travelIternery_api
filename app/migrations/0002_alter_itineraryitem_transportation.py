# Generated by Django 4.2.5 on 2024-04-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraryitem',
            name='transportation',
            field=models.CharField(choices=[('car', 'Car'), ('bus', 'Bus'), ('train', 'Train'), ('flight', 'Flight')], max_length=100),
        ),
    ]
