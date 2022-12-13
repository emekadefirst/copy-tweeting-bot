import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "emekadefirst@gmail.com"
password = "Password2021$."

# LOGIN
url = "https://twitter.com/i/flow/login"
driver = webdriver.Chrome("chromedriver")
driver.get(url)
time.sleep(15)

# USERNAME
username_field = driver.find_element(By.CLASS_NAME, "r-homxoj")
username_field.send_keys(username)
time.sleep(3)
username_field.send_keys(Keys.RETURN)
time.sleep(15)

# PASSWORD
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
time.sleep(3)
password_field.send_keys(Keys.RETURN)
time.sleep(20)

# TWEET
tweets_field = driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")
tweets_field.send_keys("")
time.sleep(10)
tweets_field.send_keys(Keys.CONTROL, Keys.ENTER)
time.sleep(10)
print("successful")


