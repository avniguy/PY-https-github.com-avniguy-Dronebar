# Generated by Django 4.1 on 2022-09-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderrow", old_name="row_price", new_name="item_price",
        ),
        migrations.RenameField(
            model_name="orderrow", old_name="row_weight", new_name="item_weight",
        ),
    ]