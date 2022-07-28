import pandas as pd
import selenium
from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://in.pinterest.com"
driver.get(url)
driver.find_element(By.XPATH("/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[5]/div/div/div[1]/input")).get_attribute("innerHTML").sendKeys("Fashion in Trend for Women and Men");

btn = driver.find_element(By.XPATH("//input[@id='nav-search-submit-button']")).click()

images_fashion = []

elements = driver.find_element(By.XPATH("/html/body/div[1]/div[1]/div/div/div[2]/div/div/div[3]/div/div[1]/div/div/div[1]/div[14]/div/div/div/div/div/div[1]/div[1]/a/div/div[1]/div/div/div/div/div/img
"))
for i in elements:
    image = i.get_attribute('src')
    images_fashion.append(image)

for img in images_fashion:
    file_name = img.split('/')[-1]
    print(f"this is the file name:{file_name}")
    r = requests.get(img, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)
                
    else:
        print('')