import streamlit as st
import pandas as pd
import requests

# Membersihkan cache
st.legacy_caching.clear_cache()

# Function to get data from Google Spreadsheet
def get_data():
    # Your spreadsheet's published CSV URL
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTnflGSDkG_l9mSnawp-HEHX-R5jMfluS1rp0HlF_hMBpQvtG21d3-zPE4TxD80CvQVPjJszeOmNWJB/pub?gid=384797514&single=true&output=csv'
    
    # Send a HTTP GET request to the URL
    response = requests.get(url)
    assert response.status_code == 200, 'Wrong status code'

    # Read the CSV content into a DataFrame
    df = pd.read_csv(url)
    
    # Convert the 'TAHUN DT' column to numeric, coercing errors to NaN
    df['TAHUN DT'] = pd.to_numeric(df['TAHUN DT'], errors='coerce')
    
    # Fill NaN values with a value of your choice or drop them
    df['TAHUN DT'] = df['TAHUN DT'].fillna(0).astype(int)

    # Convert the 'TANGGAL' column to date objects
    df['TANGGAL'] = pd.to_datetime(df['TANGGAL'], dayfirst=True, errors='coerce').dt.date

    return df

# Display data in Streamlit
st.title('Monitoring Ketersediaan & Kondisi Dump Truck')

# Get the data
df = get_data()

# Assume 'TANGGAL' is your date column name
if 'TANGGAL' in df.columns and not df['TANGGAL'].isnull().all():
    # Extract dates for the slider
    min_date = df['TANGGAL'].min()
    max_date = df['TANGGAL'].max()

    # Create the date slider
    selected_date_range = st.slider(
        "Pilih Rentang Tanggal",
        value=(min_date, max_date),
        format='DD-MM-YYYY'
    )

    # Filter the dataframe based on the selected date range
    filtered_df = df[(df['TANGGAL'] >= selected_date_range[0]) & (df['TANGGAL'] <= selected_date_range[1])]

    # Display the filtered data
    # Format dates in the dataframe to 'DD-MM-YYYY' before displaying
    filtered_df['TANGGAL'] = filtered_df['TANGGAL'].dt.strftime('%d-%m-%Y')
    st.write(filtered_df)
else:
    st.error("Kolom 'TANGGAL' tidak ditemukan atau mengandung nilai null dalam dataframe.")
