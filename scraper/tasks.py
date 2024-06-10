from bs4 import BeautifulSoup
from celery import Task
import requests
from coinmarketcapscrape.celery import app
from scraper.models import Job, Task

@app.task(bind=True, ignore_result=True)
def scrape_coin(self, job_id, coin):
    try:
        html_content = requests.get(f"https://coinmarketcap.com/currencies/{coin}/")
        soup = BeautifulSoup(html_content.content, 'html.parser')

        coin_name = soup.find('span', {'data-role': 'coin-name'}).text.strip()
        current_price = soup.find('span', {'class': 'sc-d1ede7e3-0 fsQm base-text'}).text.strip()
        market_cap = soup.find_all('dd', {'class': 'sc-d1ede7e3-0 hPHvUM base-text'})[0].text.strip()
        volume_24h = soup.find_all('dd', {'class': 'sc-d1ede7e3-0 hPHvUM base-text'})[1].text.strip()
        circulating_supply = soup.find_all('dd', {'class': 'sc-d1ede7e3-0 hPHvUM base-text'})[3].text.strip()
        total_supply = soup.find_all('dd', {'class': 'sc-d1ede7e3-0 hPHvUM base-text'})[4].text.strip()

        official_website_tag = soup.find('a', rel="nofollow noopener")
        official_website = official_website_tag['href'] if official_website_tag else None

        social_links_section = soup.find('div', {'data-role': 'stats-block'}, text='Socials')
        social_links = []
        if social_links_section:
            for link in social_links_section.find_next_all('a', rel='nofollow noopener'):
                platform_name = link.text.strip()
                platform_url = link['href']
                social_links.append({"name": platform_name, "url": platform_url})

        output = {
            "price": current_price,
            "market_cap": market_cap,
            "volume": volume_24h,
            "circulating_supply": circulating_supply,
            "total_supply": total_supply,
            "official_links": [{"name": "website", "link": official_website}],
            "socials": social_links
        }

        data= [
                {
                    "coin": coin_name,
                    "output": output
                }
            ]
        job = Job.objects.get(id=job_id)
        Task.objects.filter(job=job).update(data=data)
        return "❤️ Done!"
    except Exception as e:
        print(f"Error scraping coin {coin}: {e}")
        raise e
