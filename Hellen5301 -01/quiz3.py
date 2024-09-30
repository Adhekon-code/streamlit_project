import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("C:/Users/User/Desktop/filter2016.csv")  # Adjust the path as necessary

import streamlit as st
import matplotlib.pyplot as plt

# Assuming data is already loaded as 'data'
outcome_distribution = data['State'].value_counts()

# Plotting a Pie Chart
fig, ax = plt.subplots()
ax.pie(outcome_distribution, labels=outcome_distribution.index, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
ax.set_title('Campaign Outcome Distribution (2016)')

# Display the plot in Streamlit
st.pyplot(fig)
