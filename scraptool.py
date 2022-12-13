import time 
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import pandas as pd  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://twitter.com/bod_republic")

state = ''
while state != "complete":
    print("loading not complete")
    time.sleep(randint(3, 5))
    state = driver.execute_script("return document.readyState")
time.sleep(10)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '[data-testid="tweet"]')))
except WebDriverException:
    print("Tweets did not appear!, Try setting headless=False to see what is happening")
        
tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
final_tweet = []
for tweet in tweets:
    tweet_text = tweet.find_element(By.CSS_SELECTOR,'div[data-testid="tweetText"]').text
    print(tweet_text)
    final_tweet.append(tweet_text)
    # my_dict = {'tweets': [tweet_text]}

df_tweets = pd.DataFrame({'tweet': final_tweet})
df_tweets.to_csv('scpr.csv')

