import time
from random import randrange
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys #für z.B. die Enter Taste

#browser = webdriver.Chrome('chromedriver.exe')
#browser.get('https://www.instagram.com/')

class InstaBot:
    def __init__(self, driver_path, username, password):
        self.browser = webdriver.Chrome(driver_path)
        self.username = username
        self.password = password
    
    def accept_cookies(self):
        accept_button = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        accept_button.click()
        time.sleep(randrange(1,4))

    def open(self):
        self.browser.get('https://www.instagram.com/')
        time.sleep(randrange(10,15))
        self.accept_cookies()

    def login(self):
        username_field = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        username_field.send_keys(self.username)
        time.sleep(randrange(1,3))
        password_field = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password_field.send_keys(self.password)
        password_field.submit()
        time.sleep(randrange(4,6))

    def search(self, hashtag):
        """
        # Funktioniert aktuell nicht, sollte es aber. Alternative über URL wird benutzt.
        search_field = self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_field.click()
        search_field.send_keys(hashtag)
        search_field.send_keys(Keys.RETURN)
        time.sleep(randrange(1,3))
        search_field.send_keys(Keys.RETURN)
        time.sleep(randrange(1,3))
        """
        self.browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(randrange(1,4))

    def like(self, count):
        first_pic = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        first_pic.click()
        time.sleep(randrange(1,4))
        for i in range(0, count):
            like_button = self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]')
            like_button.click()
            time.sleep(randrange(1,4))

            arrow_button = self.browser.find_element_by_class_name("coreSpriteRightPaginationArrow")                                                    
            arrow_button.click()
            time.sleep(randrange(1,5))
