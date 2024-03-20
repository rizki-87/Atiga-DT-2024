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
    # Ensure the 'TAHUN DT' column is treated as integers to remove commas
    df['TAHUN DT'] = df['TAHUN DT'].astype(int)
    return df

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
