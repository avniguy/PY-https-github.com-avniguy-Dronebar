# Generated by Django 4.1 on 2022-09-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0007_remove_orderdetails_item"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderRow",
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
            ],
        ),
        migrations.RenameField(
            model_name="order", old_name="total", new_name="total_price",
        ),
        migrations.DeleteModel(name="OrderDetails",),
    ]
