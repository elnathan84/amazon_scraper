# Amazon Webscraper by Jopak's Angels
## About
 Webscrape Amazon through Amazon Search, Product URL, or Best Selling Products. You can also get the csv file by clicking the download link after scrapping process.
 
 This program was created by _**Elnathan John Salvarria, Kynch Tito Silao, and Kizzel Mae Tulog.**_
 
<div align="center"><img src="https://user-images.githubusercontent.com/66759228/120319848-096f8d80-c314-11eb-8b74-8cfe9854c06c.png" width="200" height="200"><img src="https://user-images.githubusercontent.com/66759228/120319841-07a5ca00-c314-11eb-9d74-4ce316da5975.png" width="200" height="200"><img src="https://user-images.githubusercontent.com/66759228/120319736-eba22880-c313-11eb-9922-932aa34ad84f.png" width="200" height="200"></div>

## Web Application
This application is running through streamlit web platfrom
[Amazon Webscraper](https://streamlit.io/)

### How to install
For VCS

    https://github.com/elnathan84/amazon_scraper.git
For terminal installation

    go get -t -d https://github.com/elnathan84/amazon_scraper.git
    
It is important to install the [Chromedriver](https://chromedriver.chromium.org/downloads) and the other packages needed for the program.

### Instructions
To get the app running type in the terminal:
  
    streamlit run app.py
You can choose three options to scrape data in Amazon:

![Options](https://user-images.githubusercontent.com/66759228/120329894-e0082f00-c31e-11eb-874c-53773c429e93.PNG)


* Product URL: Input your desired URL.

* Search Amazon: Input your desired product.

![URL](https://user-images.githubusercontent.com/66759228/120331018-f19e0680-c31f-11eb-8a24-6f41966478a3.PNG)

* Amazon Today's Deal: Outputs the current deal in the amazon list.

<img src="https://user-images.githubusercontent.com/66759228/120331124-0a0e2100-c320-11eb-8c32-2a11e754e44b.PNG">

## Column/Data key Definition
The output of the Amazon search scraper and its definitions:
| Column/Key Name | Product Name | Price | Previous Price | Rating | Shipping | Stock | Coupon |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Definition | Outputs the user search results | Shows the current price | Shows the previous price | Shows the rating of the product | Shows if its available to be shipped in current location | Number of stocks for the product | Shows if there's an available coupon | 

The output of the Amazon product URL scraper and its definitions:
| Column/Key Name | Product Name | Rating | Price | Seller | Availability | Shipping | Other Information |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Definition | Outputs the Product name | Shows the rating | Shows the price | Shows who is the seller of the product | Shows the stock information  | Shows if the shipping information and location | Shows other related information | 

The output of the Amazon Today's Deals scraper and its definitions:
| Column/Key Name | Product | Price | Time Left | Number of Ratings | Deal Type | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| Definition | Outputs the Product name | Shows the range of price of the product | Shows how much time is left before end of the deal | Shows how many users rated the product | Shows what type of Amazon Deal is the product  | 