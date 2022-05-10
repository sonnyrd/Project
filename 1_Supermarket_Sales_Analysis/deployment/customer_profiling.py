import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px

def app():
    #Data loading
    DATA_URL = ('https://raw.githubusercontent.com/sonnyrd/learning_journal/main/Phase_0/supermarket_sales_clean.csv')

    @st.cache
    def load_data():
        df = pd.read_csv(DATA_URL)
        df['Date'] = pd.to_datetime(df['Date'])
        #df['Time'] = pd.to_datetime(df['Time']).dt.hour
        return df 

    data = load_data()

    #title
    st.write("<h1 style='text-align: center; '>👥Customer Profile👥</h1>", unsafe_allow_html=True)


    # Data preparation
    
    data_1 = data.groupby(['Date','City'])['gross income'].aggregate('mean').unstack()
    data_1 = data_1.fillna(0) #replace missing value by 0
    data_1['all city'] = data_1.mean(axis='columns')
    data_1_column = ['all city','Yangon','Mandalay','Naypyitaw']
    data_1 = data_1.reindex(columns=data_1_column)

    ### select
    select_city = st.selectbox('Select City', data_1.columns)

    # by Gender
    data_4 = data.groupby(['Gender'])[['City']].value_counts().unstack()
    data_4['all city'] = data_4.sum(axis='columns')

    # by Member Type
    data_5 = data.groupby(['Customer type'])[['City']].value_counts().unstack()
    data_5['all city'] = data_5.sum(axis='columns')

    # by Payment Type
    data_6 = data.groupby(['Payment'])[['City']].value_counts().unstack()
    data_6['all city'] = data_6.sum(axis='columns')

    ####### plot
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("<h2 style='text-align: center; '>Gender</h2>", unsafe_allow_html=True)
        fig2 = px.pie(data_4,values=select_city,names=data_4.index)
        st.plotly_chart(fig2,use_container_width=True)
        with st.expander("Insight 🗒"):
             st.write(f'Pengunjung supermarket di {select_city} terdiri dari pengunjung {data_4[select_city].index[0]} sebanyak {data_4[select_city][0]} dan pengunjung {data_4[select_city].index[1]} sebanyak {data_4[select_city][1]}')
    with col2:
        st.write("<h2 style='text-align: center; '>Member Type</h2>", unsafe_allow_html=True)
        fig3 = px.pie(data_5,values=select_city,names=data_5.index)
        st.plotly_chart(fig3,use_container_width=True)
        with st.expander("Insight 🗒"):
             st.write(f'Type member supermarket di {select_city} terdiri dari  {data_5[select_city].index[0]} sebanyak {data_5[select_city][0]} dan  {data_5[select_city].index[1]} sebanyak {data_5[select_city][1]}')
    with col3:
        st.write("<h2 style='text-align: center; '>Payment Type</h2>", unsafe_allow_html=True)
        fig4 = px.pie(data_6,values=select_city,names=data_6.index)
        st.plotly_chart(fig4,use_container_width=True)
        with st.expander("Insight 🗒"):
             st.write(f'Jenis pembayaran di supermarket {select_city} terdiri dari  {data_6[select_city].index[0]} sebanyak {data_6[select_city][0]},{data_6[select_city].index[1]} sebanyak {data_6[select_city][1]} dan {data_6[select_city].index[2]} sebanyak {data_6[select_city][2]}')