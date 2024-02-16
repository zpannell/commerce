# Generated by Django 4.2.10 on 2024-02-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0016_remove_listing_test"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Sporting Goods", "Sporting Goods"),
                    ("Toys & Hobbies", "Toys & Hobbies"),
                    ("Home & Garden", "Home & Garden"),
                    ("Jewelry & Watches", "Jewelry & Watches"),
                    ("Health & Beauty", "Health & Beauty"),
                    ("Business & Industrial", "Business & Industrial"),
                    ("Pet Supplies", "Pet Supplies"),
                    ("Baby Essentials", "Baby Essentials"),
                    ("Electronics", "Electronics"),
                    ("Collectibles & Art", "Collectibles & Art"),
                    ("Books, Movies, & Music", "Books, Movies, & Music"),
                    ("Clothing", "Clothing"),
                ],
                default="",
                max_length=50,
                null=True,
            ),
        ),
    ]