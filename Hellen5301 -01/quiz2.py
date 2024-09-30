#quiz 2.  2016 filtered the dataset

import pandas as pd
import streamlit as st

#1: Load the dataset
df = pd.read_csv(r'C:\Users\User\Desktop\kickstarter_2016.csv')

#2: Convert the 'launched' column to datetime
df['Launched'] = pd.to_datetime(df['Launched'])

#3: Filter the dataset for campaigns launched in 2016
df_2016 = df[df['Launched'].dt.year == 2016]

# 4:Check for missing values
st.dataframe(df.isnull().sum())
