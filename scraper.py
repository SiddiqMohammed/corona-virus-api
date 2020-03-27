from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://www.worldometers.info/coronavirus/'

profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
#driver.set_window_position(1500, -110)
driver.get(url)


def updates():
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    for tag in soup.find('div', {"class" : "maincounter-number"}):
        x = ""
        for child in tag.string:
            x = x + child
        print(x)

for i in range(48):       #for 24hrs range = 48
    Start()
    time.sleep(1800)    #60s*30 = 30mins = 1800

def Start():
    updates()

driver.close()