from __future__ import annotations

from django.http import JsonResponse
from django.shortcuts import render

from .data import get_market_pairs, get_order_book, get_recent_trades


def home(request):
    markets = get_market_pairs()
    context = {"markets": markets}
    return render(request, "home.html", context)


def trade(request):
    markets = get_market_pairs()
    order_book = get_order_book()
    recent_trades = get_recent_trades()
    context = {
        "markets": markets,
        "order_book": order_book,
        "recent_trades": recent_trades,
    }
    return render(request, "trade.html", context)


def wallet(request):
    balances = [
        {"asset": "USDT", "available": "12,450.00", "in_order": "1,200.00"},
        {"asset": "BTC", "available": "0.4821", "in_order": "0.1200"},
        {"asset": "ETH", "available": "4.950", "in_order": "0.600"},
    ]
    context = {"balances": balances}
    return render(request, "wallet.html", context)


def api_markets(request):
    markets = [
        {
            "symbol": market.symbol,
            "last_price": str(market.last_price),
            "change_pct": str(market.change_pct),
            "volume_24h": str(market.volume_24h),
        }
        for market in get_market_pairs()
    ]
    return JsonResponse({"markets": markets})
