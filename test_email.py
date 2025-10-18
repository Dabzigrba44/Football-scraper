import os, smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise SystemExit("❌ ERROR: EMAIL_USER or EMAIL_PASS not set. Run 'source ~/.bashrc' first.")

msg = EmailMessage()
msg["Subject"] = "Test email from Termux"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg.set_content("This is a test email. If you received this, your setup works!")

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("✅ Test email sent successfully!")
except Exception as e:
    print("❌ Email failed:", e)
