from bs4 import BeautifulSoup
from selenium import webdriver
import time
from firebase import firebase
import json

#Reading the JSON file
with open('E:\Project_Files\outer_city\python_stuff\worldo-meter-scraper\serviceAccountKey.json') as f:
  data = json.load(f)
  
url = data["url"]
Database_link = data["Database_link"]
put_link = data["put_link"]
x = ''

#Starting Selenium
profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
driver.set_window_position(1500, -110)
driver.get(url)
firebase = firebase.FirebaseApplication(Database_link, None)

#Updating Firebase Database
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

#Main Function Starts Seperate Which Will Be Useful If Adding Functions In The Future
def Start():
    updates()

#Running The Code Forever
# while True:
#     Start()

#Running The Code For A Specific Number Of times Or Specific Amount Of Time
for i in range(2):       #Number Of Times
    print("update")
    time.sleep(10)    #Time In Seconds 
    Start()

driver.close()


