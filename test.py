from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


search_dict = {"Product Name": [], "Price": [], "Previous Price":[],
               "Rating": [], "Shipping": [], "Stock": [], "Coupon": []};
specific_dict = {[]}

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

def amazon_specific(url):
    # op = webdriver.ChromeOptions()
    # op.add_argument('headless')
    # driver = webdriver.Chrome(options=op)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    sleep(5)
    result = driver.find_elements_by_xpath('//*[@class="a-container"]')
    for item in result:
        try:
            # Product title
            title = item.find_element_by_xpath('.//span[contains(@class, "a-size-large product-title-word-break")]').get_attribute('innerText')
            specific_dict.setdefault("Product Name", []).append(title)
            print(title)
            # Adds Product Name
            try:
                rating = item.find_element_by_xpath('.//span[@class="a-icon-alt"]').get_attribute('innerText')
                print(rating)
                specific_dict.setdefault("Rating", []).append(rating)
            except:
                print('No Rating')
                # search_dict.setdefault("Coupon", []).append('No coupon available')
            try:
                price = item.find_element_by_xpath('.//span[@class="a-size-medium a-color-price"]').get_attribute('innerText')
                print(price)
                specific_dict.setdefault("Rating", []).append(price)
            except:
                print('Out of Stock')
                # search_dict.setdefault("Coupon", []).append('No coupon available')
            try:
                seller = item.find_element_by_xpath('.//a[@id="sellerProfileTriggerId"]').get_attribute('innerText')
                print("Sold by: " + seller)
                specific_dict.setdefault("Rating", []).append(seller)
            except:
                print('Seller data not available')
                # search_dict.setdefault("Coupon", []).append('No coupon available')
            try:
                availability = item.find_element_by_xpath('.//span[@class="a-size-medium a-color-success"]').get_attribute('innerText')
                print(availability)
                specific_dict.setdefault("Rating", []).append(availability)
            except:
                print('Out of Stock')
                # search_dict.setdefault("Coupon", []).append('No coupon available')
            print('')

        except:
            print('error')


    # driver.close()
    # driver.quit()

amazon_specific('https://www.amazon.com/Beginners-Quadcopter-Altitude-Trajectory-Toys-Light/dp/B08TRF2H6N/ref=sr_1_1_sspa?dchild=1&keywords=drone&qid=1622619408&sr=8-1-spons&psc=1&smid=A32I8WIBPR7WGY&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVUlJRDZOVFJOTEpVJmVuY3J5cHRlZElkPUEwNDk1NDMyMUcwOUtRSktLQkFPNiZlbmNyeXB0ZWRBZElkPUEwMjMwNDA2MUlENE5aOVNQRDdSMyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=')
