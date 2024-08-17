import pandas as pd
import streamlit as st

@st.cache_data
def muat_data_cluster(path='data/df_cluster.csv'):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        st.error("File data tidak ditemukan")
        return pd.DataFrame()

@st.cache_data
def muat_data_RFM(path='data/data_RFM.csv'):
    try:
        df_RFM = pd.read_csv(path)
        df_RFM['CustomerID'] = df_RFM['CustomerID'].astype(str)
        return df_RFM
    except FileNotFoundError:
        st.error(f"File data tidak ditemukan: {path}")
        return pd.DataFrame()
