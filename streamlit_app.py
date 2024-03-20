import streamlit as st
import pandas as pd
import requests
from datetime import datetime

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

# Sidebar for the date input
with st.sidebar:
    # Use the st.date_input component to receive a date input
    selected_date = st.date_input("Select date", datetime.today())
    # Display the selected date in the format "DD-MM-YYYY"
    st.write("Selected Date:", selected_date.strftime("%d-%m-%Y"))

# Display data in Streamlit
st.title('Dashboard Visualisasi Data')

# Button for refreshing data
if st.button('Refresh Data'):
    df = get_data()
    st.write(df)
else:
    # Display the initial data when the app is first run
    df = get_data()
    st.write(df)
