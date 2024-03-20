import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

# Function to get data from Google Spreadsheet
def get_data():
    # Your spreadsheet's published CSV URL
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTnflGSDkG_l9mSnawp-HEHX-R5jMfluS1rp0HlF_hMBpQvtG21d3-zPE4TxD80CvQVPjJszeOmNWJB/pub?gid=384797514&single=true&output=csv'
    
    # Read the CSV content into a DataFrame
    df = pd.read_csv(url)

    # Convert the 'TAHUN DT' column to numeric, coercing errors to NaN
    df['TAHUN DT'] = pd.to_numeric(df['TAHUN DT'], errors='coerce')

    # Fill NaN values with a value of your choice or drop them
    df['TAHUN DT'] = df['TAHUN DT'].fillna(0).astype(int) # Option 1: Fill with 0
    # df = df.dropna(subset=['TAHUN DT'])  # Option 2: Drop rows with NaN in 'TAHUN DT'

    # Now safely convert to integers
    df['TAHUN DT'] = df['TAHUN DT'].astype(int)

    return df

# Display data in Streamlit
st.title('Dashboard Visualisasi Data')

# Sidebar for the date range input
with st.sidebar:
    # Calculate the next year
    today = datetime.now()
    next_year = today.year 
    start_date = datetime(next_year, 1, 1)  # Start of next year
    end_date = datetime(next_year, 12, 31)  # End of next year
    
    # Use the st.date_input component to receive a date range input
    selected_start_date, selected_end_date = st.date_input(
        "Select your vacation for next year",
        value=(start_date, start_date + timedelta(days=30)),  # Default to a 30-day range
        min_value=start_date,
        max_value=end_date
    )

    # Display the selected date range in the format "DD-MM-YYYY"
    st.write("Selected Start Date:", selected_start_date.strftime("%d-%m-%Y"))
    st.write("Selected End Date:", selected_end_date.strftime("%d-%m-%Y"))

# Button for refreshing data
if st.button('Refresh Data'):
    df = get_data()
    st.write(df)
else:
    # Display the initial data when the app is first run
    df = get_data()
    st.write(df)
