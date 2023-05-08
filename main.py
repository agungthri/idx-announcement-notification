from selenium import webdriver
from telegram import send_message
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import datetime
import winsound

PAGE_SIZE = 10
URL_BASE = f"https://www.idx.co.id/primary/NewsAnnouncement/GetAllAnnouncement?pageNumber=1&pageSize={PAGE_SIZE}&lang=id"

# selenium setup
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# container all information
CONTAINER = []

# looping forever to crave data 
while True:
  time.sleep(1)
  browser.get(URL_BASE)
  pre_tag = browser.find_element(by=By.TAG_NAME, value="body")
  try:
    data = json.loads(pre_tag.text)
    for i in data['Items']:
      info = f"{i['Code'][:4]} - {i['Title']}"
      # if there is new data, print, send and append it to container
      if (info not in CONTAINER):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"{now} - {info}")
        winsound.Beep(1000, 500)
        winsound.Beep(1000, 500)
        CONTAINER.append(info)
        if len(CONTAINER) > 8:
          send_message(f"{now} - {info}")
      else:
        continue
  except:
    print("Something Not Okay. Refreshing...")
    continue

