import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
    df['TAHUN DT'] = df['TAHUN DT'].fillna(0).astype(int)  # Option 1: Fill with 0

    return df

# Tentukan lokasi logo perusahaan Anda
logo_path = "atiga.png"

# Menggunakan kolom untuk menyesuaikan tata letak
col1, col2 = st.columns([3, 1])  # Sesuaikan rasio sesuai kebutuhan

with col1:
    st.write("tes")  # Isi dengan konten atau biarkan kosong

with col2:
    st.image(logo_path, width=150)  # Sesuaikan lebar sesuai kebutuhan

# Display data in Streamlit
st.title('Dashboard Visualisasi Data')

# Set theme colors
primaryColor="#E694FF"
backgroundColor="#00172B"
secondaryBackgroundColor="#0083B8"
textColor="#FFFFFF"
font="sans serif"

# Apply theme colors
st.markdown(
    f"""
    <style>
    .reportview-container .main .block-container{{
        color: {textColor};
        background-color: {backgroundColor};
    }}
    .reportview-container .main {{
        color: {textColor};
        background-color: {backgroundColor};
    }}
    </style>
    """,
    unsafe_allow_html=True

# Load the data
# df = get_data()

# Visualization for "STATUS DT"
status_counts = df['STATUS DT'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Distribusi Status DT')

# Display the pie chart in Streamlit
st.pyplot(fig1)

# Visualization for "JENIS DT" vs "STATUS DT"
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='JENIS DT', hue='STATUS DT', ax=ax2)
ax2.set_title('Hubungan antara Jenis dan Status DT')
ax2.set_xlabel('Jenis DT')
ax2.set_ylabel('Jumlah')
ax2.legend(title='Status DT')

# Display the second plot in Streamlit
st.pyplot(fig2)

# Sidebar for the slicers
# with st.sidebar:
#     # Date picker
#     start_date = date(2024, 1, 1)
#     end_date = date(2024, 12, 31)
    
#     selected_date = st.date_input("Select date", [start_date, end_date], min_value=start_date, max_value=end_date)

#     # Handle single and range of dates input
#     if isinstance(selected_date, list):
#         # Unpack range of dates
#         selected_start_date, selected_end_date = selected_date
#         st.write("Selected Start Date:", selected_start_date.strftime("%d-%m-%Y"))
#         st.write("Selected End Date:", selected_end_date.strftime("%d-%m-%Y"))
#     else:
#         # Handle single date input
#         selected_start_date = selected_end_date = selected_date
#         st.write("Selected Date:", selected_start_date.strftime("%d-%m-%Y"))
    
#     # Slicer for "Status DT"
#     unique_status = df['STATUS DT'].unique().tolist()
#     selected_status = st.multiselect('Select Status DT', unique_status, default=unique_status)
    
#     # Slicer for "Jenis DT"
#     unique_jenis = df['JENIS DT'].unique().tolist()
#     selected_jenis = st.multiselect('Select Jenis DT', unique_jenis, default=unique_jenis)

# # Filter the data based on the slicers
# filtered_data = df[(df['STATUS DT'].isin(selected_status)) & (df['JENIS DT'].isin(selected_jenis))]

# # Button for refreshing data
# if st.button('Refresh Data'):
#     st.write(filtered_data)
# else:
#     # Display the filtered data when the app is first run
#     st.write(filtered_data)

# # Sidebar for the slicers
# with st.sidebar:
#     # Date picker
#     start_date = date(2024, 1, 1)
#     end_date = date(2024, 12, 31)
    
#     # Date input yang memungkinkan pemilihan satu tanggal atau rentang tanggal
#     selected_date = st.date_input("Pilih tanggal atau rentang tanggal", [start_date, end_date], min_value=start_date, max_value=end_date)

#     # Cek tipe data dari 'selected_date' untuk mengetahui apakah satu atau dua tanggal yang dipilih
#     if isinstance(selected_date, list):
#         # Pengguna memilih rentang tanggal
#         selected_start_date, selected_end_date = selected_date
#         st.write("Tanggal Mulai Terpilih:", selected_start_date.strftime("%d-%m-%Y"))
#         st.write("Tanggal Akhir Terpilih:", selected_end_date.strftime("%d-%m-%Y"))
#     else:
#         # Pengguna hanya memilih satu tanggal
#         selected_start_date = selected_end_date = selected_date
#         st.write("Tanggal Terpilih:", selected_start_date.strftime("%d-%m-%Y"))
    
#     # Slicer untuk "Status DT"
#     unique_status = df['STATUS DT'].unique().tolist()
#     selected_status = st.multiselect('Pilih Status DT', unique_status, default=unique_status)
    
#     # Slicer untuk "Jenis DT"
#     unique_jenis = df['JENIS DT'].unique().tolist()
#     selected_jenis = st.multiselect('Pilih Jenis DT', unique_jenis, default=unique_jenis)

# # Filter data berdasarkan slicers
# filtered_data = df[(df['STATUS DT'].isin(selected_status)) & (df['JENIS DT'].isin(selected_jenis)) & (df['TAHUN DT'] >= selected_start_date.year) & (df['TAHUN DT'] <= selected_end_date.year)]

# # Tombol untuk menyegarkan data
# if st.button('Segarkan Data'):
#     st.write(filtered_data)
# else:
#     # Tampilkan data terfilter ketika aplikasi pertama kali dijalankan
#     st.write(filtered_data)
