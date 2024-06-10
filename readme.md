<!-- create readme.md for 

PYTHON ASSIGNMENT

Here’s a short and simple assignment to be completed before you join us!
The assignment goal is to basically make a script to scrape some data from a website exposed as a django rest framework API


The websites assigned to you is:
 
https://coinmarketcap.com/


Write a django rest framework API which will take in a list of crypto coin acronyms, scrape the data from the website and return back the JSON response.

Libraries to use:
djangorestframework
celery
requests
selenium





For this example URL: https://coinmarketcap.com/currencies/duko/ scrape the following details:






























There will be 2 APIs in django rest:
/api/taskmanager/start_scraping [POST]-  this will take in a list payload [“DUKO”, “NOT”, “GORILLA”] which are names of the crypto coins and submit a scraping job(celery will be used) to be run for these coins parallely and return back a job id
/api/taskmanager/scraping_status/<job_id> [GET] - From the job_id received in the previous API, we can query this API and it will return the currently scraped data for that job. Sample output:

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

You need to create a class CoinMarketCap in a file coinmarketcap.py under the django app folder with the functions for making requests, scraping data, processing data and sending back a JSON response(you can add any other function if needed). Submissions without proper OOPS concepts will not be preferred.

There should be 2 models to store the jobs and tasks (each task should have it’s scraped data stored as well)

The input to the APIs should be validated: If a payload like [1, “DUKO”, 3] is provided, the API should throw relevant response that scraping cannot be continued due to invalid input

Try to avoid XPATHs as far as possible during HTML parsing

Your APIs should be generalised ie, they should work with any input coins available on CoinMarketCap and scrape all the available data (all official, social links etc)


IMPORTANT DETAILS

DEADLINE: 	11:55 PM, 11th June, 2024 (Tuesday)

The assignment has to be submitted at:
	https://forms.gle/hBxJJ7LDwnUL2GzG6

NOTE: Early submission will give you an advantage.

Create a github repo, and add your code to it. In the readme add screenshots of the tables from the admin panel and postman screenshots for the API calls with responses that you have created.
Make sure the code is neat and readable.
For any doubts, feel free to drop a mail at devgods99@gmail.com 
In case you’re not able to complete within the deadline, do submit the code even if a part or it completely doesn’t work. Because the work you put in and skills you possess are reflected by your code. 


 -->


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


### Admin Panel


### Postman Screenshots

