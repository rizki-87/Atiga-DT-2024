import streamlit as st
import pandas as pd
import requests

# Function to get data from Google Spreadsheet
def get_data():
    # Your spreadsheet's published CSV URL
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTnflGSDkG_l9mSnawp-HEHX-R5jMfluS1rp0HlF_hMBpQvtG21d3-zPE4TxD80CvQVPjJszeOmNWJB/pub?gid=384797514&single=true&output=csv'
    
    # Send a HTTP GET request to the URL
    response = requests.get(url)
    assert response.status_code == 200, 'Wrong status code'  # Check to make sure the request went through

    # Read the CSV content into a DataFrame
    df = pd.read_csv(url)
    # Convert the 'TAHUN DT' column to numeric, coercing errors to NaN
    df['TAHUN DT'] = pd.to_numeric(df['TAHUN DT'], errors='coerce')

    # Fill NaN values with a value of your choice or drop them
    df['TAHUN DT'] = df['TAHUN DT'].fillna(0).astype(int) # Option 1: Fill with 0
    
    # Now safely convert to integers
    df['TAHUN DT'] = df['TAHUN DT'].astype(int)
    return df

# Display data in Streamlit
st.title('Monitoring Ketersediaan & Kondisi Dump Truck')

# Get data
df = get_data()

# Assume 'TANGGAL' is your date column name
if 'TANGGAL' in df.columns:
    df['TANGGAL'] = pd.to_datetime(df['TANGGAL'], errors='coerce')  # Convert string to datetime
    
    # Filter out rows where 'TANGGAL' is NaT after conversion
    df = df[~df['TANGGAL'].isna()]
    
    min_date = df['TANGGAL'].min()
    max_date = df['TANGGAL'].max()

    # Slider for selecting date range
    selected_date_range = st.slider(
        "Select Date Range",
        value=(min_date.to_pydatetime(), max_date.to_pydatetime()),
        format="MM/DD/YY"
    )
    
    # Convert selected_date_range to datetime if not already
    start_date, end_date = pd.to_datetime(selected_date_range[0]), pd.to_datetime(selected_date_range[1])
    
    # Filter dataframe based on selected date range
    filtered_df = df[(df['TANGGAL'] >= start_date) & (df['TANGGAL'] <= end_date)]
    
    # Display filtered data
    st.write(filtered_df)
else:
    st.error("Column 'TANGGAL' not found in dataframe.")
