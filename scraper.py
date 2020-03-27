<<<<<<< HEAD
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://www.worldometers.info/coronavirus/'

profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
#driver.set_window_position(1500, -110)
driver.get(url)

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

for tag in soup.find('div', {"class" : "maincounter-number"}):
    print(tag)

=======
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://www.worldometers.info/coronavirus/'

profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
#driver.set_window_position(1500, -110)
driver.get(url)

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

for tag in soup.find('div', {"class" : "maincounter-number"}):
    print(tag)

>>>>>>> cea3cc6fccb5162ab01501bc63a6987466286963
driver.close()