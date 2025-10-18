import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
import os

# ==============================
# 🔒 Email setup
# ==============================
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
TO_EMAIL = "garbanda26@gmail.com"  # Your email

# ==============================
# 📰 Scraper function
# ==============================
def scrape_headlines():
    url = "https://www.bbc.com/sport/football"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = [h.text.strip() for h in soup.find_all("h3")][:10]

    # Save headlines to file
    with open("news.txt", "w") as f:
        for h in headlines:
            f.write(h + "\n")

    print("✅ Headlines saved to news.txt")
    return "\n".join(headlines)

# ==============================
# 📧 Email sender
# ==============================
def send_email(message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = "⚽ Football Headlines Update"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = TO_EMAIL

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Email failed:", e)

# ==============================
# 🔁 Main loop
# ==============================
def main():
    while True:
        headlines_text = scrape_headlines()
        send_email(headlines_text)
        print("⏳ Waiting 1 hour before next update...\n")
        time.sleep(3600)  # Wait 1 hour

if __name__ == "__main__":
    main()
