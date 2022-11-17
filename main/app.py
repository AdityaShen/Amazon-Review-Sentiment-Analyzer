import streamlit as st
from multiapp import MultiApp
from apps import login, data, model, analysis

app = MultiApp()
app.add_app("Login", login.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
app.add_app("Analysis", analysis.app)


app.run()
