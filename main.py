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

# Set the same width for all columns in the table
column_width = st.sidebar.slider("Column Width", min_value=50, max_value=500, value=100)
st.write(f'<style>div.row-widget.stRadio > div{column_width}px</style>', unsafe_allow_html=True)

# Display the table with enhanced visual
columns_to_display = filtered_leads.columns.tolist()

# Set table width to fit the content
table_width = len(columns_to_display) * column_width
st.markdown(f'<style>div[data-testid="stTable"][role="table"] table{{width: {table_width}px !important;}}</style>', unsafe_allow_html=True)

# Customize the cell values for specific columns
cell_formatters = {
    'LinkedIn': lambda link: f'<a href="{link}" target="_blank">{link}</a>',
    'Email': lambda email: f'<a href="mailto:{email}">{email}</a>'
}

# Display the table with wrapped content for long entries
table_data = filtered_leads[columns_to_display].copy()
for column in columns_to_display:
    if column in cell_formatters:
        table_data[column] = table_data[column].apply(cell_formatters[column])

st.table(table_data)

# Save the updated leads data to the CSV file (optional)
# leads_data.update(filtered_leads)
# leads_data.to_csv('Leads.csv', index=False)
