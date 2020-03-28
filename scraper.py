from bs4 import BeautifulSoup
from selenium import webdriver
import time
from firebase import firebase


url = 'https://www.worldometers.info/coronavirus/'

profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
#driver.set_window_position(1500, -110)
driver.get(url)
firebase = firebase.FirebaseApplication("https://pythondb-bfd79.firebaseio.com/", None)

x = ''

def updates():
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    for tag in soup.find('div', {"class" : "maincounter-number"}):
        # print(tag)
        for child in tag.string:
            global x
            x = x + child.rstrip()
        # print(child)
        # print(x)
        # data = {
        # 'Name': 'adasd',
        # 'Email': 'adasdasd@jason.com',
        # 'Phone': 1234567890
        # }
        if x != "":
            
            result = firebase.put('/pythondb-bfd79/customer/-M3TXyKe-R9-Vkk4MsEI', 'Name', x)
            # print(result)

# for i in range(48):       #for 24hrs range = 48
#     Start()
#     time.sleep(1800)    #60s*30 = 30mins = 1800

def Start():
    updates()



Start()

driver.close()


