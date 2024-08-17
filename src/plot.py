import plotly.express as px
import streamlit as st
import plotly.graph_objects as go


from src import recomender

# Sales growth per month
def plot_line_growth_sales_per_month(df):
    fig_total_profit = px.line(
        df, 
        x='Month', 
        y='TotalProfit', 
        title='Total Profit per Month',
        markers=True,
        height=300
    )

    st.plotly_chart(fig_total_profit, use_container_width=True)

def plot_line_growth_newcustomer_per_month(df):

    fig_new_customers = px.line(
        df,
        x='YearMonth',
        y='NumNewCustomer',
        title='Trend Growth of New Customers',
        markers=True,
        labels={'YearMonth': 'Year-Month', 'NumNewCustomer': 'Number of New Customers'}, height=300
    )

    st.plotly_chart(fig_new_customers,use_container_width=True)


def plot_mapping_profit_by_country(df):
    fig_total_sales_demographic = px.choropleth(df,
                        locations="Country",
                        locationmode='country names',
                        color="Profit",
                        hover_name="Country",width=750,height=600,
                        color_continuous_scale=px.colors.sequential.Reds)
    fig_total_sales_demographic.update_layout(
        geo=dict(
            projection_scale=1.5,  # Adjust this value to zoom in or out
            center=dict(lat=0, lon=0),  # Center the map
            projection=dict(type="equirectangular")  # You can try other types like "mercator"
        )
    )

    st.plotly_chart(fig_total_sales_demographic, use_container_width=True)


    
def plot_show_tabular_data(df):
    with st.expander("Tabular"):
        showData=st.multiselect('Filter : ', df.columns,default=[])
        st.write(df[showData])






# --- PAGE RFM ANALYSiS ---

def tabel_rfm(df):
    with st.expander("Tabular"):
        showData=st.multiselect('Filter : ', df.columns,default=[])
        st.write(df[showData])


def table_cluster_character(df):
    st.markdown('**characteristic cluster**')
    st.table(df)

def plot_segmentation_cluster_monetary_vs_frequency(df):
    st.markdown('**Monetary VS Frecuency**')
    fig_scatter = px.scatter(df, x='Monetary', y='Frequency', color='cluster', 
                            title='Customer Segments Based on Monetary Value and Frequency', 
                            labels={'Monetary': 'Monetary Value ($)', 'Frequency': 'Frequency'},
                            color_discrete_map={
                                "Platinum": "#e5e4e2",
                                "Gold": "#FFD700",
                                "Silver": "#C0C0C0",
                                "Bronze": "#CD7F32"},
                            size_max=100)

    # Update layout
    fig_scatter.update_layout(title_x=0.5)
    # Menampilkan scatter plot di Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)

def plot_3d_cluster(df):
    st.markdown('**3D Scatter Plot of Customer Segments**')
    fig_3d_cluster = px.scatter_3d(df, x='Recency', y='Frequency', z='Monetary', color='cluster', 
                        labels={'Recency': 'Recency (days)', 'Frequency': 'Frequency', 'Monetary': 'Monetary Value'},
                        opacity=0.8,
                        color_discrete_map={
                            "Platinum": "#e5e4e2",
                            "Gold": "#FFD700",
                            "Silver": "#C0C0C0",
                            "Bronze": "#CD7F32"})
    # fig_3d_cluster.update_layout(height=400)
    st.plotly_chart(fig_3d_cluster, use_container_width=True)


def insight():
        st.write('''
            1. Cluster Silver: Pelanggan Baru atau Kurang Aktif
    - Karakteristik

        - Recency (43.87): Rata-rata pelanggan terakhir kali bertransaksi sekitar 44 hari yang lalu. Ini menunjukkan bahwa mereka masih relatif baru atau mungkin baru kembali bertransaksi setelah periode ketidakaktifan.
        - Frequency (3.66): Rata-rata pelanggan dalam cluster ini bertransaksi sekitar 3-4 kali. Ini menunjukkan bahwa mereka belum terlalu sering bertransaksi.
        - Monetary (1345.42): Rata-rata pengeluaran pelanggan di cluster ini adalah sekitar 1345.42. Ini menunjukkan bahwa meskipun frekuensi transaksi rendah, jumlah yang dibelanjakan cukup signifikan.
        
    - Strategi
        - Promosi dan Diskon Awal:
            - Berikan diskon khusus atau promosi kepada pelanggan baru atau yang kembali setelah lama tidak aktif untuk mendorong transaksi lebih lanjut.
            - Contoh: "Diskon 20% untuk pembelian berikutnya" atau "Beli 2, gratis 1".
        - Email Marketing dan Rekomendasi Produk:
            - Kirim email yang berisi rekomendasi produk berdasarkan pembelian sebelumnya atau produk populer.
            - Contoh: "Anda mungkin menyukai produk ini..." atau "Produk terlaris minggu ini".
        - Program Loyalitas:
            - Mulai memperkenalkan program loyalitas yang memberikan poin atau hadiah untuk setiap pembelian.
            - Contoh: "Dapatkan poin setiap pembelian yang bisa ditukar dengan diskon atau hadiah".
        
        
    2. Cluster Gold: Pelanggan Setia dengan Pembelanjaan Tinggi
    - Karakteristik
        - Recency (15.64): Rata-rata pelanggan terakhir kali bertransaksi sekitar 16 hari yang lalu. Mereka sering bertransaksi.
        - Frequency (22.09): Rata-rata pelanggan dalam cluster ini bertransaksi sekitar 22 kali. Ini menunjukkan loyalitas yang tinggi.
        - Monetary (12463.81): Rata-rata pengeluaran pelanggan di cluster ini adalah sekitar 12463.81. Mereka menghabiskan banyak uang dan merupakan pelanggan bernilai tinggi.    

    - Strategi untuk Meningkatkan Profit
        - Program Penghargaan dan Loyalitas:

            - Tingkatkan program loyalitas dengan memberikan penghargaan eksklusif atau keuntungan tambahan.
            - Contoh: "Akses eksklusif ke penjualan awal" atau "Bonus poin ganda di bulan ulang tahun".
        - Penawaran Produk Premium:

            - Tawarkan produk premium atau bundling dengan harga spesial yang bisa meningkatkan nilai transaksi.
            - Contoh: "Bundle eksklusif dengan diskon 10%" atau "Produk premium terbaru".
        - Umpan Balik dan Personalisasi:

            - Minta umpan balik untuk meningkatkan layanan dan sesuaikan penawaran berdasarkan preferensi individu.
            - Contoh: "Kami ingin mendengar pendapat Anda..." atau "Rekomendasi produk khusus untuk Anda".
        
    3. Cluster Platinum: Pelanggan Paling Berharga (VIP)
    - Karakteristik
        - Recency (7.38): Rata-rata pelanggan terakhir kali bertransaksi sekitar 7 hari yang lalu. Mereka sangat sering bertransaksi.
        - Frequency (82.69): Rata-rata pelanggan dalam cluster ini bertransaksi sekitar 83 kali. Ini menunjukkan frekuensi yang sangat tinggi.
        - Monetary (127187.96): Rata-rata pengeluaran pelanggan di cluster ini adalah sekitar 127187.96. Mereka adalah pelanggan yang paling bernilai tinggi.
    - Strategi untuk Meningkatkan Profit
        - Layanan dan Pengalaman Eksklusif:

            - Berikan layanan khusus seperti personal shopper atau akses VIP ke acara eksklusif.
            - Contoh: "Akses VIP ke peluncuran produk" atau "Layanan personal shopper gratis".
        - Penawaran Produk Terbatas:

            - Tawarkan produk edisi terbatas atau koleksi khusus yang tidak tersedia untuk pelanggan lain.
            - Contoh: "Edisi terbatas hanya untuk anggota VIP" atau "Koleksi eksklusif terbaru".
        - Program VIP:

            - Kembangkan program VIP dengan keuntungan lebih seperti pengiriman gratis, hadiah ulang tahun, atau diskon khusus.
            - Contoh: "Pengiriman gratis untuk semua pesanan" atau "Hadiah ulang tahun eksklusif".
        
        
    4. Cluster Bronze: Pelanggan Tidak Aktif atau Berisiko Churn
    - Karakteristik
        - Recency (248.47): Rata-rata pelanggan terakhir kali bertransaksi sekitar 248 hari yang lalu. Mereka sudah lama tidak bertransaksi.
        - Frequency (1.55): Rata-rata pelanggan dalam cluster ini bertransaksi sekitar 1-2 kali. Ini menunjukkan frekuensi transaksi yang sangat rendah.
        - Monetary (478.65): Rata-rata pengeluaran pelanggan di cluster ini adalah sekitar 478.65. Mereka menghabiskan sedikit uang dibandingkan dengan cluster lainnya.

    - Strategi untuk Meningkatkan Profit
        - Kampanye Reaktivasi:

            - Kirim kampanye reaktivasi dengan penawaran khusus untuk menarik mereka kembali.
            - Contoh: "Diskon 30% untuk kembali berbelanja" atau "Hadiah gratis dengan pembelian pertama Anda setelah lama tidak aktif".
        - Survey Kepuasan Pelanggan:

            - Lakukan survey untuk memahami alasan ketidakaktifan dan tawarkan solusi atau penawaran yang relevan.
            - Contoh: "Apa yang bisa kami perbaiki?" atau "Diskon 20% sebagai ucapan terima kasih atas umpan balik Anda".
        - Follow-Up Personal:

            - Lakukan follow-up personal melalui email atau telepon untuk mengetahui kebutuhan mereka dan menawarkan bantuan.
            - Contoh: "Kami merindukan Anda! Ada yang bisa kami bantu?" atau "Diskon khusus untuk menyambut Anda kembali".
        ''')


def plot_num_customer_segment(df):
    # Menghitung jumlah pelanggan per Recency dan SegmentRecency
    line_chart_data = df.groupby(['Recency', 'SegmentRecency']).size().reset_index(name='CustomerCount')

    # Menghitung jumlah total pelanggan per SegmentRecency
    total_segments = df['SegmentRecency'].value_counts().to_dict()

    # Membuat line chart menggunakan Plotly
    fig = px.line(line_chart_data, x='Recency', y='CustomerCount', color='SegmentRecency', title='Customer Segments Based on Recency',color_discrete_sequence=px.colors.sequential.Turbo)

    # Menambahkan garis vertikal untuk membedakan setiap segment recency
    fig.add_vline(x=30, line=dict(color='grey', dash='dash'))
    fig.add_vline(x=90, line=dict(color='grey', dash='dash'))
    fig.add_vline(x=180, line=dict(color='grey', dash='dash'))
    fig.add_vline(x=line_chart_data['Recency'].max(), line=dict(color='grey', dash='dash'))

    # Menambahkan anotasi jarak garis untuk setiap segmen
    fig.add_annotation(x=15, y=max(line_chart_data['CustomerCount']) * 0.8, text='< 30 days', showarrow=False, font=dict(color='black', size=10))
    fig.add_annotation(x=60, y=max(line_chart_data['CustomerCount']) * 0.8, text='30 - 90 days', showarrow=False, font=dict(color='black', size=10))
    fig.add_annotation(x=135, y=max(line_chart_data['CustomerCount']) * 0.8, text='90 - 180 days', showarrow=False, font=dict(color='black', size=10))
    fig.add_annotation(x=250, y=max(line_chart_data['CustomerCount']) * 0.8, text='> 180 days', showarrow=False, font=dict(color='black', size=10))

    # Menambahkan anotasi jumlah total pelanggan untuk setiap segment recency dengan border
    fig.add_annotation(x=5, y=max(line_chart_data['CustomerCount']) * 1.1, text=f'Active: {total_segments.get("Active", 0)}', showarrow=False, font=dict(color='black', size=10), bgcolor='white', opacity=1, bordercolor='black', borderwidth=1)
    fig.add_annotation(x=60, y=max(line_chart_data['CustomerCount']) * 1.1, text=f'Warm: {total_segments.get("Warm", 0)}', showarrow=False, font=dict(color='black', size=10), bgcolor='white', opacity=1, bordercolor='black', borderwidth=1)
    fig.add_annotation(x=135, y=max(line_chart_data['CustomerCount']) * 1.1, text=f'Cool: {total_segments.get("Cool", 0)}', showarrow=False, font=dict(color='black', size=10), bgcolor='white', opacity=1, bordercolor='black', borderwidth=1)
    fig.add_annotation(x=250, y=max(line_chart_data['CustomerCount']) * 1.1, text=f'Inactive: {total_segments.get("Inactive", 0)}', showarrow=False, font=dict(color='black', size=10), bgcolor='white', opacity=1, bordercolor='black', borderwidth=1)

    fig.update_layout(
        xaxis_title='Recency (days)',
        yaxis_title='Number of Customers',
        legend_title='Segment Recency',
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)


def plot_bar_monetary_per_cluster(df):
    # Membuat bar chart menggunakan Plotly
    fig_bar = px.bar(df, 
                     x='Monetary', 
                     y='cluster',
                     color='cluster',
                     labels={'cluster': 'cluster', 'Monetary': 'Monetary Value ($)'},
                     color_discrete_map={
                "Platinum": "#e5e4e2",
                "Gold": "#FFD700",
                "Silver": "#C0C0C0",
                "Bronze": "#CD7F32"})

    st.plotly_chart(fig_bar, use_container_width=True)



def plot_bar_monetary_per_segment_recency(df):
    # Membuat bar chart menggunakan Plotly
    fig_bar = px.bar(df, 
                     x='Monetary', 
                     y='SegmentRecency', 
                     color='SegmentRecency',
                     labels={'SegmentRecency': 'Segment Recency', 'Monetary': 'Monetary Value ($)'},
                     color_discrete_sequence=px.colors.sequential.Turbo)

    # Update layout
    fig_bar.update_layout( yaxis={'categoryorder':'total ascending'})

    # Menampilkan bar chart di Streamlit
    st.plotly_chart(fig_bar, use_container_width=True)




def plot_heatmap_segmon_vs_segrec(df):
    # Plot heatmap menggunakan Plotly
    fig_heatmap = px.imshow(df, 
                            labels=dict(x="Recency Segment", y="Monetary Segment", color="Percentage"),
                            x=df.columns,
                            y=df.index,
                            color_continuous_scale='Mint')

    # Update layout dan menambahkan template teks untuk menampilkan persentase
    fig_heatmap.update_layout(
        annotations=[
            dict(
                x=col,
                y=row,
                text=f"%{df.loc[row, col]:.2f}",
                showarrow=False,
                font=dict(color='black')
            )
            for row in df.index
            for col in df.columns
        ]
    )



    # Menampilkan heatmap di Streamlit
    st.plotly_chart(fig_heatmap, use_container_width=True)



@st.cache_data
def plot_radar_habbit_hourly_cluster(df):

    fig = px.line_polar(df, r='transaction', theta='Hour', color='cluster', line_close=True, height=400,width=400,
                     color_discrete_map={
                "Platinum": "#e5e4e2",
                "Gold": "#FFD700",
                "Silver": "#C0C0C0",
                "Bronze": "#CD7F32"})
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,  # Atur nilai ini untuk menyesuaikan posisi vertikal
            xanchor="center",
            x=0.5,
            font=dict(size=10),  # Ukuran font legenda
            bordercolor="LightGray",
            borderwidth=1,
            bgcolor="rgba(255, 255, 255, 0)"  # Transparansi latar belakang
            
        )
    )

    st.plotly_chart(fig, use_container_width=True)

@st.cache_data
def plot_radar_habbit_nameday_cluster(df):

    fig = px.line_polar(df,r='transaction', theta='Dayname', color='cluster', line_close=True, height=400,width=400,
                    hover_data=['transaction'],
                    color_discrete_map={
                "Platinum": "#e5e4e2",
                "Gold": "#FFD700",
                "Silver": "#C0C0C0",
                "Bronze": "#CD7F32"})
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,  # Atur nilai ini untuk menyesuaikan posisi vertikal
            xanchor="center",
            x=0.5,
            font=dict(size=10),  # Ukuran font legenda
            bordercolor="LightGray",
            borderwidth=1,
            bgcolor="rgba(255, 255, 255, 0)"  # Transparansi latar belakang
        )
    )
    st.plotly_chart(fig,use_container_width=True)

@st.cache_data
def plot_radar_habbit_dayly_cluster(df):


    fig = px.line_polar(df,r='transaction', theta='Day', color='cluster', line_close=True, height=400,width=400,
                    hover_data=['transaction'],
                    color_discrete_map={
                "Platinum": "#e5e4e2",
                "Gold": "#FFD700",
                "Silver": "#C0C0C0",
                "Bronze": "#CD7F32"})
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,  # Atur nilai ini untuk menyesuaikan posisi vertikal
            xanchor="center",
            x=0.5,
            font=dict(size=10),  # Ukuran font legenda
            bordercolor="LightGray",
            borderwidth=1,
            bgcolor="rgba(255, 255, 255, 0)"  # Transparansi latar belakang
        )
    )
    
    st.plotly_chart(fig,use_container_width=True)

@st.cache_data
def plot_radar_habbit_monthly_cluster(df):
    

    fig = px.line_polar(df,r='transaction', theta='NameMonth', color='cluster', line_close=True, height=400,width=400,
                    hover_data=['transaction'],
                    color_discrete_map={
                "Platinum": "#e5e4e2",
                "Gold": "#FFD700",
                "Silver": "#C0C0C0",
                "Bronze": "#CD7F32"})
    
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,  # Atur nilai ini untuk menyesuaikan posisi vertikal
            xanchor="center",
            x=0.5,
            font=dict(size=10),  # Ukuran font legenda
            bordercolor="LightGray",
            borderwidth=1,
            bgcolor="rgba(255, 255, 255, 0)"  # Transparansi latar belakang
        )
    )
    
    st.plotly_chart(fig,use_container_width=True)

def radar_insight_text(selected_clusters):
    for cluster in selected_clusters:
        if cluster == 'Silver':
            st.write('''
                ### Analisis Klaster Silver
                1. **Analisis hourly transaction habits**
                - Puncak Aktivitas: Jam 12:00-14:00.
                - Strategi: Luncurkan promosi spesial pada jam-jam ini untuk memanfaatkan puncak transaksi.

                2. **Analisis days transaction habits**
                - Puncak Aktivitas: banyak transaksi hari Kamis.
                - Strategi: Luncurkan promosi spesial pada hari ini untuk memanfaatkan puncak transaksi.

                3. **Analisis date transaction habits**
                - Puncak Aktivitas: Konsisten tinggi dengan beberapa puncak pada tanggal 5, 8, 15, dan 20.
                - Strategi: Luncurkan promosi spesial dan kampanye penjualan pada tanggal-tanggal ini untuk memanfaatkan puncak transaksi.

                4. **Analisis month transaction habits**
                - Puncak Aktivitas: Oktober dan November.
                - Strategi: Rencanakan promosi besar dan kampanye produk pada bulan-bulan ini.
            ''')

        elif cluster == 'Gold':
            st.write('''
                ### Analisis Klaster Gold
                1. **Analisis hourly transaction habits**
                - Aktivitas: Stabil sepanjang hari, dengan sedikit peningkatan antara jam 9:00-14:00.
                - Strategi: Fokuskan upaya pemasaran pada jam-jam ini untuk meningkatkan visibilitas.

                2. **Analisis days transaction habits**
                - Puncak Aktivitas: banyak transaksi hari Kamis.
                - Strategi: Fokuskan upaya pemasaran pada hari ini untuk meningkatkan visibilitas.

                3. **Analisis date transaction habits**
                - Aktivitas: Stabil dengan beberapa puncak pada tanggal 1, 14, dan 22.
                - Strategi: Fokuskan upaya pemasaran dan penawaran spesial pada tanggal-tanggal ini untuk meningkatkan transaksi.

                4. **Analisis month transaction habits**
                - Puncak Aktivitas: Stabil sepanjang tahun, puncak di Desember.
                - Strategi: Pertahankan strategi yang konsisten dan tingkatkan promosi di bulan dengan transaksi rendah.
            ''')

        elif cluster == 'Platinum':
            st.write('''
                ### Analisis Klaster Platinum
                1. **Analisis hourly transaction habits**
                - Aktivitas: Sangat rendah sepanjang hari, sedikit puncak pada jam 12:00-13:00.
                - Strategi: Tingkatkan kampanye pemasaran untuk meningkatkan partisipasi sepanjang hari.

                2. **Analisis days transaction habits**
                - Puncak Aktivitas: banyak transaksi di hari Kamis.
                - Strategi: Tingkatkan kampanye pemasaran untuk meningkatkan partisipasi sepanjang hari.

                3. **Analisis date transaction habits**
                - Aktivitas: Sangat rendah, dengan sedikit peningkatan pada tanggal 5 dan 20.
                - Strategi: Tingkatkan kampanye pemasaran pada tanggal-tanggal ini untuk meningkatkan partisipasi dan transaksi.

                4. **Analisis month transaction habits**
                - Puncak Aktivitas: Rendah sepanjang tahun, puncak di September.
                - Strategi: Fokuskan pemasaran dan inovasi produk untuk meningkatkan transaksi sepanjang tahun.
            ''')

        elif cluster == 'Bronze':
            st.write('''
                ### Analisis Klaster Bronze
                1. **Analisis hourly transaction habits**
                - Aktivitas: Stabil dengan sedikit peningkatan antara jam 10:00-13:00.
                - Strategi: Pertahankan upaya pemasaran yang konsisten, khususnya selama jam-jam aktif.

                2. **Analisis days transaction habits**
                - Puncak Aktivitas: banyak transaksi hari Kamis.
                - Strategi: Pertahankan upaya pemasaran yang konsisten, khususnya selama jam-jam aktif.

                3. **Analisis date transaction habits**
                - Aktivitas: Rendah dengan beberapa puncak pada tanggal 1 dan 31.
                - Strategi: Pertahankan upaya pemasaran yang konsisten, khususnya pada tanggal-tanggal ini untuk memaksimalkan transaksi.

                4. **Analisis month transaction habits**
                - Puncak Aktivitas: Variatif, puncak di Januari dan Desember.
                - Strategi: Tingkatkan keterlibatan dan promosikan produk secara agresif selama bulan dengan aktivitas tinggi.
            ''')


def display_filters(df):
    col1, col2 = st.columns(2)
    with col1:
        cluster = st.selectbox(
            "Pilih Cluster",
            options=df['cluster'].unique()
        )
        df_filtered = df.query("cluster == @cluster")

    with col2:
        customer_id = st.selectbox(
            "Pilih Customer ID",
            options=df_filtered['CustomerID'].unique()
        )
        df_filtered = df_filtered.query("CustomerID == @customer_id")
    
    return df_filtered, cluster


def display_tables(df_filtered):
    df_filter_sorted_invoice = df_filtered.sort_values(by='InvoiceDate', ascending=False)
    df_filter_sorted_quantity = df_filtered.sort_values(by='Quantity', ascending=False)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("#### Tabel Data Pembelian Produk Pelanggan Terbaru ####")
            with st.expander("Lihat Tabel"):
                with st.container(border=True, height=300):
                    st.table(df_filter_sorted_invoice[['CustomerID', 'StockCode', 'Description','InvoiceDate']].drop_duplicates())

    with col2:
        with st.container(border=True):
            st.markdown("#### Tabel Data Pembelian Produk Berdasarkan Jumlah Quantity ####")
            with st.expander("Lihat Tabel"):
                with st.container(border=True, height=300):
                    st.table(df_filter_sorted_quantity[['CustomerID', 'StockCode', 'Description', 'Quantity']].drop_duplicates())



# def plot_display_filters_and_table(df):
#     col1, col2 = st.columns(2)
#     with col1:
#         cluster = st.selectbox(
#             "Pilih Cluster",
#             options=df['cluster'].unique()
#         )
        
        
#         df = df.query("cluster == @cluster")

#     with col2:
#         customer_id = st.selectbox(
#             "Pilih Customer ID",
#             options=df['CustomerID'].unique()
#         )

#         df = df.query("CustomerID == @customer_id")
    

    
#     df_filtered = df.query("cluster == @cluster and CustomerID == @customer_id")
#     df_filter_sorted_invoice = df_filtered.sort_values(by='InvoiceDate', ascending=False)
#     df_filter_sorted_quantity = df_filtered.sort_values(by='Quantity', ascending=False)
    
#     col1,col2 = st.columns(2)
#     with col1:
#         with st.container(border=True):
#             st.markdown("#### Tabel Data Pembelian Produk Pelanggan terbaru ####")
#             with st.expander("See Table"):
#                 with st.container(border=True, height=300):
#                     st.table(df_filter_sorted_invoice[['CustomerID', 'StockCode', 'Description','InvoiceDate']].drop_duplicates())

#     with col2:
#         with st.container(border=True):
#             st.markdown("#### Tabel Data Pembelian Produk berdasarkan jumlah quantity ####")
#             with st.expander("See Table"):
#                 with st.container(border=True, height=300):
#                     st.table(df_filter_sorted_quantity[['CustomerID', 'StockCode', 'Description', 'Quantity']].drop_duplicates())
           



def plot_recommend_product(df_cluster):
    recomen_produk = recomender.RecommenderSystem(df_cluster, 'StockCode', 'Description')
    recomen_produk.fit()

    stockcode = st.text_input(label="Masukkan Stock Code")
    st.markdown("**Produk yang Direkomendasikan**")
    if stockcode:
        try:
            rekomendasi_produk = recomen_produk.recommend(stockcode)
            st.table(rekomendasi_produk.reset_index(drop=True))

            st.markdown("#### Penjelasan dan Saran Strategis")
            



        except ValueError as e:
            st.error(f"Error: {e}")


def plot_recomend_basket_produk(recommendations):
# Visualize the top k recommendations using Plotly
    fig = px.bar(recommendations, x='antecedents', y='confidence', title='Rekomendasi Teratas Berdasarkan Confidence')
    fig.update_layout(xaxis_title='Produk Antecedents', yaxis_title='Confidence')

    st.plotly_chart(fig)

    
     # Provide insights and strategic suggestions
    st.markdown("### Penjelasan dan Rekomendasi")
    for index, row in recommendations.iterrows():
        st.markdown(f"**Jika pelanggan membeli {row['antecedents']}, mereka juga cenderung membeli {row['consequents']}**.")
        st.markdown(f"- **Confidence:** Ini adalah ukuran seberapa sering aturan ini benar. Nilai confidence yang tinggi berarti pelanggan yang membeli produk pertama (antecedent) juga sering membeli produk kedua (consequent). Contoh: Confidence {row['confidence']:.2f} berarti ada {row['confidence']*100:.2f}% kemungkinan pelanggan akan membeli produk kedua jika mereka membeli produk pertama.")
        st.markdown(f"- **Lift:** Ini adalah ukuran seberapa besar peningkatan kemungkinan pembelian produk kedua (consequent) setelah produk pertama (antecedent) dibeli. Nilai lift lebih dari 1 menunjukkan adanya hubungan positif. Contoh: Lift {row['lift']:.2f} berarti pembelian produk kedua {row['lift']:.2f} kali lebih mungkin terjadi jika produk pertama dibeli.")
        st.markdown("**Saran Strategis:** Pertimbangkan untuk menggabungkan produk-produk ini dalam satu paket atau membuat promosi untuk mendorong pembelian bersama.")

def plot_bar_freq_top_product(rekomendasi_basket,recommendations):
     # Display frequency of top products using Plotly
    product_counts = rekomendasi_basket.basket_df[rekomendasi_basket.column_desc].value_counts().head(10)
    fig_product_counts = px.bar(product_counts, x=product_counts.index, y=product_counts.values, title='10 Produk Paling Sering Dibeli')
    fig_product_counts.update_layout(xaxis_title='Produk', yaxis_title='Frekuensi')
    st.plotly_chart(fig_product_counts)


    # Display recommended product packages
    st.markdown("### Rekomendasi Paket Produk")
    for index, row in recommendations.iterrows():
        st.markdown(f"- **Paket Produk:** {row['antecedents']} + {row['consequents']}")
        st.markdown(f"  - Confidence: {row['confidence']:.2f}")
        st.markdown(f"  - Lift: {row['lift']:.2f}")
        st.markdown("  - **Saran:** Coba tawarkan paket ini dengan diskon atau promosi khusus untuk meningkatkan penjualan.")