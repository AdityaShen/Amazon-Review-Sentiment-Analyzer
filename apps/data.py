import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from encodings.utf_8 import encode
from selectorlib import Extractor
import requests 
import json 
from time import sleep
import csv
from dateutil import parser as dateparser

def app():

    st.title('Data Extractor')
    st.write("This is the `Data Extractor` page of our product.")
    st.write("Enter the `Review URLs` to generate the CSV file.")
    st.text("")
    st.text("")
    st.text("")
    
    string1 = st.text_input("Enter 1st URL", max_chars=500, )
    st.text("")
    st.text("")
    string2 = st.text_input("Enter 2nd URL", max_chars=500, )
    st.text("")
    st.text("")
    string3 = st.text_input("Enter 3rd URL", max_chars=500, )
    
    st.write("")
    st.write("")
    urllist=[string1,string2,string3,]
    
 
    e= Extractor.from_yaml_file('selectors.yml')

    def scrape(url):    
        headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            }

    # Download the page using requests
        st.write("Downloading %s"%url)
        r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
        if r.status_code > 500:
            if "To discuss automated access to Amazon data please contact" in r.text:
                st.write("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
            else:
                st.write("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
            return None
    # Pass the HTML of the page and create 
        return e.extract(r.text)

    button=st.button("Extract Review Data")
    if button:
# product_data = []
        with open('data.csv','w',encoding="utf8",newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["title","content","product"])
            writer.writeheader()
            for url in urllist:
                if url=="":
                    continue
                data = scrape(url) 
                if data:
                    for r in data['reviews']:
                        r["product"] = data["product_title"]
                #r['url'] = url
                        if 'verified' in r:
                            if 'Verified Purchase' in r['verified']:
                                r['verified'] = 'Yes'
                            else:
                                r['verified'] = 'Yes'
                #r['rating'] = r['rating']
                #date_posted = r['date'].split('on ')[-1]
                #if r['images']:
                    #r['images'] = "\n".join(r['images'])
                #r['date'] = dateparser.parse(date_posted).strftime('%d %b %Y')
                        writer.writerow(r)
                    sleep(5) 
        
    
  
    