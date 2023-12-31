from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

class twitterBot:
    def __init__(self, username, password):
        self.username = "cappabarra"
        self.password = "edmundye342587797"
        self.bot = driver

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/i/flow/login')
        wait = WebDriverWait(bot, 10)

        try:
            username = wait.until(EC.visibility_of_element_located((By.NAME, 'text')))
        except:
            username = wait.until(EC.visibility_of_element_located((By.NAME, 'text')))

        username.send_keys(self.username)

        next_button = bot.find_elements(By.XPATH, '//div[@role="button"]')
        next_button[-2].click()
        try:
            password = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        except:
            password = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def likeAndReply(self):
        bot = self.bot
        bot.get("https://twitter.com/nikisundefined")
        wait = WebDriverWait(bot, 10)

        try:
            niks_tweet = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="tweet"]')))
            like_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="like"]')))
            like_button.click()
        except:
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            like_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="like"]')))
            like_button.click()
        
        time.sleep(1)
        bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        

bot = twitterBot('cappabarra', 'edmundye342587797')
bot.login()
bot.likeAndReply()