# Generated by Django 4.2.10 on 2024-02-14 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0018_alter_listing_currentbid_alter_listing_startingbid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image",
            field=models.URLField(blank=True, default=None, max_length=400, null=True),
        ),
    ]
