# Generated by Django 5.0.1 on 2024-02-16 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxiparty", "0009_taxiparty_time_alter_taxiparty_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taxiparty",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 2, 16, 7, 38, 49, 754643, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]