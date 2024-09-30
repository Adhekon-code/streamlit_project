

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/Users/User/Desktop/filter2016.csv")  # Adjust the path as necessary

# Apply log transformation to the funding goals
df['Log_Goal'] = np.log10(df['Goal'])  # Replace 'Goal' with the actual column name for funding goals

# Create a figure
plt.figure(figsize=(10, 6))

# Plot histogram with density
sns.histplot(df['Log_Goal'].dropna(), bins=30, kde=True, color='skyblue', edgecolor='black')

# Customize the plot
plt.title('Distribution of Log-transformed Funding Goals')
plt.xlabel('Log10(Funding Goal)')
plt.ylabel('Density')
plt.grid(axis='y', alpha=0.75)

# Show the plot in Streamlit
st.pyplot(plt)

# Optionally, display basic statistics
st.write("Basic Statistics of Log-transformed Funding Goals:")
st.write(df['Log_Goal'].describe())
