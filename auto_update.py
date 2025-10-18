import time
import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.bbc.com/sport/football"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    headlines = soup.find_all("h3")

    with open("news.txt", "w", encoding="utf-8") as file:
        for h in headlines[:10]:
            headline = h.text.strip()
            file.write(headline + "\n")

    print("✅ Headlines updated and saved to news.txt")

# Repeat every hour (3600 seconds)
while True:
    scrape_headlines()
    print("⏳ Waiting for 1 hour before next update...\n")
    time.sleep(3600)
