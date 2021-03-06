import streamlit as st
import csv
import numpy as np
from amazon_scraper import amazon_search, search_dict, amazon_specific, specific_dict, picture, amazon_deals, deals_dict
import pandas as pd
import time
import base64


def load_searchdata():
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)

        # Update status text.
        status_text.text('Loading')

        # Doing computation, wink wink
        time.sleep(0.01)

        while i == 50:
            with st.spinner("The angels are scraping..."):
                amazon_search(text)
            st.success('We have returned with glorious data!')
            df = pd.DataFrame.from_dict(search_dict)
            # df = df.drop(df.index[7])
            # dfr = df.reset_index(drop=True)
            progress_bar.progress(i + 1)
            i += 1
    status_text.empty()
    st.balloons()
    st.dataframe(df)

    csv = df.to_csv(index=True)
    b64 = base64.b64encode(csv.encode()).decode()
    st.markdown('### **⬇️ Download CSV File **')
    href = f'<a href="data:file/csv;base64,{b64}" download="amazon_search.csv">Amazon Search Results</a>'
    st.markdown(href, unsafe_allow_html=True)


def load_specificdata():
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)

        # Update status text.
        status_text.text('Loading')

        # Doing computation, wink wink
        time.sleep(0.01)

        while i == 50:
            with st.spinner("The angels are scraping..."):
                amazon_specific(url)
            st.success('We have returned with glorious data!')
            df = pd.DataFrame.from_dict(specific_dict)
            # df = df.drop(df.index[7])
            # dfr = df.reset_index(drop=True)
            progress_bar.progress(i + 1)
            i += 1
    status_text.empty()
    st.balloons()
    st.dataframe(df)

    csv = df.to_csv(index=True)
    b64 = base64.b64encode(csv.encode()).decode()
    st.markdown('### **⬇️ Download CSV File **')
    href = f'<a href="data:file/csv;base64,{b64}" download="amazon_pd.csv">Product Data</a>'
    st.markdown(href, unsafe_allow_html=True)


def load_dealsdata():
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)

        # Update status text.
        status_text.text('Loading')

        # Doing computation, wink wink
        time.sleep(0.01)

        while i == 50:
            with st.spinner("The angels are scraping..."):
                amazon_deals()
            st.success('We have returned with glorious data!')
            df = pd.DataFrame.from_dict(deals_dict)
            # df = df.drop(df.index[7])
            # dfr = df.reset_index(drop=True)
            progress_bar.progress(i + 1)
            i += 1
    status_text.empty()
    st.balloons()
    st.dataframe(df)

    csv = df.to_csv(index=True)
    b64 = base64.b64encode(csv.encode()).decode()
    st.markdown('### **⬇️ Download CSV File **')
    href = f'<a href="data:file/csv;base64,{b64}" download="amazon_deals.csv">Amazon Deals</a>'
    st.markdown(href, unsafe_allow_html=True)

# Webapp
st.set_page_config(page_title = "Amazon Webscraper")

desc = "Webscrape Amazon through Product URL or Amazon Search.\
        You can either enter the Product URL or just search Amazon through here.\
        This app was developed with Streamlit and Selenium for the webapp and scraping features.\
        Check out our github repository! (https://github.com/gnsslrrcs/dlsud-cpse325-2021/tree/major-exam/scraping/Amazon).\
        "
st.image('./logo.png', width=300)
st.title("Amazon Webscraper")
st.header("By Jopak's Angels")
st.markdown(desc)
st.subheader("Scraping Menu")
select_input = st.radio("Select Input:", ["Product URL", "Search Amazon", "Amazon Today's Deals"])


if select_input == "Product URL":
    url = st.text_input("URL")
    if st.button("Scrape It!"):
        load_specificdata()
        # st.markdown(f"![Cannot Retrieve Image]({picture[0]})")
        st.image(
            f"{picture[0]}",
            width=400, # Manually Adjust the width of the image as per requirement
        )
        specific_dict.clear()
        picture.clear()

        # placeholder(text)
elif select_input == "Amazon Today's Deals":
    if st.button('Show Me!'):
        load_dealsdata()
        deals_dict.clear()
else:
    text = st.text_area("Search Amazon")
    if st.button("Scrape It!"):
        load_searchdata()
        search_dict.clear()




