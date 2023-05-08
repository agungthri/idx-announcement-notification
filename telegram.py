import requests
from dotenv import load_dotenv
import os

load_dotenv()

CHAT_ID = str(os.getenv("CHAT_ID"))
TOKEN = str(os.getenv("TOKEN"))

# telegram bot to send messege 
def send_message(msg):
    params = {"chat_id":CHAT_ID,"text":msg}
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.get(url, params=params, timeout=30)