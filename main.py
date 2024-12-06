from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shortenURL import generateShortenURL
from generateImage import generateRandomImage
import subprocess
import random

driver = webdriver.Chrome()

driver.get("https://edition.cnn.com/?refresh=1")

driver.maximize_window()#maximize
time.sleep(3)

print("Page Title: " + driver.title)

# find the article
article = driver.find_element(By.XPATH,"//div[@class = 'stack'][1]")
#find the link

linkToArticle = driver.find_element(By.XPATH,"//div[@class = 'stack'][1]//div[@class='stack__items ']//div[contains(@class,'container container_lead')]/div/a")

linkArt = linkToArticle.get_attribute("href")

titleofArticle = linkToArticle.get_attribute("data-zjs-container_name")
print(linkArt)
print(titleofArticle)

#Step 2: Generate a caption for the article
# div[@class = 'stack'][1] // div[@ class ='stack__items '] // div[contains(@class ,'container container_lead')] / div / a / h2
linkToArticle.click()
time.sleep(2)
print("Page Title: " + driver.title)

wait = WebDriverWait(driver, 30)
# wait.until(EC.visibility_of_element_located(By.XPATH,"//main[@class = 'article__main']/div[@class = 'article__content-container']/div[@class = 'article__content']//p[contains(@class,'vossi-paragraph')][1]"))
# try:
wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/section[3]/section[1]/article/div/section/div/p[1]")))
# finally:
#     driver.quit()

# articleParaforcaption = driver.find_element,By.XPATH("//main[@class = 'article__main']/div[@class = 'article__content-container']/div[@class = 'article__content']//p[contains(@class,'vossi-paragraph')][1]")
articleParaforcaption = driver.find_element(By.XPATH,"/html/body/div[2]/section[3]/section[1]/article/div/section/div/p[1]")
# driver.execute_script("arguments[0].scrollIntoView();", articleParaforcaption)

articleText = articleParaforcaption.text
print(articleText)

privateURL = 1
shortURL = generateShortenURL(linkArt, privateURL, None)
caption = articleText + "(" + shortURL + ")."
print(shortURL)
print(caption)

#STEP 3:GENERATE RANDOM IMAGE BASED ON ARTICLE TITLE
randomword = random.randrange(0,len(titleofArticle.split()),1)
print("random word picker => ", randomword)
keywordForImageGeneration = titleofArticle.split()[randomword]
print("key word => ", keywordForImageGeneration)
imageUrl = generateRandomImage(keywordForImageGeneration)
print(imageUrl)

#STEP 4: PUBLISH CONTENT



subprocess.call(["taskkill", "/F", "/IM", "ChromeDriver.exe"]) #kills all background process on test completion

driver.close()
driver.quit()