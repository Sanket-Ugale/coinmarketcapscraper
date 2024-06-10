# CoinMarketCap API

This is a Django Rest Framework API which will take in a list of crypto coin acronyms, scrape the data from the website and return back the JSON response.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
git clone https://github.com/Sanket-Ugale/coinmarketcapscraper.git
```

```bash
python -m venv venv
```

for ubuntu
```bash
source venv/bin/activate
```

for windows

```bash
venv\Scripts\activate
```

```bash
cd coinmarketcapscrape
```


```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver 
```

```bash
celery -A coinmarketcapscrape.celery worker --pool=solo -l info
```

## API Endpoints

### Start Scraping
```bash
POST /api/taskmanager/start_scraping
```

#### Request Body
```json
{
    "coins": ["DUKO", "NOT", "GORILLA"]
}
```

#### Response
```json
{
    "job_id": "<UUID>"
}
```

### Scraping Status
```bash

GET /api/taskmanager/scraping_status/<job_id>
```

#### Response
```json
{
  "job_id": "<UUID>",
  "tasks": [
    {
      "coin": "DUKO",
      "output": {
        "price": 0.003913,
        "price_change": -5.44,
        "market_cap": 37814377,
        "market_cap_rank": 740,
        "volume": 4583151,
        "volume_rank": 627,
        "volume_change": 12.21,
        "circulating_supply": 9663955990,
        "total_supply": 9999609598,
        "diluted_market_cap": 39127766,
        "contracts": [
          {
            "name": "solana",
            "address": "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
          }
        ],
        "official_links": [
          {
            "name": "website",
            "link": "https://dukocoin.com"
          }
        ],
        "socials": [
          {
            "name": "twitter",
            "url": "https://twitter.com/dukocoin"
          },
          {
            "name": "telegram",
            "url": "https://t.me/+jlScZmFrQ8g2MDg8"
          }
        ]
      }
    },
    {
     “coin”: “NOT”,
            “output”: {
            …
         }
    },
    {
     “coin”: “GORILLA”,
            “output”: {
            …
         }
    }
  ]
}
```


## Screenshots

1. Home route (/)
![image](https://github.com/Sanket-Ugale/coinmarketcapscraper/assets/121743571/323b6421-82ec-4bc9-a6c8-fc0429794fa5)

2. Get Data route(/api/taskmanager/scraping_status/<uuid:job_id>)
![image](https://github.com/Sanket-Ugale/coinmarketcapscraper/assets/121743571/b90ec43e-ca5f-4544-b9c2-efb1ade47675)




### Admin Panel

![image](https://github.com/Sanket-Ugale/coinmarketcapscraper/assets/121743571/06a40fe7-6f9e-401b-893c-47360aa24f84)

![image](https://github.com/Sanket-Ugale/coinmarketcapscraper/assets/121743571/e042feca-c593-41c5-970b-d54c1d5a5fd7)

![image](https://github.com/Sanket-Ugale/coinmarketcapscraper/assets/121743571/1fbf79d1-eddd-40a2-a3c9-82e78fcc44e8)


### Postman Screenshots
1. Start Scraping Route (/api/taskmanager/start_scraping)

![image](https://github.com/Sanket-Ugale/coinmarketcapscraper/assets/121743571/b06c55dd-bbfc-415c-8306-b67ac2c925ac)



2. Get Jobs (/api/taskmanager/scraping_status/<uuid:job_id>)

![image](https://github.com/Sanket-Ugale/coinmarketcapscraper/assets/121743571/0a99c408-a55e-4636-9822-d5894f7a696d)





