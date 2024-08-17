# import module
import streamlit as st

# import pandas as pd

from src import plot,processing_data,connection


#Connection
df_cluster = connection.muat_data_cluster('data/df_cluster.csv')

# MAINPAGE

st.title(':bar_chart: Analysis')
st.markdown('---')

# Section 1
# KPI

total_sales = processing_data.total_sales(df_cluster)

total_transaksi = processing_data.total_transaksi(df_cluster)

total_customer = processing_data.total_customer(df_cluster)

growth_last_month = processing_data.growth_last_month(df_cluster)


if growth_last_month > 0:
    emoji = "⬆️"
elif growth_last_month < 0:
    emoji = "⬇️"
else:
    emoji = "➖"

col1,col2,col3,col4= st.columns(4)
with col1:
    with st.container(border=True):
        st.markdown('**Total Sales**')
        st.markdown(f'$ {total_sales}')
with col2:
    with st.container(border=True):
        st.markdown('**Total Transaction**')
        st.markdown(f'{total_transaksi}')
with col3:
    with st.container(border=True):
        st.markdown('**Total Customer**')
        st.markdown(f'{total_customer}')
with col4:
    with st.container(border=True):
        st.markdown('**Profit Growth Per Month**')
        st.markdown(f' {growth_last_month}% {emoji}')

st.markdown("---")


# --section 2
# Sales growth per month
df_total_sales_per_month = processing_data.total_sales_per_month(df_cluster)

# Growth new customer per month
df_growth_new_customer = processing_data.growth_new_customer(df_cluster)


col1,col2 = st.columns(2)
with col1:
    with st.container(border=True):
        plot.plot_line_growth_sales_per_month(df_total_sales_per_month)
with col2:
    with st.container(border=True):
        plot.plot_line_growth_newcustomer_per_month(df_growth_new_customer)

st.markdown("---")


# --Section 3
# Mapping Demographic Total Sales

df_profit_per_country = processing_data.profit_per_country(df_cluster)


with st.container():
    st.markdown("**Peta Demografis Penjualan**")
    col1,col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            year = st.multiselect(
                "select year",
                options=df_profit_per_country['Year'].unique(),
                default=df_profit_per_country['Year'].unique()
                )
            
            df_profit_per_country = df_profit_per_country.query("Year == @year")
    with col2:
        with st.container(border=True):
            month = st.multiselect(
                "select month",
                options=df_profit_per_country['NameMonth'].unique(),
                default=df_profit_per_country['NameMonth'].unique()
                )
            df_profit_per_country = df_profit_per_country.query("NameMonth == @month")


plot.plot_mapping_profit_by_country(df_profit_per_country)

# --Section 4

plot.plot_show_tabular_data(df_cluster)