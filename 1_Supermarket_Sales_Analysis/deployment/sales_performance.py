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
        return df 

    data = load_data()

    #title
    st.write("<h1 style='text-align: center; '>💲Sales Performance💲</h1>", unsafe_allow_html=True)

    if st.checkbox('show Dataset'):
        st.write(data)
        st.markdown("data yang digunakan adalah `Supermarket Sales` yang dapat diakses melalui [kaggle]('https://www.kaggle.com/aungpyaeap/supermarket-sales')")
        st.write('Dataset information:')
        st.markdown(
            '''
            <table style="border-collapse: collapse; width: 98.2955%; height: 252px;" border="1">
            <tbody>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;"><strong>column</strong></td>
            <td style="width: 85.5491%; height: 18px;"><strong>description</strong></td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Invoice id</td>
            <td style="width: 85.5491%; height: 18px;">Computer generated sales slip invoice identification number</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">City</td>
            <td style="width: 85.5491%; height: 18px;">Location of supercenters</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Customer type</td>
            <td style="width: 85.5491%; height: 18px;">Type of customers, recorded by Members for customers using member card and Normal for without member card.</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Gender</td>
            <td style="width: 85.5491%; height: 18px;">Gender type of customer</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Product line</td>
            <td style="width: 85.5491%; height: 18px;">General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Unit price</td>
            <td style="width: 85.5491%; height: 18px;">Price of each product in $</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Quantity</td>
            <td style="width: 85.5491%; height: 18px;">Number of products purchased by customer</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Total</td>
            <td style="width: 85.5491%; height: 18px;">Total price including tax</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Date</td>
            <td style="width: 85.5491%; height: 18px;">Date of purchase (Record available from January 2019 to March 2019)</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Time</td>
            <td style="width: 85.5491%; height: 18px;">Purchase time (10am to 9pm)</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Payment</td>
            <td style="width: 85.5491%; height: 18px;">Payment used by customer for purchase (3 methods are available &ndash; Cash, Credit card and Ewallet)</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">COGS</td>
            <td style="width: 85.5491%; height: 18px;">Cost of goods sold</td>
            </tr>
            <tr style="height: 18px;">
            <td style="width: 14.4509%; height: 18px;">Gross income</td>
            <td style="width: 85.5491%; height: 18px;">Gross income</td>
            </tr>
            <tr>
            <td style="width: 14.4509%;">Rating</td>
            <td style="width: 85.5491%;">Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)</td>
            </tr>
            </tbody>
            </table>
            <p>&nbsp;</p>
            '''
            ,unsafe_allow_html=True)

    # Data preparation
    data_1 = data.groupby(['Date','City'])['gross income'].aggregate('mean').unstack()
    data_1 = data_1.fillna(0) #replace missing value by 0
    data_1['all city'] = data_1.mean(axis='columns')
    data_1_column = ['all city','Yangon','Mandalay','Naypyitaw']
    data_1 = data_1.reindex(columns=data_1_column)

    # Data Preparation product line
    data_2 = data.groupby(['Product line','City'])['Quantity'].aggregate('sum').unstack()
    data_2['all city'] = data_2.sum(axis='columns')

    # Data preparation Peak Hour
    data_3 = data.groupby(['Time','City'])['Invoice ID'].count().unstack()
    data_3['all city'] = data_3.sum(axis='columns')

    # Data preparation average Rating
    data_5 = data.groupby(['Date','City'])['Rating'].mean().unstack()
    data_5['all city'] = data_5.mean(axis='columns')

    #column 1
    col1, col2,= st.columns(2)
    with col1:
        # radio button
        gross_income_compare = st.selectbox('Pilih salah Satu',('Overall Summary','Comparison'))
        #gross_income_compare = st.checkbox('Comparison')


    # slider pilih tanggal
    start_date = dt.datetime(year=data_1.index[0].year,month=data_1.index[0].month,day=data_1.index[0].day)
    end_date = dt.datetime(year=data_1.index[-1].year,month=data_1.index[-1].month,day=data_1.index[-1].day)
    select_date = st.slider("Pilih Periode",min_value=start_date,value=(start_date,end_date),max_value=end_date) 
    date_selected = data_1.loc[select_date[0]:select_date[1]]

    # title
    st.write("<h2 style='text-align: center; '>Daily Average Gross Income</h2>", unsafe_allow_html=True)

    if gross_income_compare == 'Comparison':
    #if gross_income_compare:
        with col2:
            select_city = st.multiselect('Pilih Kota', data_1.columns[1:4],default=['Yangon','Mandalay'])
        with st.container():
            fig1 = px.line(date_selected,y=select_city)
            st.plotly_chart(fig1,use_container_width=True) 

    else:
        # Select box pilih kota
        with col2:
            select_city = st.selectbox('Pilih Kota', data_1.columns)
        # Plot
        with st.container():
            fig1 = px.area(date_selected,y=select_city)
            st.plotly_chart(fig1,use_container_width=True)
        
        # Column Summary    
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write('### **Lowest**')
            st.write(f'# **${round(date_selected[select_city].min(),4)}**')
        with col2:
            st.write('### **Total Average**')
            st.write(f'# **${round(date_selected[select_city].mean(),4)}**')            
        with col3:
            st.write('### **Highest**')
            st.write(f'# **${round(date_selected[select_city].max(),4)}**') 
        with col4:
            st.write("### **Average Rating**")
            st.write(f'# **{round(data_5.loc[select_date[0]:select_date[1]][select_city].mean(),2)}**')

        with st.expander("Insight 🗒"):
            st.write(f'Pada periode {select_date[0].date()} sampai dengan {select_date[1].date()}, Average Gross Income terbesar dari supermarket di kota **{select_city}** \
            yaitu pada tanggal **{date_selected[select_city].idxmax().date()}** dengan nilai Average Gross Income sebesar **{round(date_selected[select_city].max(),4)}** \
            sementara untuk Average Gross Income terkecil yaitu  pada tanggal **{date_selected[select_city].idxmin().date()}** dengan nilai Average Gross Income sebesar **{round(date_selected[select_city].min(),4)}** \
            dan average rating untuk periode ini yaitu **{round(data_5.loc[select_date[0]:select_date[1]][select_city].mean(),2)}**')

        col4, col5 = st.columns(2)
        with col4:
            st.write("<h2 style='text-align: center; '>Product Line Purchased</h2>", unsafe_allow_html=True)
            fig5 = px.bar(data_2,x=data_2.index,y=select_city)
            st.plotly_chart(fig5,use_container_width=True)
            with st.expander("Insight 🗒"):
                st.write(f'Product Line Purchased paling banya di {select_city} yaitu adalah {data_2[select_city].idxmax()} yaitu sebanyak {data_2[select_city].max()} Unit \
                    sementara itu untuk Purchased paling sedikit adalah {data_2[select_city].idxmin()} yaitu sebanyak {data_2[select_city].min()} Unit. ')
        with col5:
            st.write("<h2 style='text-align: center; '>Peak Hour Transcaction</h2>", unsafe_allow_html=True)
            fig6 = px.bar(data_3, x=data_3.index,y=select_city)
            st.plotly_chart(fig6,use_container_width=True)
            with st.expander("Insight 🗒"):
                st.write(f'Jumlah transaksi terbanyak di {select_city} yaitu pada pukul {data_3[select_city].idxmax()}:00 yaitu sebanyak {data_3[select_city].max()} transaksi \
                    sementara untuk transaksi paling sedikit yaitu pada pukul {data_3[select_city].idxmin()}:00 yaitu sebanyak {data_3[select_city].min()} transaksi ')


                     


    


