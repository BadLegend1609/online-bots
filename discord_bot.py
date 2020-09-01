from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import sys
from credentials import discord_username, discord_password
import random

username = discord_username
password = discord_password
replies = ['.', 'khub miss korchi', 'jani ghumaccho... but still', 'i love you', 'valo lagche na kichu', '<3', ':black_heart:']

class DiscordBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.driver.get('https://discord.gg')
        self.action = ActionChains(self.driver)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/header[2]/nav/div[2]/a").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]").click()
        print("Logged in as user")
        print('Replies are: ' + replies)
        sleep(10)
        
        
    def spam(self):
        sleep(20)
        script = """
            document.querySelectorAll('a[aria-label="aa"')[0].click()
        """
        self.driver.execute_script(script)
        sleep(3)
        a = 0
        counter = 0
        channels = self.driver.find_elements_by_xpath("//div[contains(@class, 'content-3at_AU')]")
        for channel in channels:
            text = channel.get_attribute('innerText')
            if text == 'new':
                channel.click()
                    
        while a == 0 :
            random.shuffle(replies)
            reply = random.choice(replies)
            replies.pop(reply)
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div").send_keys(reply)
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div/div").send_keys(Keys.ENTER)
            timerandomizer = random.randint(120, 1200)
            sleep((3600/2) + int(timerandomizer))
            print(counter)
            counter += 1
        
        
        
    def remake_channels(self):
        sleep(5)
        script = """
            document.querySelectorAll('a[aria-label="aa"')[0].click()
        """
        self.driver.execute_script(script)
        def delete_channel():
            channels = self.driver.find_elements_by_xpath("//div[contains(@class, 'content-3at_AU')]")
            for channel in channels:
                text = channel.get_attribute('innerText')
                if text == 'new':
                    self.action.context_click(on_element = channel)
                    self.action.perform()
                    self.driver.find_element_by_xpath("//div[contains(text(), 'Delete Channel')]").click()
                    sleep(1)
                    self.driver.find_element_by_xpath("//div[contains(text(), 'Delete Channel')]").click()
                    print("Deleted The Channel")

        def make_channel():
            script = """
            document.querySelectorAll('div[class="contents-18-Yxp"]')[1].click()
            """
            self.driver.execute_script(script)
            sleep(1)
            self.driver.find_element_by_xpath("//input[contains(@class, 'inputDefault-_djjkz input-cIJ7To')]").send_keys('new')
            self.driver.find_element_by_xpath("//div[contains(text(), 'Create Channel')]").click()
            print("Added The Channel!")
                
        delete_channel()
        make_channel()
                    
if __name__ == "__main__":
    my_bot = DiscordBot(username, password)
    my_bot.spam()
