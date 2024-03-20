import streamlit as st
import gspread
import pandas as pd

# Inisialisasi client gspread untuk akses spreadsheet publik
gc = gspread.service_account()

# Buka spreadsheet publik dan ambil data dari sheet tertentu
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1u8W2CTCgSSQAFuci59bMmFczQyH3_7ajgCRJJH9CNQE'
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet('combined sheet')
df = pd.DataFrame(worksheet.get_all_records())

# Menampilkan data di Streamlit
st.title('Dashboard Visualisasi Data')
st.write(df)
