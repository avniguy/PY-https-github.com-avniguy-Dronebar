# Generated by Django 4.1 on 2022-09-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_remove_order_total_price_remove_order_total_weight"),
    ]

    operations = [
        migrations.AddField(
            model_name="order", name="total_price", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="order", name="total_weight", field=models.FloatField(default=0),
        ),
    ]