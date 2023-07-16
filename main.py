import streamlit as st
import pandas as pd

# Load the leads data from the CSV file
leads_data = pd.read_csv('Leads.csv')

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

# Apply filters to the leads data
filtered_leads = leads_data.copy()

if filter_name:
    filtered_leads = filtered_leads[filtered_leads['First Name'].str.contains(filter_name, case=False)]

if filter_location:
    filtered_leads = filtered_leads[filtered_leads['Location'].str.contains(filter_location, case=False)]

if filter_stage != 'All':
    filtered_leads = filtered_leads[filtered_leads['Stage'].astype(str) == filter_stage]

# Display the table with one row per lead
columns_to_display = filtered_leads.columns.tolist()
for idx, row in filtered_leads.iterrows():
    st.write('---')
    st.write(f"**Lead {idx + 1}**")
    for column in columns_to_display:
        st.write(f"**{column}:** {row[column]}")

# Save the updated leads data to the CSV file (optional)
# leads_data.update(filtered_leads)
# leads_data.to_csv('Leads.csv', index=False)
