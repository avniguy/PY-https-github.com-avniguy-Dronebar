# Generated by Django 4.1 on 2022-09-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_order_total_price_order_total_weight"),
    ]

    operations = [
        migrations.AddField(
            model_name="order", name="lat_location", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="long_location",
            field=models.FloatField(default=0),
        ),
    ]