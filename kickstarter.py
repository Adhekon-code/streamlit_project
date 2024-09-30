 # git --version
# Get the 2016 filtered the dataset from the  whole of the data

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset (replace 'your_dataset.csv' with the actual file name)
df = pd.read_csv('kickstarter.csv')

st.write("Checking to see the columns in the dataset:")
st.write(df.columns.tolist())

# Convert the 'Launched' column to datetime format
df['Launched'] = pd.to_datetime(df['Launched'])

# Extract the year from the 'Launched' column
df['Launch'] = df['Launched'].dt.year

# Filter for campaigns launched in 2016
st.write("Filtered 2016 Data set from the total of 2009 to 2017:")
filtered_data = df[df['Launch'] == 2016]

# Display the filtered dataset
st.dataframe(filtered_data)

# Select only the critical columns
st.write("Figuring out the 5 critical columns for 2016 Dataset:")
critical_columns = ['Launched', 'Goal', 'Category', 'Pledged', 'Backers', 'State']
critical_data = filtered_data[critical_columns]

# Display the filtered critical dataset in the Streamlit app
st.write("Filtered critical columns for campaigns launched in 2016:")
st.dataframe(critical_data)


# Count the number of successful vs. unsuccessful campaigns
state_counts = critical_data['State'].value_counts()

# Check if the dataset is balanced
total_campaigns = state_counts.sum()
successful_campaigns = state_counts.get('Successful', 0)
unsuccessful_campaigns = state_counts.get('Failed', 0) + state_counts.get('Canceled', 0)  # Include other states if necessary

#analyzing 2016 filtered data and examining the state of the campaign
st.write("What is the distribution of campaign states (successful vs. unsuccessful)?:")
st.write("This question helps in understanding the overall success rate of campaigns in the dataset:")

# Display the balance information
st.write("Total campaigns:", total_campaigns)
st.write("Successful campaigns:", successful_campaigns)
st.write("Unsuccessful campaigns:", unsuccessful_campaigns)
st.write("Is the dataset balanced?", "Yes" if successful_campaigns == unsuccessful_campaigns else "No")

# Visualization
plt.figure(figsize=(10, 5))
sns.countplot(data=critical_data, x='State', order=state_counts.index, palette='viridis', hue='State', legend=False)
plt.title('Distribution of Campaign States for 2016')
plt.xlabel('Campaign State')
plt.ylabel('Number of Campaigns')
plt.xticks(rotation=45)

# Show the plot in Streamlit
st.pyplot(plt)


# Count successful and unsuccessful campaigns by category
success_counts = critical_data[critical_data['State'] == 'Successful'].groupby('Category').size()
failure_counts = critical_data[critical_data['State'] != 'Successful'].groupby('Category').size()

# Create a DataFrame to combine the counts
category_counts = pd.DataFrame({
    'Successful': success_counts,
    'Unsuccessful': failure_counts
}).fillna(0)

# Get the top three categories for successful and unsuccessful campaigns
top_successful = category_counts.nlargest(3, 'Successful')
top_unsuccessful = category_counts.nlargest(3, 'Unsuccessful')

# Display the results in Streamlit
st.write("Top 3 Categories for Successful Campaigns:")
st.dataframe(top_successful)

st.write("Top 3 Categories for Unsuccessful Campaigns:")
st.dataframe(top_unsuccessful)

# Create a bar plot for visual representation
plt.figure(figsize=(12, 6))
category_counts.plot(kind='bar', stacked=True, color=['green', 'red'])
plt.title('Distribution of Successful and Unsuccessful Campaigns by Category (2016)')
plt.xlabel('Category')
plt.ylabel('Number of Campaigns')
plt.xticks(rotation=45)
plt.legend(title='Campaign State')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#  Display the plot in Streamlit
st.pyplot(plt)

# Horizontal bar chart for top categories
plt.figure(figsize=(12, 6))

 #Define the bar width
bar_width = 0.35

# Set the positions of the bars on the x-axis
r1 = np.arange(len(category_counts))  # Positions for successful
r2 = [x + bar_width for x in r1]  # Positions for unsuccessful (offset)

# Plot the successful campaigns in green
plt.bar(r1, category_counts['Successful'], color='green', width=bar_width, label='Successful', alpha=0.7)
# Plot unsuccessful campaigns
plt.bar(r2, category_counts['Unsuccessful'], color='red', width=bar_width, label='Unsuccessful', alpha=0.7)

st.write("Comparison using Side-by-Side Bar Chart:")
plt.title('Top Categories for Successful and Unsuccessful Campaigns (2016)')
plt.xlabel('Number of Campaigns')
plt.ylabel('Category')
plt.legend()
plt.grid(axis='x')
plt.show()

# Optional: Display the plot in Streamlit
st.pyplot(plt)

st.write("Distribution of the funding goal-There are a small number of campaigns with very high funding:")

# Apply log transformation to the 'Goal' column
df['Log_Goal'] = np.log10(df['Goal'] + 1)  # Adding 1 to avoid log(0)

# Create a histogram to show the distribution of log-transformed funding goals
plt.figure(figsize=(12, 6))
plt.hist(df['Log_Goal'], bins=30, color='blue', alpha=0.7)
plt.title('Distribution of Log-Transformed Funding Goals')
plt.xlabel('Log10(Goal Amount)')
plt.ylabel('Number of Campaigns')
plt.grid(axis='y')

# Display the plot in Streamlit
st.pyplot(plt)
