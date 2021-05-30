from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import numpy as np


def amazon_search(query):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    search_box = driver.find_element_by_id('twotabsearchtextbox')
    search_box.send_keys(query)
    # search_box.send_keys('drone')
    search_box.send_keys(Keys.ENTER)
    sleep(5)

    result = driver.find_elements_by_xpath('//*[@class="sg-col-inner"]')
    # print(result)
    for item in result:
        try:
            title = item.find_element_by_xpath('.//span[contains(@class, "a-size-base-plus a-color-base a-text-normal")]').get_attribute('innerText')
            # price = item.find_element_by_xpath('.//span[@class="c13VH6"]').get_attribute('innerText')
            # location = item.find_element_by_xpath('.//span[@class="c2i43- "]').get_attribute('innerText')
            #link = item.find_element_by_xpath('.//*[@class="c16H9d"]//a[contains(@age, "0")]').get_attribute('innerHTML')
            # title = item.find_element_by_xpath('.//*[@class="s-main-slot s-result-list s-search-results sg-row"]//data-asin//class//span//span//class//[contains(@class, "a-size-base-plus a-color-base a-text-normal")]').get_attribute('innerText')
            print(title)
            # print(price)
            # print(location)
            #print(link)
            print('')

        except:
            print('error')
