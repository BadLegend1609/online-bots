from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from credentials import discord_username, discord_password




password = discord_username
username = discord_password

class DiscordBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.driver.get('https://discord.gg')
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/header[2]/nav/div[2]/a").click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]").click()
        sleep(10)
    def spam(self):
        sleep(10)
        script = """
            document.querySelectorAll('a[aria-label="Cockroach Cumstain"')[0].click()
        """
        self.driver.execute_script(script)
        sleep(3)
        a = 0
        counter = 0
        
        while a == 0 :
            
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div").send_keys("@here Binod \n Binod")
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div/div").send_keys(Keys.ENTER)
            sleep(2.5)
            print(counter)
            counter += 1
        

my_bot = DiscordBot(username, password)
my_bot.spam()