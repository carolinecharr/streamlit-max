import streamlit as st
import pandas as pd
from streamlit_aggrid import AgGrid, GridOptionsBuilder, AgGridConfigBuilder

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

# Configure the editable table using streamlit-aggrid
gb = GridOptionsBuilder.from_dataframe(filtered_leads)
gb.configure_default_column(groupable=True, editable=True)
grid_options = gb.build()

# Create a copy of the filtered leads for display and updating
updated_leads = filtered_leads.copy()

# Display the editable table
ag = AgGrid(
    updated_leads,
    gridOptions=grid_options,
    width='100%',
    data_return_mode='AS_INPUT',
    update_mode='VALUE_CHANGED',
    fit_columns_on_grid_load=True,
)

# Update the leads_data with the updated stage values
leads_data.update(updated_leads)

# Save the updated leads data to the CSV file (optional)
# leads_data.to_csv('Leads.csv', index=False)
