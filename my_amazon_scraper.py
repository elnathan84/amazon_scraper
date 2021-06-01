from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

search_dict = {"Product Name": [], "Discounted Price": [], "Previous Price": [], "Rating": [], "Shipping": [], "Stock": [], "Coupon": []};


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

    for item in result:
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

                # Adds Current Price
                try:

                    c_price = item.find_element_by_xpath('.//span[@class="a-offscreen"]').get_attribute('innerText')
                    print(c_price)
                    search_dict.setdefault("Discounted Price", []).append(c_price)
                except:
                    print('Product on exclusive pricing')
                    search_dict.setdefault("Discounted Price", []).append("Product on exclusive pricing")

                # Adds Original Price
                try:
                    o_price = item.find_element_by_xpath('.//span[@class="a-price a-text-price"]//span[@class="a-offscreen"]').get_attribute('innerText')
                    print(o_price)
                    search_dict.setdefault("Previous Price", []).append(o_price)
                except:
                    print('No discount')
                    try:
                        c_price = item.find_element_by_xpath('.//span[@class="a-offscreen"]').get_attribute('innerText')
                        search_dict.setdefault("Previous Price", []).append(c_price)
                    except:
                        search_dict.setdefault("Previous Price", []).append('Price Unavailable')

                # Rating
                try:
                    rating = item.find_element_by_xpath('.//span[@class="a-icon-alt"]').get_attribute('innerText')
                    print(rating)
                    search_dict.setdefault("Rating", []).append(rating)
                except:
                    print('No Rating')
                    search_dict.setdefault("Rating", []).append("No Rating")

                # Shipping
                try:
                    shipping = item.find_element_by_xpath('.//span[@class="a-size-small a-color-secondary"]').get_attribute('innerText')
                    print(shipping)
                    if 'Ships' in shipping:
                        search_dict.setdefault("Shipping", []).append(shipping)
                        loc_shipping = shipping
                    else:
                        search_dict.setdefault("Shipping", []).append(loc_shipping)
                except:
                    print('Shipping not Available')
                    search_dict.setdefault("Shipping", []).append('Shipping Unavailable')
                # Stock
                try:
                    stock = item.find_element_by_xpath('.//span[@class="a-size-small a-color-price"]').get_attribute('innerText')
                    print(stock)
                    search_dict.setdefault("Stock", []).append(stock)
                except:
                    print('In stock')
                    search_dict.setdefault("Stock", []).append('In stock')
                # Coupon
                try:
                    coupon = item.find_element_by_xpath('.//span[@class="a-size-base s-highlighted-text-padding aok-inline-block s-coupon-highlight-color"]').get_attribute('innerText')
                    print(coupon + ' with coupon')
                    search_dict.setdefault("Coupon", []).append(coupon + ' with coupon')
                except:
                    print('No coupon available')
                    search_dict.setdefault("Coupon", []).append('No coupon available')
                dup_check = title
            print('')

        except:
            print('error')
    # driver.close()
    # driver.quit()

def amazon_specific():
    None