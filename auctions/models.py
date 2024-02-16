from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


CATEGORY_CHOICES = (
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
    ("Clothing", "Clothing")
)
# should the choices be in their own class. kinda says that in project description
class User(AbstractUser):
    watchlist = models.ManyToManyField("Listing", related_name="watchlist", blank=True)
    pass


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    startingbid = models.DecimalField(max_digits=10, decimal_places=2)
    currentbid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.URLField(max_length=400, default=None, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="", null=True, blank=True)
    createdby = models.CharField(max_length=50, default=None)
    createddate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default="open")
    highestbidder = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return (f"{self.id}: {self.title}")


class Bid(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None)
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    bidby = models.CharField(max_length=50, default=None)
    biddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.bid} was bid by {self.bidby} at {self.biddate}."


class Comment(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None)
    commenttext = models.CharField(max_length=2000, default=None)
    commentby = models.CharField(max_length=50, default=None)
    commentdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"{self.id}: {self.commenttext} was written by {self.commentby}"
                f" at {self.commentdate}.")