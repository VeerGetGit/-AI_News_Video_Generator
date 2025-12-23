# scraped_news.py
import requests
from bs4 import BeautifulSoup

def scrape_google_top_news(num_articles=5):
    url = "https://news.google.com/rss"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml-xml")  
    items = soup.find_all("item", limit=num_articles)

    articles = []
    for item in items:
        title = item.title.text.strip()
        link = item.link.text.strip()
        source = item.source.text.strip() if item.source else ""
       
        summary = item.description.text.strip() if item.description else ""
        articles.append({
            "title": title,
            "link": link,
            "source": source,
            "summary": summary  
        })
    return articles
