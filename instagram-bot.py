from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen

email = input("\nWhat is your Instagram email adress? ")
email.strip()
password = input("\nWhat is your Instagram password? ")
password.strip()
hashtag = input("\nWhich subject should the posts you like have? ")
hashtag.replace(" ", "")

class InstagramBot:

    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        email = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys(self.email)
        time.sleep(0.25)
        password.send_keys(self.password)
        time.sleep(0.25)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def search(self, hashtag):
        bot = self.bot
        pop = 1
        while pop >= 1:
            notifications = bot.find_element_by_class_name("HoLwm ")
            notifications.click()
            pop = 0
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
            time.sleep(3)
        print(links)
        for link in links:
            bot.get(link)
            time.sleep(2)
            likeButton = bot.find_element_by_class_name("u-__7")
            likeButton.click()
            time.sleep(4)

start = InstagramBot(email, password)
start.login()
start.search(hashtag)
start.likePosts()