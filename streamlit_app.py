import streamlit as st
import gspread
import pandas as pd

# Function to get data from Google Spreadsheet
def get_data():
    # Open the public spreadsheet
    gc = gspread.Client()
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1u8W2CTCgSSQAFuci59bMmFczQyH3_7ajgCRJJH9CNQE')
    worksheet = sh.worksheet('Combined Sheet')
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
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
