import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/sport/football"
response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")
headlines = soup.find_all("h3")

print("Latest Football Headlines:\n")

with open("news.txt", "w", encoding="utf-8") as file:
    for h in headlines[:10]:
        headline = h.text.strip()
        print("-", headline)
        file.write(headline + "\n")

print("\n✅ Headlines saved to news.txt successfully!")
