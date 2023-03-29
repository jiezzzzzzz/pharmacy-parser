from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


options = Options()
executable_path = os.path.join(os.getcwd(), 'chromedriver', 'chromedriver.exe')
driver = webdriver.Chrome(options=options, service=Service(executable_path=executable_path))


driver.get("https://www.rlsnet.ru/drugs/agapurin-40")
time.sleep(3)
pob = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div[1]/div[2]/div[3]/div[23]').text
print(pob)
xpath = '/html/body/div[1]/div[6]/div/div[1]/div[2]/div[3]/div[5]/a'
element = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].click();", element)


soup = BeautifulSoup(driver.page_source, 'html.parser')
brutto_name=soup.find(attrs={"class": {"structure-heading"}, 'id': {'formula'}}).text.strip()
print(brutto_name)
brutto = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div[2]/div[6]').text
print(brutto)
