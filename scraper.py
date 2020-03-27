from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'worldometer.com/corona'

profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
driver.set_window_position(1500, -110)
driver.get(url)

time.sleep(10)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

for tag in soup.find('div', {"class" : "maincounter-number"}):
    print(tag.text)



driver.close()