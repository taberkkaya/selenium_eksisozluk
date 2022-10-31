from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
entryCount = 1
while pageCount <= 10:
    randomPage = random.randint(1,2354)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements(By.CSS_SELECTOR,".content")
    for element in elements:
        entries.append(element.text)
    #time.sleep(1)
    pageCount+=1

with open("entries.txt","w",encoding="utf-8") as f:
    for entry in entries:
        f.write(str(entryCount) + "-\n" + entry + "\n")
        entryCount+=1
    
browser.close()
