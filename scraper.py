from bs4 import BeautifulSoup
from selenium import webdriver
import time
from firebase import firebase


url = 'https://www.worldometers.info/coronavirus/'

profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
driver.set_window_position(1500, -110)
driver.get(url)
firebase = firebase.FirebaseApplication("https://pythondb-bfd79.firebaseio.com/", None)

x = ''

def updates():
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    listed = []
    text_list = ['Total_Cases', 'Deaths', 'Recovered']
    i = 0

    # for meta in soup.find_all('div', {'class': 'maincounter-number'}):
    #     institution = meta.find_all()[2].text.strip()
    #     print(institution)  # or whatever you like to store it
   
    for my_tag in soup.find_all(class_="maincounter-number"):
        listed.append(my_tag.text.strip())
    # print(listed[1])
    while i < len(text_list):
        result = firebase.put('/pythondb-bfd79/customer/-M3TXyKe-R9-Vkk4MsEI', "'{}'".format(text_list[i]), listed[i])
        # E = "'{}'".format(text_list[i])
        # print(listed)
        i += 1

    # for tag in soup.find_all('div', {"class" : "maincounter-number"}):
    #     # print(tag)
    #     for child in tag.string:
    #         print(child)
        # for child in tag.string:
        #     global x
        #     x = x + child.rstrip()
        # if x != "":
        #     result = firebase.put('/pythondb-bfd79/customer/-M3TXyKe-R9-Vkk4MsEI', 'Recovered', x)
        #     print(result)


def Start():
    updates()

Start()

# for i in range(48):       #for 24hrs range = 48
#     Start()
#     time.sleep(1800)    #60s*30 = 30mins = 1800
driver.close()


