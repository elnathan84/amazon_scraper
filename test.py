from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


search_dict = {"Product Name": [], "Price": [], "Previous Price":[],
               "Rating": [], "Shipping": [], "Stock": [], "Coupon": []};


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

                # Adds Current Price
                try:

                    c_price = item.find_element_by_xpath('.//span[@class="a-offscreen"]').get_attribute('innerText')
                    print(c_price)
                    search_dict.setdefault("Price", []).append(c_price)
                except:
                    print('Product on exclusive pricing')
                    search_dict.setdefault("Price", []).append("Product on exclusive pricing")

                # Adds Original Price
                try:

                    o_price = item.find_element_by_xpath('.//span[@class="a-price a-text-price"]//span[@class="a-offscreen"]').get_attribute('innerText')
                    print(o_price)
                    search_dict.setdefault("Previous Price", []).append(o_price)
                except:
                    print('No discount')
                    search_dict.setdefault("Previous Price", []).append(c_price)


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
                    search_dict.setdefault("Shipping", []).append(shipping)
                except:
                    print('Shipping not Available')
                    search_dict.setdefault("Shipping", []).append('Shipping not Available')
                # Stock
                try:
                    stock = item.find_element_by_xpath('.//span[@class="a-size-base"]').get_attribute('innerText')
                    print(stock)
                    search_dict.setdefault("Stock", []).append(stock)
                except:
                    print('No stock available')
                    search_dict.setdefault("Stock", []).append('No stock available')
                # Coupon
                try:
                    coupon = item.find_element_by_xpath('.//span[@class="a-size-base s-highlighted-text-padding aok-inline-block s-coupon-highlight-color"]').get_attribute('innerText')
                    print(coupon + ' with coupon')
                    search_dict.setdefault("Coupon", []).append(coupon + ' with coupon')
                except:
                    print('No coupon available')
                    search_dict.setdefault("Coupon", []).append('No coupon available')

            print('')
            dup_check = title
        except:
            print('error')

    driver.close()
    driver.quit()


amazon_search('drone')
