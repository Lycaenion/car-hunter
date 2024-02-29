from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import selenium
import re

driver = webdriver.Chrome()

driver.get("https://auto.bazos.sk/ford/?hledat=galaxy&rubriky=auto&hlokalita=97411&humkreis=300&cenaod=&cenado=&order=&crp=&kitx=ano")

ads = driver.find_elements(By.CSS_SELECTOR, 'div.inzeraty.inzeratyflex')
YEAR_PATTERN = re.compile(r'(?sm).*?(?P<year>\b20[12]\d\b)')


for ad in ads:

    link = ad.find_element(By.CLASS_NAME, 'inzeratynadpis').find_element(By.TAG_NAME, 'a').get_attribute("href")
    price = ad.find_element(By.CLASS_NAME, "inzeratycena").find_element(By.TAG_NAME, "b").text
    short_description = ad.find_element(By.CLASS_NAME, "popis").text
    title = ad.find_element(By.CLASS_NAME, 'inzeratynadpis').find_element(By.CLASS_NAME, "nadpis").text
    short_description = ad.find_element(By.CLASS_NAME, "popis").text

    ad.find_element(By.LINK_TEXT, title).click()

    long_description = driver.find_element(By.CLASS_NAME, "popisdetail").text

    driver.back()

    #Give the program time to reload all the elements before starting the next one
    time.sleep(2)

    match = YEAR_PATTERN.match(long_description)
    if match:
        year = match.group('year')
        print(f'title {title} year {year} link {link} price {price} long description {long_description}')
