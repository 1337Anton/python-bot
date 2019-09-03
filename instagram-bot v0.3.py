__author__ = "Anton Rave"
__copyright__ = "Copyright 2019, Anton Rave"
__credits__ = "Simo Edwin, also known as Dev Ed, https://www.youtube.com/channel/UClb90NQQcskPUGDIXsQEz5Q"
__license__ = "CC 3.0"
__version__ = "0.3"
__maintainer__ = "Anton Rave"
__email__ = "info@antonrave.de"
__status__ = "Production"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time
from urllib.request import urlopen
import re
from validate_email import validate_email
import ctypes
import getpass

ctypes.windll.kernel32.SetConsoleTitleW("Instagram-Bot v0.3")

class InstagramBot:

    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.comment = comment
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        try:
            email = WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        finally:
            email = bot.find_element_by_name("username")
            email.clear()
            email.send_keys(self.email)
        try:
            password = WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        finally:
            password = bot.find_element_by_name("password")
            password.clear()
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
        try:
           notifications = WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm")))
        finally:
            notifications = bot.find_element_by_class_name("HoLwm")
            notifications.click()

    def search_hashtag(self, hashtag):
        bot = self.bot
        try:
            search_bar = bot.find_element_by_class_name("wUAXj")
            search_bar.click()
            time.sleep(0.5)
            search = bot.find_element_by_class_name("x3qfX")
            search.send_keys(hashtag)
            time.sleep(1.25)
            search.send_keys(Keys.ENTER)
            time.sleep(1.25)
            search.send_keys(Keys.ENTER)
        except Exception:
            try:
                bot.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
            except Exception:
                print("Error!")
        time.sleep(2)

    def likePosts(self):
        bot = self.bot
        time.sleep(3)
        links=[]
        for amount in range(1, 2):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            source = bot.page_source
            data = bs(source, 'html.parser')
            body = data.find('body')
            script = body.find('span')
            for link in script.findAll('a'):
                if re.match("/p", link.get('href')):
                    links.append('https://www.instagram.com'+link.get('href'))

        print("\n")
        print("There are " + len(links) + "posts on this hashtag frontpage.")

        for link in links:
            bot.get(link)
            time.sleep(2)
            like_button = bot.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9")
            like_button.click()
            time.sleep(2)
            #comment = bot.find_element_by_class_name("X7cDz")
            #comment.send_keys(self.comment)
            #comment.send_keys(Keys.RETURN)
            #time.sleep(1)


email_good = False
password_good = False
hashtag_good = False

print("\n")
print(" .___                __                                              __________        __    ")
print(" |   | ____   ______/  |______    ________________    _____          \______   \ _____/  |_  ")
print(" |   |/    \ /  ___|   __\__  \  / ___\_  __ \__  \  /     \   ______ |    |  _//  _ \   __\ ")
print(" |   |   |  \\___ \ |  |  / __ \/ /_/  >  | \// __ \|  Y Y  \ /_____/ |    |   (  <_> )  |   ")
print(" |___|___|  /____  >|__| (____  |___  /|__|  (____  /__|_|  /         |______  /\____/|__|   ")
print("         \/     \/           \/_____/            \/      \/                 \/               ")
print("Version 0.3")
print("\n")
print("With the Instagram Bot you can like a lot of posts including a specific hashtag.")
print("\n")

while email_good == False:
    email = input("What is your Instagram email adress? ")
    is_valid = validate_email(email, verify=True)
    if is_valid == False:
        email_good = False
        print("\n")
        print("This isn't a valid E-Mail adress.")
        print("\n")
    else:
        email_good = True


while password_good == False:
    password = getpass.getpass("What is your Instagram Password? ")
    password.strip()
    if len(password) <=8:
        password_good = False
        print("\n")
        print("This isn't a valid Instagram password.")
        print("\n")
    else:
        password_good = True

while hashtag_good == False:
    hashtag = input("Posts containing which hashtag do you want to like? #")
    hashtag = hashtag.replace(" ", "")
    hashtag = hashtag.replace("#", "")
    hashtag = ("#" + hashtag)
    hashtag_good = True

comment = "Nice picture!"
start = InstagramBot(email, password)
start.login()
start.search_hashtag(hashtag)
start.likePosts()