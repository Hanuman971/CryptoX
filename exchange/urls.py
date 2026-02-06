from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("trade/", views.trade, name="trade"),
    path("wallet/", views.wallet, name="wallet"),
    path("api/markets/", views.api_markets, name="api_markets"),
]
