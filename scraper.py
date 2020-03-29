from bs4 import BeautifulSoup
from selenium import webdriver
import time
from firebase import firebase
import json


with open('E:\Project_Files\outer_city\python_stuff\worldo-meter-scraper\serviceAccountKey.json') as f:
  data = json.load(f)
  
url = data["url"]
Database_link = data["Database_link"]
put_link = data["put_link"]


profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
driver.set_window_position(1500, -110)
driver.get(url)
firebase = firebase.FirebaseApplication(Database_link, None)

x = ''

def updates():
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    listed = []
    text_list = ['Total_Cases', 'Deaths', 'Recovered']
    i = 0
   
    for my_tag in soup.find_all(class_="maincounter-number"):
        listed.append(my_tag.text.strip())
    while i < len(text_list):
        result = firebase.put(put_link, "'{}'".format(text_list[i]), listed[i])
        i += 1


def Start():
    updates()

# while True:
#     Start()

for i in range(2):       #for 24hrs range = 48
    print("update")
    time.sleep(10)    #60s*30 = 30mins = 1800
    Start()

driver.close()


