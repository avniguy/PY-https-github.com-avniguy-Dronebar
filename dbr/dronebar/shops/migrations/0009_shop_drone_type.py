# Generated by Django 4.1 on 2022-09-21 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("drones", "0001_initial"),
        ("shops", "0008_delete_shop1"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="drone_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="shop_drone_type",
                to="drones.dronetype",
            ),
        ),
    ]
