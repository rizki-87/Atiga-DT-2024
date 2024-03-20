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

# Dapatkan data
df = get_data()

# Asumsikan 'TANGGAL' adalah nama kolom tanggal Anda
if 'TANGGAL' in df and not df['TANGGAL'].isnull().all():
    # Konversi string ke datetime jika belum diubah
    df['TANGGAL'] = pd.to_datetime(df['TANGGAL'], errors='coerce')
    
    min_date = df['TANGGAL'].min()
    max_date = df['TANGGAL'].max()

    # Pastikan min_date dan max_date adalah tipe datetime sebelum di set di slider
    if isinstance(min_date, pd.Timestamp) and isinstance(max_date, pd.Timestamp):
        selected_date = st.slider(
            "Pilih Tanggal",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date),
            format="DD-MM-YYYY"
        )

        # Filter data berdasarkan rentang tanggal yang dipilih
        filtered_df = df[df['TANGGAL'].dt.date.between(selected_date[0].date(), selected_date[1].date())]

        # Tampilkan data yang difilter
        st.write(filtered_df)
    else:
        st.error("Kolom 'TANGGAL' tidak dapat dikonversi ke tipe datetime.")
else:
    st.error("Kolom 'TANGGAL' tidak ditemukan atau semua nilainya null dalam dataframe.")
