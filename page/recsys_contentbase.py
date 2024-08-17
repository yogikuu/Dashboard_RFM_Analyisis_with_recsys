import streamlit as st

from src import plot, processing_data,connection



# connection
df_cluster = connection.muat_data_cluster('data/df_cluster.csv')
df_RFM = connection.muat_data_RFM('data/data_RFM.csv')


# Title
st.title('🔍 Recomendation Content Base ')
st.markdown("---")

# Section 1: Filter and Display Data

df_filter = processing_data.filter_df(df_cluster)

df_filtered,cluster = plot.display_filters(df_filter)

# st.table(df_filtered)


plot.display_tables(df_filtered)

st.markdown("---")

# Section 2: Recommend Products


plot.plot_recommend_product(df_cluster)

df = df_cluster.query(
            "cluster == @cluster"
        )

st.markdown("---")
st.subheader('Transaction Habits')
with st.container(border=True):
    col1,col2 = st.columns(2)
    with col1:
        
        with st.container(border=True):
            st.markdown("**Habit Hourly**")
            plot.plot_radar_habbit_hourly_cluster(processing_data.hourly_transactions(df))
        
    with col2:
        with st.container(border=True):
            st.markdown("**Habit Day**")
            plot.plot_radar_habbit_nameday_cluster(processing_data.name_day_transaction(df))


    col1,col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("**Habit Date**")
            plot.plot_radar_habbit_dayly_cluster(processing_data.daily_transaction(df))
        
    with col2:
        with st.container(border=True):
            st.markdown("**Habit Month**")
            plot.plot_radar_habbit_monthly_cluster(processing_data.monthly_transaction(df))
    
    with st.expander("See Insight"):
        with st.container(border=True, height=300):
            plot.radar_insight_text([cluster])

