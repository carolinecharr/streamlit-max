import streamlit as st
import pandas as pd

# Load the leads data from the CSV file
leads_data = pd.read_csv('Leads.csv')

# Display the logo
logo = 'vs-logo.png'
st.image(logo, width=100)

# Set page title
st.title('Collecting Leads from LinkedIn')

# Define the filter options for Name, Location, and Stage
col1, col2, col3 = st.columns(3)

# Text input for Name filter
filter_name = col1.text_input('Filter by Name')

# Text input for Location filter
filter_location = col2.text_input('Filter by Location')

# Selectbox for Stage filter
stage_options = ['All', '1', '2', '3']
filter_stage = col3.selectbox('Filter by Stage', stage_options)

# Add spacing between filters and table
st.markdown('<br>', unsafe_allow_html=True)

# Apply filters to the leads data
filtered_leads = leads_data.copy()

if filter_name:
    filtered_leads = filtered_leads[filtered_leads['First Name'].str.contains(filter_name, case=False)]

if filter_location:
    filtered_leads = filtered_leads[filtered_leads['Location'].str.contains(filter_location, case=False)]

if filter_stage != 'All':
    filtered_leads = filtered_leads[filtered_leads['Stage'].astype(str) == filter_stage]

# Display the table with enhanced visual
st.table(filtered_leads)

# Save the updated leads data to the CSV file (optional)
# leads_data.update(filtered_leads)
# leads_data.to_csv('Leads.csv', index=False)

from bs4 import BeautifulSoup

# Sample string
string_content = '''
This is a sample string containing some text.
There are multiple lines and sentences in this string.
We will use BeautifulSoup to parse and extract information.
'''

# Create BeautifulSoup object
soup = BeautifulSoup(string_content, 'html.parser')

# Extract information from the string
lines = soup.get_text().split('\n')
sentences = [sentence.strip() for line in lines for sentence in line.split('.') if sentence.strip()]

# Print the extracted information
print("Lines:")
for line in lines:
    print(line)

print("\nSentences:")
for sentence in sentences:
    print(sentence)
