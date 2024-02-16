from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from decimal import Decimal

from .models import User, Listing, Bid, Comment#, Watchlist


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(status="open"),
        "status": "Active"
    })


def closed(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(status="closed"),
        "status": "Closed"
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def newlisting(request):
    categories = sorted([c[0] for c in Listing.category.field.choices])
    if request.method == "POST":
        l = Listing()
        l.title = request.POST["title"]
        l.description = request.POST["description"]
        l.startingbid = request.POST["startingbid"]
        l.currentbid = None
        l.image = request.POST["imageurl"]
        l.category = request.POST["category"]
        l.createdby = request.POST["createdby"]
        l.save()
        return render(request, "auctions/newlisting.html", {
            "categories": categories
        })
    else:
        return render(request, "auctions/newlisting.html", {
            "categories": categories
        })
    
def listings(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    b = Bid()
    bids = Bid.objects.filter(item=listing_id).count()
    comments = Comment.objects.filter(item=listing_id)
    if request.method == "POST":
        if request.user.is_authenticated:
            b.item = listing
            b.bid = request.POST["bid"]
            b.bid = Decimal(b.bid)
            b.bidby = request.user.username
            if listing.currentbid == None:
                if b.bid >= listing.startingbid:
                    listing.currentbid = b.bid
                    listing.highestbidder = request.user.username
                else:
                    return render(request, "auctions/listing.html", {
                        "listing": listing,
                        "message": "Invalid bid. Bid must be equal or greater than starting bid.",
                        "comment": comments
                    })
            else:
                if b.bid > listing.currentbid:
                    listing.currentbid = b.bid
                    listing.highestbidder = request.user.username
                else:
                    return render(request, "auctions/listing.html", {
                        "listing": listing,
                        "message": "Invalid bid. Bid must be greater than current bid.",
                        "comment": comments
                    })
            b.save()
            listing.save()
            bids = Bid.objects.filter(item=listing_id).count()
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "bids": bids,
                "comment": comments
            })
        else:
            return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "bids": bids,
            "comment": comments
        })
    

def close(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        if request.user.username == listing.createdby:
            listing.status = "closed"
            listing.save()
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "message": "This listing is now closed."
            })
        else:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "message": "You must be the creator of the listing in order to close it."
            })
    else:
        return HttpResponseRedirect(reverse("listings", kwargs = {"listing_id": listing_id}))
    

def comment(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    c = Comment()
    if request.method == "POST":
        if request.user.is_authenticated:
            c.item = listing
            c.commenttext = request.POST["comment"]
            c.commentby = request.user.username
            c.save()
        return HttpResponseRedirect(reverse("listings", kwargs = {"listing_id": listing_id}))
    else:
        return HttpResponseRedirect(reverse("listings", kwargs = {"listing_id": listing_id}))
    

def watchlist(request):
    return render(request, "auctions/index.html", {
        "listings": request.user.watchlist.all(),
        "status": "Watchlist"
    })


def addwatchlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            listing_id = request.POST["watchlist"]
            listing = Listing.objects.get(id=listing_id)
            request.user.watchlist.add(listing)
            request.user.save()
        return HttpResponseRedirect(reverse("listings", kwargs = {"listing_id": listing_id}))
    else:
        return render(request, "auctions/index.html", {
            "listings": request.user.watchlist.all()
        })


def removewatchlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            listing_id = request.POST["watchlist"]
            listing = Listing.objects.get(id=listing_id)
            request.user.watchlist.remove(listing)
            request.user.save()
        return HttpResponseRedirect(reverse("listings", kwargs = {"listing_id": listing_id}))
    else:
        return render(request, "auctions/index.html", {
            "listings": request.user.watchlist.all()
        })
    

def categories(request):
    categories = sorted([c[0] for c in Listing.category.field.choices])
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

def singlecategory(request, category):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(category=category, status="open"),
        "status": category
    })