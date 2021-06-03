from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

search_dict = {"Product Name": [], "Discounted Price": [], "Previous Price": [], "Rating": [], "Shipping": [], "Stock": [], "Coupon": []};
specific_dict = {"Product Name": [], "Rating": [], "Price": [], "Seller": [], "Availability": [], "Shipping": [], "Other Information":[]};
deals_dict = {"Product": [], "Price": [], "Time Left": [], "Number of Ratings":[], "Deal Type":[]};
picture = []


def amazon_search(query):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Remote(options=op)
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

def amazon_specific(url):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get(url)
    sleep(5)
    result = driver.find_elements_by_xpath('//*[@class="a-container"]')
    for item in result:
        try:
            # Product title
            title = item.find_element_by_xpath('.//span[contains(@class, "a-size-large product-title-word-break")]').get_attribute('innerText')
            specific_dict.setdefault("Product Name", []).append(title)
            print(title)

            # Rating
            try:
                rating = item.find_element_by_xpath('.//span[@class="a-icon-alt"]').get_attribute('innerText')
                print(rating)
                specific_dict.setdefault("Rating", []).append(rating)
            except:
                print('No Rating')
                specific_dict.setdefault("Rating", []).append('Rating not available')
            # Pricing
            try:
                price = item.find_element_by_xpath('.//span[@class="a-size-medium a-color-price"]').get_attribute('innerText')
                print(price)
                specific_dict.setdefault("Price", []).append(price)
            except:
                print('Price not available')
                specific_dict.setdefault("Price", []).append('Price not available')
            # Seller
            try:
                seller = item.find_element_by_xpath('.//a[@id="sellerProfileTriggerId"]').get_attribute('innerText')
                print("Sold by: " + seller)
                specific_dict.setdefault("Seller", []).append(seller)
            except:
                print('Seller data not available')
                specific_dict.setdefault("Seller", []).append('Seller data not available')
            # Availability
            try:
                try:
                    availability = item.find_element_by_xpath('.//div[@class="a-section a-spacing-base"]//span[@class="a-size-medium a-color-price"]').get_attribute('innerText')
                except:
                    availability = item.find_element_by_xpath('.//span[@class="a-size-medium a-color-success"]').get_attribute('innerText')
                print(availability)
                specific_dict.setdefault("Availability", []).append(availability)
            except:
                print('Out of Stock')
                specific_dict.setdefault("Availability", []).append('Out of Stock')
            # Image
            try:
                image = item.find_element_by_xpath('.//div[@class="imgTagWrapper"]//img').get_attribute('src')
                print(image)
                picture.append(image)
            except:
                print('Cannot retrieve image')
                picture.append('Cannot retrieve image')

            # Shipping
            try:
                shipping = item.find_element_by_xpath('.//div[@id="exports_desktop_qualifiedBuybox_tlc_feature_div"]//span').get_attribute('innerText')
                print(shipping)
                specific_dict.setdefault("Shipping", []).append(shipping)
            except:
                print('Shipping not available')
                specific_dict.setdefault("Shipping", []).append('Shipping not available')

            # Other Info
            try:
                type = item.find_element_by_xpath('.//div[@class="a-row"]//label').get_attribute('innerText')
                type_sub = item.find_element_by_xpath('.//div[@class="a-row"]//span[@class="selection"]').get_attribute('innerText')
                print(type + type_sub)
                info = type + type_sub
                specific_dict.setdefault("Other Information", []).append(info)
            except:
                print('No other information')
                specific_dict.setdefault("Other Information", []).append('No other information')

            print('')

        except:
            print('error')

    # driver.close()
    # driver.quit()

def amazon_deals():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get('https://www.amazon.com')
    search_box = driver.find_element_by_xpath('//*[@id="nav-xshop"]/a[1]')
    search_box.send_keys(Keys.ENTER)
    sleep(5)
    result = driver.find_elements_by_xpath('//*[@class="a-row dealContainer dealTile"]')
    print(result)
    for item in result:
        try:
            # Product title
            title = item.find_element_by_xpath('.//a[contains(@id, "dealTitle")]//span[contains(@class, "a-declarative")]').get_attribute('innerText')
            deals_dict.setdefault("Product", []).append(title)
            print(title)

            # Price
            try:
                price = item.find_element_by_xpath('.//span[contains(@class, "gb-font-size-medium inlineBlock unitLineHeight dealPriceText")]').get_attribute('innerText')
                print(price)
                deals_dict.setdefault("Price", []).append(price)
            except:
                print('No Rating')
                deals_dict.setdefault("Price", []).append('Price not available')
            # Hours left
            try:
                time = item.find_element_by_xpath('.//span[contains(@role, "timer")]').get_attribute('innerText')
                print(time)
                deals_dict.setdefault("Time Left", []).append('Ends in ' + time)
            except:
                print('No Time')
                deals_dict.setdefault("Time Left", []).append('Time till deal cut off not available')
            # Number of Ratings
            try:
                rate = item.find_element_by_xpath('.//span[contains(@class, "a-size-small a-color-base")]').get_attribute('innerText')
                print(rate)
                deals_dict.setdefault("Number of Ratings", []).append(f'Rated by {rate} users')
            except:
                print('No. of ratings not available')
                deals_dict.setdefault("Number of Ratings", []).append('No. of ratings not available')
            # Deal of the Day
            try:
                deal = item.find_element_by_xpath('.//span[contains(@class, "a-size-mini a-color-base dotdBadge")]').get_attribute('innerText')
                print(deal)
                deals_dict.setdefault("Deal Type", []).append('Prime ' + deal)
            except:
                print('Amazon Deal')
                deals_dict.setdefault("Deal Type", []).append('Amazon Deal')


            print('')

        except:
            print('error')

    # driver.close()
    # driver.quit()