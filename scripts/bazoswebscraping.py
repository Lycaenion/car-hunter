from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import selenium

driver = webdriver.Chrome()

driver.get("https://auto.bazos.sk/ford/?hledat=galaxy&rubriky=auto&hlokalita=97411&humkreis=300&cenaod=&cenado=&order=&crp=&kitx=ano")


ads = driver.find_elements(By.CSS_SELECTOR, 'div.inzeraty.inzeratyflex')

for ad in ads:

    link = ad.find_element(By.CLASS_NAME, 'inzeratynadpis').find_element(By.TAG_NAME, 'a').get_attribute("href")
    price = ad.find_element(By.CLASS_NAME, "inzeratycena").find_element(By.TAG_NAME, "b").text
    description = ad.find_element(By.CLASS_NAME, "popis").text

    print(f'{link} {price} {description}')
