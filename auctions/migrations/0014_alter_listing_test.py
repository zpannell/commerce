# Generated by Django 4.2.10 on 2024-02-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0013_alter_listing_test"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="test",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
