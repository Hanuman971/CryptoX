# CryptoX

A local Django demo that mimics a Binance-style exchange landing page and APIs.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000>.

## API endpoints

- `GET /api/markets/` – market list
- `GET /api/tickers/` – simplified ticker data
- `GET /api/orderbook/?symbol=BTCUSDT` – static order book
