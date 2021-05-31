from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import numpy as np

search_dict = {"Product Name": [], "Price": [], "Discounted Price": []};


def amazon_search(query):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get("https://www.amazon.com/")
    search_box = driver.find_element_by_id('twotabsearchtextbox')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    sleep(5)
    dup_check = ""
    result = driver.find_elements_by_xpath('//*[@class="sg-col-inner"]')

    for item in result[3:]:
        try:
            # checks the search result output
            try:
                title = item.find_element_by_xpath('.//span[contains(@class, "a-size-medium a-color-base a-text-normal")]').get_attribute('innerText')
            except:
                title = item.find_element_by_xpath('.//span[contains(@class, "a-size-base-plus a-color-base a-text-normal")]').get_attribute('innerText')

            # checks for duplicates
            if title == dup_check:
                print('')
            else:
                # Adds Product Name
                print(title)
                search_dict.setdefault("Product Name", []).append(title)

                try:
                    # Adds Original Price
                    o_price = item.find_element_by_xpath('.//span[@class="a-price a-text-price"]//span[@class="a-offscreen"]').get_attribute('innerText')
                    print(o_price)
                    search_dict.setdefault("Price", []).append(o_price)
                except:
                    print('No discount')
                    search_dict.setdefault("Price", []).append("No discount")
                try:
                    # Adds Current Price
                    c_price = item.find_element_by_xpath('.//span[@class="a-offscreen"]').get_attribute('innerText')
                    print(c_price)
                    search_dict.setdefault("Discounted Price", []).append(c_price)
                except:
                    print('Product on exclusive pricing')
                    search_dict.setdefault("Discounted Price", []).append("Product on exclusive pricing")


            # location = item.find_element_by_xpath('.//span[@class="c2i43- "]').get_attribute('innerText')
            # link = item.find_element_by_xpath('.//*[@class="c16H9d"]//a[contains(@age, "0")]').get_attribute('innerHTML')
            # title = item.find_element_by_xpath('.//*[@class="s-main-slot s-result-list s-search-results sg-row"]//data-asin//class//span//span//class//[contains(@class, "a-size-base-plus a-color-base a-text-normal")]').get_attribute('innerText')
            # print(location)
            # print(link)
            print('')
            dup_check = title
        except:
            print('')
