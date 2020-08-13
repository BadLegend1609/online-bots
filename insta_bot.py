from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from credentials import insta_username, insta_password

class InstaBot:
    ################################################################# INITIALIZING THE BOT ###########################################
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.driver.get('https://instagram.com')
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//a[@href='/weakness_16/']").click()
        sleep(2)
        
    #########################Getting Followers And Following And Comparing And Unfollowing or Following Them############################
    def getFollwers(self):
        
        #######################Getting vectors of following and followers##########################################
        followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('innerHTML')
        following = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').get_attribute('innerHTML')
        print("You have: " + followers + " followers")
        print("You have: " + following + " following")
        
        ################################################Making Function Variables#######################################
        followers_list = []
        followers_list_raw = []
        following_list = []
        following_list_raw = []
        to_unfollow_list = []
        to_follow_list = []
        
        ##########################################Adding to followers list###########################################
        def followers_add():
            scroll = round(int(followers)/7)
            self.driver.find_element_by_xpath('//a[text()=" followers"]').click()
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[2]').click()
            
            script = """ 
                element = document.querySelector(".isgrP");
                element.scrollTo(0, element.scrollHeight);
            """
            for i in range(scroll):
                self.driver.execute_script(script)
                sleep(2)
            print("End scroll followers")
            
            followers_list_raw.append((self.driver.find_elements_by_class_name("enpQJ")))
            sleep(1)
            
            for i in followers_list_raw:
                for links in i:
                    name = links.get_attribute('innerText')
                    followers_list.append(name)
            sleep(1)        
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
            sleep(1)
            
                
            print(followers_list)
        
        
        ###########################################Adding to following list##################################
        def following_add():
            scroll = round(int(followers)/7)
            self.driver.find_element_by_xpath('//a[text()=" following"]').click()
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[2]').click()
            
            script = """ 
                element = document.querySelector(".isgrP");
                element.scrollTo(0, element.scrollHeight);
            """
            for i in range(scroll):
                self.driver.execute_script(script)
                sleep(2)
            print("End scroll following")
            
            following_list_raw.append((self.driver.find_elements_by_class_name("enpQJ")))
            sleep(1)
            
            for i in following_list_raw:
                for links in i:
                    name = links.get_attribute('innerText')
                    following_list.append(name)
           
            sleep(1)        
            self.driver.find_element_by_xpath('//html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
            sleep(1)
                
            print(following_list)
        
        
            
                        
        followers_add()
        following_add()
        # compare()
        
username, password = insta_username, insta_password      
bot = InstaBot(username, password)
bot.getFollwers()