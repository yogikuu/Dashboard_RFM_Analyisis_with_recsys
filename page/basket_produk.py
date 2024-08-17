import streamlit as st

from src import recomender,plot,connection



# connection
df_cluster = connection.muat_data_cluster('data/df_cluster.csv')


st.title('🛒 Basket Analysis Apriori')
st.markdown('---')

# Select country from the dropdown
country = st.selectbox(
    "Select Country",
    options=df_cluster['Country'].unique()
)

if st.button("Generate"):
    # Initialize the recommendation class
    rekomendasi_basket = recomender.RecomendBasketProduk(df_cluster, country, 'Country', 'InvoiceNo', 'Description', 'Quantity')
    # Transform data to one-hot encoding
    rekomendasi_basket.transform_one_hot()
    # Fit the model to find frequent itemsets and association rules
    rekomendasi_basket.fit()
    # Get the top k recommendations
    recommendations = rekomendasi_basket.recommend()

    # Display the recommendations in a table
    st.table(recommendations)

    plot.plot_recomend_basket_produk(recommendations)

    plot.plot_bar_freq_top_product(rekomendasi_basket,recommendations)

