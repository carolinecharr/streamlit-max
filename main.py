import streamlit as st
import pandas as pd

# Load the leads data from the CSV file
leads_data = pd.read_csv('Leads.csv')

# Set page title
st.title('Collecting Leads from LinkedIn')

# Define the filter options for Name, Location, and Stage
filter_name = st.text_input('Filter by Name')
filter_location = st.text_input('Filter by Location')
filter_stage = st.selectbox('Filter by Stage', ['', '1', '2', '3'])

# Apply filters to the leads data
filtered_leads = leads_data[
    (leads_data['First Name'].str.contains(filter_name, case=False)) &
    (leads_data['Location'].str.contains(filter_location, case=False))
]

if filter_stage != '':
    filtered_leads = filtered_leads[filtered_leads['Stage'].astype(str) == filter_stage]

# Set default value of 1 for leads with an empty stage
filtered_leads.loc[filtered_leads['Stage'].isnull(), 'Stage'] = 1

# Create a copy of the filtered leads for display and updating
updated_leads = filtered_leads.copy()

# Display the table with editable stage values
columns_to_display = ['First Name', 'Last Name', 'Job Title', 'Location', 'Stage']

# Helper function to update stage value on cell click
def update_stage_value(row_index, column_name, new_value):
    updated_leads.at[row_index, column_name] = new_value

# Iterate through each lead and create an editable table cell for the stage column
for idx, row in updated_leads.iterrows():
    cell_value = st.selectbox(f"Lead {idx + 1} Stage", ['', '1', '2', '3'], index=row['Stage'])
    if cell_value != '':
        update_stage_value(idx, 'Stage', int(cell_value))

st.table(updated_leads[columns_to_display].style.set_table_styles([
    {'selector': 'th', 'props': [('max-width', '150px')]}  # Set maximum width for all columns
]))

# Update the leads_data with the updated stage values
leads_data.update(updated_leads)

# Save the updated leads data to the CSV file
leads_data.to_csv('leads.csv', index=False)
