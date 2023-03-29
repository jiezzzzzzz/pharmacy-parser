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

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.get("https://www.rlsnet.ru/drugs/ukazatel/c0")
time.sleep(3)
links = []

links_scope = driver.find_elements(By.CSS_SELECTOR, 'a.link')
for one_link in links_scope:
    links.append(one_link.get_attribute('href'))
for link in links[2:]:
    driver.get(link)

    pob = driver.find_element(By.CSS_SELECTOR, 'div > p.OPIS_POLE').text
    if len(pob) == 0:
        print("пусто")
    else:
        print(pob)
    xpath = '/html/body/div[1]/div[6]/div/div[1]/div[2]/div[3]/div[5]/a'
    element = driver.find_element(By.CSS_SELECTOR, 'a')
    driver.execute_script("arguments[0].click();", element)
    brutto = driver.find_element(By.CSS_SELECTOR, 'div:not([class]):nth-of-type(3)').text
    if len(brutto) == 0:
        print('пусто')
    else:
        print(brutto)

