# Generated by Django 3.2.5 on 2022-08-31 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0021_delete_menuitemprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
