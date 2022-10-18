# Generated by Django 4.1 on 2022-10-01 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0010_remove_shop_drone_type"),
        ("drones", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="drone",
            name="shop",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="shop",
                to="shops.shop",
            ),
        ),
    ]
