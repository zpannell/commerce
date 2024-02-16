from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting/", views.newlisting, name="newlisting"),
    path("listings/<str:listing_id>/", views.listings, name="listings"),
    path("close/<str:listing_id>/", views.close, name="close"),
    path("comment/<str:listing_id>/", views.comment, name="comment"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("addwatchlist/", views.addwatchlist, name="addwatchlist"),
    path("removewatchlist/", views.removewatchlist, name="removewatchlist"),
    path("closed/", views.closed, name="closed"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category>", views.singlecategory, name="singlecategory"),
]
