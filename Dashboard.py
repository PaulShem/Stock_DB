import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Market Price Analysis Dashboard",
    layout="wide",
)
path = "./data/data.online.csv"
df = pd.read_csv(path)

numeric_df = df.select_dtypes(['float', 'int'])
numeric_cols = numeric_df.columns
text_df = df.select_dtypes(['object'])
text_cols = text_df.columns

st.title("Market Price analysis Dashboard:")
st.sidebar.title("Market Price Analysis Dashboard")
st.sidebar.header("Please Select Here:")
check_box = st.sidebar.checkbox(label="Display Dataset")

clist = df['company'].unique()
selected_company = st.sidebar.selectbox("Select a company:",clist)

with st.sidebar:
    start = st.date_input('Start', value=pd.to_datetime('2020-10-1'))
    end = st.date_input('End', value=pd.to_datetime('2020-10-30'))
if check_box:
    st.write(df)

filtered_df = df[df['company'] == selected_company]
line_fig = px.line(filtered_df,
                   x='date', y='price',
                   title=f'Market Price for {selected_company}')

st.plotly_chart(line_fig)






    



