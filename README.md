# CryptoX

Binance-inspired demo exchange built with Django templates and static assets.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000 to view the Markets page.

## Pages

- `/` Markets overview
- `/trade/` Spot trading view
- `/wallet/` Portfolio overview
- `/api/markets/` JSON market snapshot
