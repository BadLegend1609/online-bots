from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class WpBot:
    ################################################################# INITIALIZING THE BOT ###########################################
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
        sleep(15)
    def spam(self,contact):
        self.driver.find_element_by_xpath('//span[@title="{}"]'.format(contact)).click()
        a = True
        count = 0
        while a:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(".")
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
            print(count)
            count += 1
            
bot = WpBot()
name = "Kundu Bro ❤️" #replace it with the name of your contact
bot.spam(name)
        
        
        