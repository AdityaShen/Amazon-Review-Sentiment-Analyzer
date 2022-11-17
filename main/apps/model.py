import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

def app():
    st.title('View the extracted data')

    st.write('Click the `button` to view the extracted data from the products given.')

    button=st.button("Show Extracted Data")
    if button:
        st.write(pd.read_csv("data.csv"))
