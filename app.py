import streamlit as st
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import numpy as np

#Webapp
st.set_page_config(page_title = "Amazon Webscraper")


desc = "Webscrape Amazon through Product URL or Amazon Search\
        You can either enter the Product URL or just search Amazon through here.\
        This app was developed with Streamlit and Selenium for the webapp and scraping features\
        Check out our github repository! (https://github.com/gnsslrrcs/dlsud-cpse325-2021/tree/major-exam/scraping/Amazon).\
        "

st.title("Jopak's Angels' Amazon Webscraper")
st.markdown(desc)
st.subheader("Select the option")
select_input = st.radio("Select Input:", ["Product URL", "Search Amazon"])

if select_input == "Product URL":
    url = st.text_input("URL")
    if st.button("Scrape It!"):
        print("")
        # text = get_page_text(url)
        # generate_output(text)

else:
    text = st.text_area("Search Amazon")
    if st.button("Scrape It!"):
        print("")
        # generate_output(text)