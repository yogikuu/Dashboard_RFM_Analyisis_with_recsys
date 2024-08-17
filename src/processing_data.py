import pandas as pd
import calendar
import streamlit as st

# --Page Analysis

## --Section 1
## --KPI

def total_sales(df):    
    total_sales = round(df['Profit'].sum(),2)
    return total_sales

def total_transaksi(df):
    total_transaksi = int(df['InvoiceNo'].nunique())
    return total_transaksi

def total_customer(df):
    total_customer = int(df['CustomerID'].nunique()) 
    return total_customer

def growth_last_month(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    total_sales_per_month=df.groupby(df['InvoiceDate'].dt.to_period('M'))['Profit'].sum().reset_index()
    total_sales_per_month.columns = ['Month', 'TotalProfit']
    total_sales_per_month['SalesGrowth'] = round(total_sales_per_month['TotalProfit'].pct_change() * 100,2)
    growth_last_month = round(total_sales_per_month['SalesGrowth'].iloc[-1],2)
    return growth_last_month

# --Section 2
def total_sales_per_month(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    total_sales_per_month = df.groupby(df['InvoiceDate'].dt.to_period('M'))['Profit'].sum().reset_index()
    total_sales_per_month.columns = ['Month', 'TotalProfit']
    # total_sales_per_month['Month'] = total_sales_per_month['Month'].dt.to_timestamp()  # Mengubah kembali ke timestamp
    total_sales_per_month['SalesGrowth'] = round(total_sales_per_month['TotalProfit'].pct_change() * 100, 2)
    total_sales_per_month['Month'] = total_sales_per_month['Month'].dt.strftime('%Y-%m')  # Baru ubah ke string
    return total_sales_per_month

def growth_new_customer(df):
    df_firstpurchase = df.groupby(['CustomerID'])['InvoiceDate'].min().reset_index(name='FirstPurchaseDate')
    df_firstpurchase['YearMonth'] = df_firstpurchase['FirstPurchaseDate'].dt.to_period('M')
    # df_firstpurchase['YearMonth'] = df_firstpurchase['YearMonth'].dt.to_timestamp()  # Mengubah kembali ke timestamp
    df_new_customer_per_month=df_firstpurchase.groupby(['YearMonth']).size().reset_index(name='NumNewCustomer')
    df_new_customer_per_month['YearMonth'] = df_new_customer_per_month['YearMonth'].dt.strftime('%Y-%m')
    return df_new_customer_per_month


#  --Section 3
def profit_per_country(df):
    df_country_profit =  df.groupby(['Country','Year','NameMonth'])['Profit'].sum().reset_index()
    return df_country_profit





# ---RFM AALYSIS---

def characteristic_cluster(df):
    df_character_rfm = df.groupby(["cluster"])[["Recency","Frequency","Monetary"]].mean()
    return df_character_rfm


def sum_monetary_per_cluster(df):
    aggregated_data = df.groupby(['cluster'])['Monetary'].sum().reset_index()
    aggregated_data = aggregated_data.sort_values(by='Monetary', ascending=False)
    return aggregated_data


def sum_monetary_per_segmentrecency(df):
    aggregated_data = df.groupby(['SegmentRecency'])['Monetary'].sum().reset_index()
    aggregated_data = aggregated_data.sort_values(by='Monetary', ascending=False)
    return aggregated_data


def pivot_segmonvssegrec_val_mone(df):
    # Membuat pivot table
    pivot_table = round(((df.pivot_table(index='SegmentMonetary', columns='SegmentRecency', values='Monetary', aggfunc='sum', fill_value=0) / df['Monetary'].sum()) * 100),2)
    pivot_table = pivot_table[['Active', 'Warm', 'Cool', 'Inactive']]
    return pivot_table




def hourly_transactions(df):
    hourly_transactions = df.groupby(['InvoiceNo', 'cluster', 'Hour']).size().reset_index(name='Transactions').groupby(['cluster', 'Hour'])['Transactions'].count().unstack(fill_value=0)
    all_hours = range(24)
    hourly_transactions = hourly_transactions.reindex(columns=all_hours, fill_value=0)
    hourly_transactions = hourly_transactions.unstack().reset_index(name='transaction')
    
    hourly_transactions['Hour'] = hourly_transactions['Hour'].apply(lambda x: f"-{x}-")
    return hourly_transactions


def name_day_transaction(df):
    name_day_transactions = df.groupby(['InvoiceNo','cluster','Dayname']).size().reset_index(name='Transactions').groupby(['cluster', 'Dayname'])['Transactions'].count().unstack(fill_value=0)
    day_names = list(calendar.day_name)
    name_day_transactions = name_day_transactions.reindex(columns=day_names, fill_value=0)
    name_day_transactions = name_day_transactions.unstack().reset_index(name='transaction')
    return name_day_transactions

def daily_transaction(df):
    daily_transactions = df.groupby(['InvoiceNo','cluster','Day']).size().reset_index(name='Transactions').groupby(['cluster', 'Day'])['Transactions'].count().unstack(fill_value=0)
    
    tanggal_bulan=list(range(1,31))
    daily_transactions = daily_transactions.reindex(columns=tanggal_bulan,fill_value=0)
    daily_transactions = daily_transactions.unstack().reset_index(name='transaction')
    daily_transactions['Day'] = daily_transactions['Day'].apply(lambda x: f"-{x}-")
    return daily_transactions

def monthly_transaction(df):
    monthly_transactions = df.groupby(['InvoiceNo','cluster','NameMonth']).size().reset_index(name='Transactions').groupby(['cluster', 'NameMonth'])['Transactions'].count().unstack(fill_value=0)
    month_names = list(calendar.month_name)[1:]
    monthly_transactions = monthly_transactions.reindex(columns=month_names, fill_value=0)
    monthly_transactions = monthly_transactions.unstack().reset_index(name='transaction')
    return monthly_transactions



# --- recsys content bas page---
def filter_df(df):
    df_filter = df[['InvoiceNo','InvoiceDate','CustomerID','StockCode','Description','cluster',"Quantity"]]
    df_filter = df_filter.groupby(['InvoiceDate','CustomerID','StockCode','Description','cluster'])["Quantity"].sum().reset_index()
    return df_filter