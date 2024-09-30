import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("C:/Users/User/Desktop/filter2016.csv")  # Adjust the path as necessary

# Checking unique values in the 'State' column to identify correct labels
unique_states = df['State'].unique()
print(unique_states)

