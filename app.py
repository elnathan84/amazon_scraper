import streamlit as st
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import numpy as np

#Webapp
st.set_page_config(page_title = "Amazon Webscraper")


desc = "This web app detects fake news written in the English Language.\
        You can either enter the URL of a news article, paste the text directly or just use our Chrome Extension.\
        This app was developed with the Streamlit and Spacy Python libraries.\
        This app is modeled and created using the formula and dataset training from (https://github.com/derevirn/gfn-detector).\
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