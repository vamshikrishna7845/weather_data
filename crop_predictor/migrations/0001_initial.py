# Generated by Django 4.1 on 2022-08-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WeatherData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(unique=True)),
                ("max_temp", models.IntegerField()),
                ("min_temp", models.IntegerField()),
                ("precipitation", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="YieldData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField(unique=True)),
                ("qty_harvested", models.IntegerField()),
            ],
        ),
    ]