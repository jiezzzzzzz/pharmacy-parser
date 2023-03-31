from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

options = Options()
executable_path = os.path.join(os.getcwd(), 'chromedriver', 'chromedriver.exe')
driver = webdriver.Chrome(options=options, service=Service(executable_path=executable_path))


driver.get("https://www.rlsnet.ru/drugs/ukazatel/c0")
time.sleep(3)
links = []

links_scope = driver.find_elements(By.CSS_SELECTOR, 'a.link')

for one_link in links_scope:
    links.append(one_link.get_attribute('href'))

for link in links[2:]:
    try:
        driver.get(link)
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        opis_pole = soup.find_all('p', class_='OPIS_POLE')
        if len(opis_pole) >= 7:
            pob = opis_pole[7].text
            if len(pob) == 0:
                print("пусто")
            else:
                print(pob)
                element = driver.find_element(By.CSS_SELECTOR, 'a')
                driver.execute_script("arguments[0].click();", element)
                brutto = driver.find_element(By.CSS_SELECTOR, 'div:not([class]):nth-of-type(3)').text

                if len(brutto) == 0:
                    print('пусто')
                else:
                    print(brutto)
    except TimeoutException:
        print('new connection try')
        driver.get("https://www.rlsnet.ru/drugs/ukazatel/c0")
        time.sleep(5)
    #pob = driver.find_element(By.CSS_SELECTOR, 'div.OPIS_POLE p').text[12:]




