import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv("C:/Users/User/Desktop/filter2016.csv")  # Adjust the path as necessary



# Filter for unsuccessful campaigns (assuming the 'State' column indicates 'Failed' or 'Successful')
unsuccessful_campaigns = df[df['State'] == 'Failed']

# Group by Category and Subcategory to get the count of unsuccessful campaigns
unsuccessful_by_category_subcategory = unsuccessful_campaigns.groupby(['Category', 'Subcategory']).size().reset_index(name='Count')

# Display the result in Streamlit
st.write("Unsuccessful Campaigns by Category and Subcategory")
st.dataframe(unsuccessful_by_category_subcategory)

# Optional: You can also display this information in a chart (bar chart) for better visualization
st.write("Bar Chart of Unsuccessful Campaigns by Category and Subcategory")

# Create a bar chart using Streamlit's built-in functionality
st.bar_chart(unsuccessful_by_category_subcategory.set_index(['Category', 'Subcategory'])['Count'])
