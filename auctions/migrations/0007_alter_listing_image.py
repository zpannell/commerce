# Generated by Django 4.2.10 on 2024-02-14 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0006_alter_bid_bid_alter_listing_currentbid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image",
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
