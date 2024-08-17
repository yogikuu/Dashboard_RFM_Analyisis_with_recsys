import pandas as pd
import streamlit as st

from src import plot,processing_data,connection

# Connection

df_RFM = connection.muat_data_RFM('data/data_RFM.csv')
df_cluster = connection.muat_data_cluster('data/df_cluster.csv')


# Title

st.title('📈 RFM Analysis')
st.markdown("---")

# Section 1


plot.tabel_rfm(df_RFM)


st.markdown("---")

# Section 2

df_characteristic_cluster = processing_data.characteristic_cluster(df_RFM)
with st.container(border=True):
    tab1, tab2, tab3 = st.tabs(["Table","Monetary vs frequency","3d Plot"])

    with tab1:
        plot.table_cluster_character(df_characteristic_cluster)
    with tab2:
        plot.plot_segmentation_cluster_monetary_vs_frequency(df_RFM)
    with tab3:
        plot.plot_3d_cluster(df_RFM)

    with st.expander("See Insight"):
        with st.container(border=True, height=300):
            plot.insight()

st.markdown("---")


# Section 3
# Chart Number Segment

plot.plot_num_customer_segment(df_RFM)


st.markdown("---")

# Section 4

df_grup_segmentrec = processing_data.sum_monetary_per_segmentrecency(df_RFM)
df_grup_cluster_monetary = processing_data.sum_monetary_per_cluster(df_RFM)
df_pivot_segmon_vs_segrec = processing_data.pivot_segmonvssegrec_val_mone(df_RFM)

with st.container(border=True):
    tab1, tab2 = st.tabs(["Bar","Heatmap"])
    with tab1:
        col1,col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("**Monetary value per Cluster**")
                plot.plot_bar_monetary_per_cluster(df_grup_cluster_monetary)
        
        with col2:
            with st.container(border=True):
                st.markdown("**Monetary value per Segment Recency**")
                plot.plot_bar_monetary_per_segment_recency(df_grup_segmentrec)
    with tab2:
        with st.container(border=True):
            st.markdown("**heatmap Segment Monetary VS Segment Recency**")
            plot.plot_heatmap_segmon_vs_segrec(df_pivot_segmon_vs_segrec)


st.markdown("---")

# Section 5

cluster = st.multiselect(
        "select cluster",
        options=df_cluster['cluster'].unique(),
        default=df_cluster['cluster'].unique()
        )


df_cluster = df_cluster.query(
            "cluster == @cluster"
        )


with st.container(border=True):
    col1,col2 = st.columns(2)
    with col1:
        
        with st.container(border=True):
            st.markdown("**Habit Hourly**")
            plot.plot_radar_habbit_hourly_cluster(processing_data.hourly_transactions(df_cluster))
        
    with col2:
        with st.container(border=True):
            st.markdown("**Habit Name Day**")
            plot.plot_radar_habbit_nameday_cluster(processing_data.name_day_transaction(df_cluster))


    col1,col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("**Habit daily**")
            plot.plot_radar_habbit_dayly_cluster(processing_data.daily_transaction(df_cluster))
        
    with col2:
        with st.container(border=True):
            st.markdown("**Habit Monthly**")
            plot.plot_radar_habbit_monthly_cluster(processing_data.monthly_transaction(df_cluster))
    
    with st.expander("See Insight"):
        with st.container(border=True, height=300):
            plot.radar_insight_text(cluster)






