from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import numpy as np

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/")
search_box = driver.find_element_by_id('twotabsearchtextbox')
search_box.send_keys('iphone11')
search_box.send_keys(Keys.ENTER)
sleep(5)
dup_check = ""
result = driver.find_elements_by_xpath('//*[@class="sg-col-inner"]')
# print(result)
for item in result[3:]:
    try:
        try:
            title = item.find_element_by_xpath('.//span[contains(@class, "a-size-medium a-color-base a-text-normal")]').get_attribute('innerText')
        except:
            title = item.find_element_by_xpath('.//span[contains(@class, "a-size-base-plus a-color-base a-text-normal")]').get_attribute('innerText')

        # print(title)
        if title == dup_check:
            print('')
        else:
            print(title)
            try:
                o_price = item.find_element_by_xpath('.//span[@class="a-price a-text-price"]//span[@class="a-offscreen"]').get_attribute('innerText')
                print(o_price)
            except:
                print('No discount')
            try:
                c_price = item.find_element_by_xpath('.//span[@class="a-offscreen"]').get_attribute('innerText')
                print(c_price)
            except:
                print('Product on exclusive pricing')


        # location = item.find_element_by_xpath('.//span[@class="c2i43- "]').get_attribute('innerText')
        #link = item.find_element_by_xpath('.//*[@class="c16H9d"]//a[contains(@age, "0")]').get_attribute('innerHTML')
        # title = item.find_element_by_xpath('.//*[@class="s-main-slot s-result-list s-search-results sg-row"]//data-asin//class//span//span//class//[contains(@class, "a-size-base-plus a-color-base a-text-normal")]').get_attribute('innerText')
        # print(location)
        # print(link)
        print('')
        dup_check = title
    except:
        print('error')