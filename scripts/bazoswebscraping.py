from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import selenium
import re
import db
import emailsender

def find_cars():

    link_list = []
    email_body = ""
    driver = webdriver.Chrome()

    driver.get(
        "https://auto.bazos.sk/ford/?hledat=galaxy&rubriky=auto&hlokalita=97411&humkreis=300&cenaod=&cenado=&order=&crp=&kitx=ano")

    ads = driver.find_elements(By.CSS_SELECTOR, 'div.inzeraty.inzeratyflex')
    YEAR_PATTERN = re.compile(r'(?sm).*?(?P<year>\b20[12]\d\b)')

    for ad in ads:

        link = ad.find_element(By.CLASS_NAME, 'inzeratynadpis').find_element(By.TAG_NAME, 'a').get_attribute("href")
        print("Link " + link)

        if db.is_ad_in_db(link) is False:
                print("The ad is not in the db")
                price = ad.find_element(By.CLASS_NAME, "inzeratycena").find_element(By.TAG_NAME, "b").text
                if re.search('[a-zA-z]', price) is not None:
                    print("Not a float")
                else:
                    converted_price = float(price.replace(" ", "").strip('€'))
                    print(f'the price is {price}')
                    title = ad.find_element(By.CLASS_NAME, 'inzeratynadpis').find_element(By.CLASS_NAME, "nadpis").text
                    ad.find_element(By.LINK_TEXT, title).click()
                    long_description = driver.find_element(By.CLASS_NAME, "popisdetail").text
                    driver.back()
                    match = YEAR_PATTERN.match(long_description)
                    if match:
                        year = match.group('year')
                        #print(f'title {title} year {year} link {link} price {price} long description {long_description}')
                        db.add_ad_to_db(link, converted_price)
                        link_list.append(link)

        else:
            print("ad already in db")

        """Values for later implementation"""


        #Give the program time to reload all the elements before starting the next one
        time.sleep(2)

    if len(link_list) == 0:
        email_body = "No new ads to view"
    else:
        for link in link_list:
            email_body = email_body + link + '\n'

    emailsender.sendemail(email_body)










if __name__ == "__main__":
    find_cars()