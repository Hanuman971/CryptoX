from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal


@dataclass(frozen=True)
class MarketPair:
    symbol: str
    last_price: Decimal
    change_pct: Decimal
    volume_24h: Decimal


@dataclass(frozen=True)
class OrderLevel:
    price: Decimal
    amount: Decimal


def get_market_pairs() -> list[MarketPair]:
    return [
        MarketPair("BTC/USDT", Decimal("65342.25"), Decimal("2.8"), Decimal("38250")),
        MarketPair("ETH/USDT", Decimal("3521.10"), Decimal("-1.2"), Decimal("129340")),
        MarketPair("SOL/USDT", Decimal("148.54"), Decimal("6.4"), Decimal("721045")),
        MarketPair("BNB/USDT", Decimal("592.88"), Decimal("0.8"), Decimal("45120")),
        MarketPair("XRP/USDT", Decimal("0.621"), Decimal("-0.4"), Decimal("910234")),
    ]


def get_order_book() -> dict[str, list[OrderLevel]]:
    bids = [
        OrderLevel(Decimal("65340.20"), Decimal("0.82")),
        OrderLevel(Decimal("65325.75"), Decimal("1.13")),
        OrderLevel(Decimal("65300.00"), Decimal("2.41")),
    ]
    asks = [
        OrderLevel(Decimal("65360.40"), Decimal("0.65")),
        OrderLevel(Decimal("65380.10"), Decimal("1.02")),
        OrderLevel(Decimal("65410.00"), Decimal("1.87")),
    ]
    return {"bids": bids, "asks": asks}


def get_recent_trades() -> list[dict[str, str]]:
    now = datetime.utcnow()
    trades = []
    for idx, price in enumerate(["65340.20", "65355.10", "65320.80", "65372.40"]):
        trades.append(
            {
                "price": price,
                "amount": str(Decimal("0.10") + Decimal(idx) / Decimal("10")),
                "side": "buy" if idx % 2 == 0 else "sell",
                "time": (now - timedelta(seconds=idx * 42)).strftime("%H:%M:%S"),
            }
        )
    return trades
