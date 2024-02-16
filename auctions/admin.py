from django.contrib import admin
from .models import User, Listing, Bid, Comment

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "startingbid", "currentbid",
                    "category", "createdby", "createddate")
    
class BidAdmin(admin.ModelAdmin):
    list_display = ("item", "bid", "bidby", "biddate")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("item", "commentby", "commenttext", "commentdate")

# Register your models here.
admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
#admin.site.register(Watchlist)