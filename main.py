import streamlit as st
import pandas as pd

# Load the leads data from the CSV file
leads_data = pd.read_csv('Leads.csv')

# Set page title
st.title('Collecting Leads from LinkedIn')

# Define the filter options for Name, Location, and Stage
filter_name, filter_location, filter_stage = st.beta_columns(3)

# Text input for Name filter
name_input = filter_name.text_input('Filter by Name')

# Text input for Location filter
location_input = filter_location.text_input('Filter by Location')

# Selectbox for Stage filter
stage_options = ['', '1', '2', '3']
stage_input = filter_stage.selectbox('Filter by Stage', stage_options)

# Apply filters to the leads data
filtered_leads = leads_data[
    (leads_data['First Name'].str.contains(name_input, case=False)) &
    (leads_data['Location'].str.contains(location_input, case=False))
]

if stage_input != '':
    filtered_leads = filtered_leads[filtered_leads['Stage'].astype(str) == stage_input]

# Set default value of 1 for leads with an empty stage
filtered_leads.loc[filtered_leads['Stage'].isnull(), 'Stage'] = 1

# Create a copy of the filtered leads for display and updating
updated_leads = filtered_leads.copy()

# Create an editable table for the leads
columns_to_display = ['First Name', 'Last Name', 'Job Title', 'Location', 'Stage']

# Helper function to update stage value on cell update
def update_stage_value(updated_stage, row_index, col_index):
    updated_leads.at[row_index, columns_to_display[col_index]] = updated_stage

# Display the table with editable stage values
for idx, row in updated_leads.iterrows():
    for col_idx, column in enumerate(columns_to_display):
        if column == 'Stage':
            if stage_input == '':
                st.write(row[column])
            else:
                updated_stage = st.selectbox(f"Lead {idx + 1} Stage", ['', '1', '2', '3'], index=row[column] - 1)
                if updated_stage != '':
                    update_stage_value(int(updated_stage), idx, col_idx)
        else:
            st.write(row[column])

st.table(updated_leads[columns_to_display])

# Update the leads_data with the updated stage values
leads_data.update(updated_leads)

# Save the updated leads data to the CSV file
leads_data.to_csv('Leads.csv', index=False)
