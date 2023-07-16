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

# Create a copy of the filtered leads for display and updating
updated_leads = filtered_leads.copy()

# Create an editable table for the leads
columns_to_display = updated_leads.columns.tolist()

# Helper function to update stage value on cell update
def update_stage_value(updated_stage, row_index):
    updated_leads.at[row_index, 'Stage'] = updated_stage

# Display the table with editable stage values
for idx, row in updated_leads.iterrows():
    for column in columns_to_display:
        if column == 'Stage':
            if filter_stage == 'All':
                st.write(row[column])
            else:
                updated_stage = st.selectbox(f"Lead {idx + 1} Stage", ['', '1', '2', '3'], index=row[column] - 1)
                if updated_stage != '':
                    update_stage_value(int(updated_stage), idx)
        else:
            st.write(row[column])

# Save the updated leads data to the CSV file (optional)
# leads_data.update(updated_leads)
# leads_data.to_csv('Leads.csv', index=False)
