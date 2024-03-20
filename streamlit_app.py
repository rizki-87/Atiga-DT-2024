import streamlit as st
import pandas as pd
import requests

# Function to get data from Google Spreadsheet
def get_data():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTnflGSDkG_l9mSnawp-HEHX-R5jMfluS1rp0HlF_hMBpQvtG21d3-zPE4TxD80CvQVPjJszeOmNWJB/pub?output=xlsx'
    response = requests.get(url)
    assert response.status_code == 200, 'Wrong status code'
    df = pd.read_excel(url)

    # Clean and convert the 'TAHUN DT' column
    df['TAHUN DT'] = pd.to_numeric(df['TAHUN DT'], errors='coerce').fillna(0).astype(int)

    # Convert the 'TANGGAL' column to dates
    df['TANGGAL'] = pd.to_datetime(df['TANGGAL'], errors='coerce').dt.date
    return df

# Display data in Streamlit
st.title('Monitoring Ketersediaan & Kondisi Dump Truck')
df = get_data()

# Check if 'TANGGAL' column exists and has no nulls
if 'TANGGAL' in df.columns and not df['TANGGAL'].isnull().all():
    min_date, max_date = df['TANGGAL'].min(), df['TANGGAL'].max()
    selected_date_range = st.slider("Pilih Rentang Tanggal", value=(min_date, max_date))
    filtered_df = df[df['TANGGAL'].between(*selected_date_range)]
    st.write(filtered_df)
else:
    st.error("Kolom 'TANGGAL' tidak ditemukan atau mengandung nilai null dalam dataframe.")
