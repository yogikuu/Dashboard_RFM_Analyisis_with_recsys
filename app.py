import streamlit as st

st.set_page_config(layout="wide")


#  --- Page Setup ---
analysis_page = st.Page(
    page="page/analysis.py",
    title="Analysis",
    icon="📊",  # Chart icon for analysis
    default=True
)

rfm_page = st.Page(
    page="page/rfm_page.py",
    title="RFM Analysis",
    icon="📈"  # Line chart icon for RFM analysis
)

basket_page = st.Page(
    page="page/basket_produk.py",
    title="Basket Analysis Apriori",
    icon="🛒"  # Shopping cart icon for basket analysis
)

recsys_page = st.Page(
    page="page/recsys_contentbase.py",
    title="Recomendation Content Base",
    icon="🔍"  # Magnifying glass icon for recommendation system
)


# --- Navigation setup ---
pg = st.navigation(pages=[analysis_page,rfm_page,basket_page,recsys_page])

pg.run()

