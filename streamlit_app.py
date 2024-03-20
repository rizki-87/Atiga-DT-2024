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

# Assuming 'TANGGAL' is the name of your date column
if 'TANGGAL' in df:
    min_date = df['TANGGAL'].min()
    max_date = df['TANGGAL'].max()

    # Create the date slider
    selected_date = st.slider(
        "Pilih Tanggal",
        min_value=min_date.to_pydatetime(),  # Convert to python datetime
        max_value=max_date.to_pydatetime(),  # Convert to python datetime
        value=(min_date.to_pydatetime(), max_date.to_pydatetime()),  # Convert to python datetime
        format="DD-MM-YYYY"
    )

    # Filter the data based on the selected date range
    filtered_df = df[df['TANGGAL'].dt.date.between(selected_date[0].date(), selected_date[1].date())]

    # Display the filtered data
    st.write(filtered_df)
else:
    st.error("Column 'TANGGAL' not found in the dataframe.")
