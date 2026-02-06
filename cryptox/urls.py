"""CryptoX URL Configuration."""
from django.contrib import admin
from django.urls import path

from exchange import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("api/markets/", views.markets, name="markets"),
    path("api/tickers/", views.tickers, name="tickers"),
    path("api/orderbook/", views.orderbook, name="orderbook"),
]
