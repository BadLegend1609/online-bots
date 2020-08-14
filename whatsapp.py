from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

##############################################Defining Global Functions######################################
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


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
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys("Test")
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
            print(count)
            count += 1
            sleep(100)
            
    def get_del_msg(self, contact):
        self.driver.find_element_by_xpath('//span[@title="{}"]'.format(contact)).click()
        a = True
        prev_list = []
        while a:
            new_list = self.driver.find_elements_by_xpath('//div[@class="_2hqOq _28DtS message-in focusable-list-item"]')
            if new_list != prev_list:
                msg_raw = new_list[-1].get_attribute('innerHTML')
                msg = cleanhtml(msg_raw)
                myfile = open('Messages.txt', 'a+')
                myfile.write(str(msg) + '\n')
                print('New message written')
                myfile.close()
                prev_list = new_list
            else:
                print("No New Messages")
    
    def test_get_text(self, contact):
        self.driver.find_element_by_xpath('//span[@title="{}"]'.format(contact)).click()
        msg = self.driver.find_element_by_xpath('//div[@class="_2hqOq _28DtS message-in focusable-list-item"]')
        msg_raw = msg.get_attribute('innerHTML')
        print(cleanhtml(msg_raw))


bot = WpBot()
# name = "20 20" #replace it with the name of your contact
# bot.get_del_msg(name)