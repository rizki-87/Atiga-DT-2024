import streamlit as st
import pandas as pd
import requests
from datetime import datetime, date

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

# Tentukan lokasi logo perusahaan Anda
logo_path = "atiga.png"

# Tampilkan logo di aplikasi Streamlit
# st.image(logo_path, use_column_width=True)

# Menggunakan kolom untuk menyesuaikan tata letak
col1, col2 = st.columns([3, 1])  # Sesuaikan rasio sesuai kebutuhan

with col1:
    st.write("")  # Isi dengan konten atau biarkan kosong

with col2:
    st.image(logo_path, width=150)  # Sesuaikan lebar sesuai kebutuhan

# Display data in Streamlit
st.title('Dashboard Visualisasi Data')

# Load the data
df = get_data()

# Visualization for "STATUS DT"
status_counts = df['STATUS DT'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Distribusi Status DT')

# Display the pie chart in Streamlit
st.pyplot(fig1)

# Sidebar for the slicers
with st.sidebar:
    # Date picker
    start_date = date(2024, 1, 1)
    end_date = date(2024, 12, 31)
    selected_date = st.date_input("Select date", [start_date, start_date], min_value=start_date, max_value=end_date)
    st.write("Selected Start Date:", selected_date[0].strftime("%d-%m-%Y"))
    if len(selected_date) > 1:
        st.write("Selected End Date:", selected_date[1].strftime("%d-%m-%Y"))
    
    # Slicer for "Status DT"
    unique_status = df['STATUS DT'].unique().tolist()
    selected_status = st.multiselect('Select Status DT', unique_status, default=unique_status)
    
    # Slicer for "Jenis DT"
    unique_jenis = df['JENIS DT'].unique().tolist()
    selected_jenis = st.multiselect('Select Jenis DT', unique_jenis, default=unique_jenis)

# Filter the data based on the slicers
filtered_data = df[(df['STATUS DT'].isin(selected_status)) & (df['JENIS DT'].isin(selected_jenis))]

# Button for refreshing data
if st.button('Refresh Data'):
    st.write(filtered_data)
else:
    # Display the filtered data when the app is first run
    st.write(filtered_data)
