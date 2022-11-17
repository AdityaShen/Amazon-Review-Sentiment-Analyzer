import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import csv
import json
import requests


def app():
    st.title('Analyzing the data extracted from the CSV')

    def request_analysis(text_to_analyze):
        payload = "text=" + str(text_to_analyze)
        response = requests.post("http://text-processing.com/api/sentiment/", data=payload)
        return response
        
    button=st.button("Analyze Data")
    if button:
            countpos = 0
            countneg = 0
            countneu = 0
            with open('data.csv',encoding="utf8",newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                next(reader)
                for row in reader:
                    try:    
                        print('Analyzing: ' + str(row))
                        output = request_analysis(str(row))
                        output = output.json()
                        if 'pos' in output['label']:
                            print('Analyzed as positive')
                            countpos += 1
                        elif 'neg' in output['label']:
                            print('Analyzed as negative')
                            countneg += 1
                        else:
                            print('Analyzed as neutral')    
                            countneu += 1
                        print()
                
                    except UnicodeEncodeError as e:
                        continue  
            csvfile.close()
            st.write('The `distribution` of reviews on the product are: ')
            st.text("")
            st.text("")
            st.text("")
            chart_data = pd.DataFrame({'Number of Users':[countpos,countneg,countneu], 'Type of Sentiment':['Positive','Negative','Neutral']})
            bar_chart=alt.Chart(chart_data).mark_bar().encode(
            y='Number of Users',x='Type of Sentiment',).properties(
            width=800,height=700).configure_axis(labelFontSize=15,titleFontSize=20,)
            def centurygothic():
                font = "Century Gothic"

                return {
                    "config" : {
                        "title": {'font': font},
                        "axis": {
                            "labelFont": font,
                            "titleFont": font
                        }
                    }
                }

            alt.themes.register('centurygothic', centurygothic)
            alt.themes.enable('centurygothic')
            st.altair_chart(bar_chart,use_container_width=True)
            st.text("")
            st.text("")
            st.write("Number of positive reviews for the product:",countpos)
            st.write("Number of neutral reviews for the product:",countneu)
            st.write("Number of negative reviews for the product:",countneg)
            
            