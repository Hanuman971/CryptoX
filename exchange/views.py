from __future__ import annotations

from datetime import datetime, timezone

from django.http import JsonResponse
from django.shortcuts import render


MARKETS = [
    {
        "symbol": "BTCUSDT",
        "base": "BTC",
        "quote": "USDT",
        "price": 64250.12,
        "change": 2.14,
        "volume": 12890.45,
    },
    {
        "symbol": "ETHUSDT",
        "base": "ETH",
        "quote": "USDT",
        "price": 3502.77,
        "change": -1.02,
        "volume": 32990.21,
    },
    {
        "symbol": "SOLUSDT",
        "base": "SOL",
        "quote": "USDT",
        "price": 146.32,
        "change": 4.38,
        "volume": 81002.13,
    },
    {
        "symbol": "BNBUSDT",
        "base": "BNB",
        "quote": "USDT",
        "price": 581.09,
        "change": 0.48,
        "volume": 12900.07,
    },
]


def home(request):
    context = {
        "markets": MARKETS,
        "last_updated": datetime.now(timezone.utc),
    }
    return render(request, "index.html", context)


def markets(_request):
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "markets": MARKETS,
    }
    return JsonResponse(payload)


def tickers(_request):
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tickers": [
            {
                "symbol": market["symbol"],
                "last": market["price"],
                "change": market["change"],
                "volume": market["volume"],
            }
            for market in MARKETS
        ],
    }
    return JsonResponse(payload)


def orderbook(request):
    symbol = request.GET.get("symbol", "BTCUSDT")
    orderbook_payload = {
        "symbol": symbol,
        "bids": [
            {"price": 64240.2, "amount": 0.82},
            {"price": 64212.9, "amount": 1.43},
            {"price": 64190.1, "amount": 2.1},
        ],
        "asks": [
            {"price": 64260.8, "amount": 0.54},
            {"price": 64288.4, "amount": 1.12},
            {"price": 64310.7, "amount": 0.76},
        ],
    }
    return JsonResponse(orderbook_payload)
