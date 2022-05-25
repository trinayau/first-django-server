from django.urls import path
from . import views

# makes a url that gives it a view
urlpatterns = [
    path("", views.index, name="livestock-index"),
    path("about/", views.about, name="livestock-about"),
    path("all/", views.all, name="livestock-all"),
    path("shop/", views.shop, name="livestock-shop"),
    path("cows/", views.cows, name="livestock-cows"),
    path("cows/<int:id>", views.cow, name="livestock-cow")
]