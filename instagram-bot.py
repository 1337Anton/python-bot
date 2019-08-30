from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from bs4 import BeautifulSoup as bs
import time
from urllib.request import urlopen
import re
from validate_email import validate_email

def split_str(s):
  return [ch for ch in s]

email_good = False
password_good = False
hashtag_good = False

good_chars_email = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-", "_", "@"]

print("\n")
print(" .___                __                                              __________        __    ")
print(" |   | ____   ______/  |______    ________________    _____          \______   \ _____/  |_  ")
print(" |   |/    \ /  ___|   __\__  \  / ___\_  __ \__  \  /     \   ______ |    |  _//  _ \   __\ ")
print(" |   |   |  \\___ \ |  |  / __ \/ /_/  >  | \// __ \|  Y Y  \ /_____/ |    |   (  <_> )  |   ")
print(" |___|___|  /____  >|__| (____  |___  /|__|  (____  /__|_|  /         |______  /\____/|__|   ")
print("         \/     \/           \/_____/            \/      \/                 \/               ")
print("\n")
print("With the Instagram Bot you can like alot of posts including a specific hashtag.")
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
    password = input("What is your Instagram password? ")
    password.strip()
    if len(password) <=8:
        password_good = False
        print("\n")
        print("This isn't a valid Instagram password.")
        print("\n")
    else:
        password_good = True

while hashtag_good == False:
    hashtag = input("Posts containing which hashtag do you want to like? \n")
    hashtag.replace(" ", "")
    hashtag.replace("#", "")
    hashtag_good = True

class InstagramBot:

    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        email = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys(self.email)
        time.sleep(0.25)
        password.send_keys(self.password)
        time.sleep(0.25)
        password.send_keys(Keys.RETURN)

    def search(self, hashtag):
        bot = self.bot
        try:
            notifications = WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm ")))
        finally:
            notifications = bot.find_element_by_class_name("HoLwm ")
            notifications.click()
        time.sleep(4)
        bot.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

    def likePosts(self):
        bot = self.bot
        links=[]
        for i in range(1,2):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            source = bot.page_source
            data=bs(source, 'html.parser')
            body = data.find('body')
            script = body.find('span')
            for link in script.findAll('a'):
                if re.match("/p", link.get('href')):
                    links.append('https://www.instagram.com'+link.get('href'))

        print("\n")
        print(links)
        print("\n")
        len(links)

        for link in links:
            bot.get(link)
            time.sleep(2)
            like_button = bot.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9")
            like_button.click()
            time.sleep(2)
            # comment_button = bot.find_element_by_name("X7cDz")
            # comment_button.click()
            # time.sleep(1)
            # comment_button.send_keys("Nice picture!")
            # comment_button.send_keys(Keys.RETURN)
            # time.sleep(2)
            source = bot.page_source
            data=bs(source, 'html.parser')
            body = data.find('body')
            comment_button = data.find("textarea")
            # comment_button.send_keys("Nice picture!")
            # comment_button.send_keys(Keys.RETURN)



start = InstagramBot(email, password)
start.login()
start.search(hashtag)
start.likePosts()