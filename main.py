import streamlit as st
import pandas as pd

# Load the leads data from the CSV file
leads_data = pd.read_csv('Leads.csv')

# Define the filter options for Name, Location, and Stage
filter_name = st.sidebar.text_input('Filter by Name')
filter_location = st.sidebar.text_input('Filter by Location')
filter_stage = st.sidebar.selectbox('Filter by Stage', ['1', '2', '3'])

# Apply filters to the leads data
filtered_leads = leads_data[
    (leads_data['First Name'].str.contains(filter_name, case=False)) &
    (leads_data['Location'].str.contains(filter_location, case=False)) &
    (leads_data['Stage'] == int(filter_stage))
]

# Display the filtered leads table
st.table(filtered_leads)

# Allow users to update the stage value for each lead using a dropdown button
if st.checkbox('Update Stage Value'):
    updated_leads = leads_data.copy()
    for idx, row in updated_leads.iterrows():
        new_stage = st.selectbox(f"Lead {idx + 1} Stage", ['1', '2', '3'], index=row['Stage'] - 1)
        updated_leads.at[idx, 'Stage'] = int(new_stage)
    st.table(updated_leads)
