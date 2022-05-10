import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import plotly.express as px
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    #Data loading
    DATA_URL = ('https://raw.githubusercontent.com/sonnyrd/learning_journal/main/Phase_0/supermarket_sales_clean.csv')

    @st.cache
    def load_data():
        df = pd.read_csv(DATA_URL)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Time'] = pd.to_datetime(df['Time']).dt.hour
        return df 

    data = load_data()

    #Prepare Data for anova
    data_1 = data.groupby(['Date','City'])['gross income'].aggregate('mean').unstack()
    data_1 = data_1.fillna(0)

    #prepare Data Pie
    data_2 = data.groupby(['City'])[['gross income']].mean()

    #title
    st.write("<h1 style='text-align: center; '>🔎Hypothesis Testing🔍</h1>", unsafe_allow_html=True)
    st.write("Pada bagian ini akan dilakukan uji hipotesis untuk mencari tahu apakah terdapat atau tidak terdapat perbedaan average daily gross income diantara supermarket di kota Mandalay, Naypyitaw dan Yangon. untuk itu dilakukanlah uji hipotesis, pengujian yang dilakukan adalah dengan menggunakan Anova Test..")

    if st.checkbox('show data'): 
        col1,col2 = st.columns([1,1])
        with col1:
            st.write('Average Daily Gross Income')
            fig1 = px.pie(data_2,values='gross income',names=data_2.index)
            st.plotly_chart(fig1)
        with col2:
            st.write('Average Daily Gross Income DataFrame')
            st.write(data_1)

    st.write("<h2 style='text-align: center; '>Anova</h2>", unsafe_allow_html=True)

    st.write("Hipotesis :  \n H0: μ Mandalay = μ Naypyitaw = μ Yangon  \n H0: μ Mandalay != μ Naypyitaw != μ Yangon ")

 
    f_stat,p_val = stats.f_oneway(data_1.Mandalay,data_1.Naypyitaw,data_1.Yangon)
    st.write(f"Hasil Uji Statistik:  \n f stat : `{round(f_stat,4)}`  \n p-value : `{round(p_val,4)}`")
    st.write('Hasil uji hipotesis dengan menggunakan `Anova Test` dapat disimpulkan bahwa kita `menerima H0 atau Hipotesis awal` hal tersebut dapat \
         dilihat dari nilai p value diatas 0.05 sehingga dapat disimpulkan tidak ada perbedaan yang signifikan diantara rata-rata gross income kota Mandalay, Naypyitaw dan Yangon. agar lebih jelas dapat melihat grafik dibawah ini:')

    # with st.expander('show plot'):
        # # Confidence interval 
        # ci = stats.norm.interval(0.95, data_1.Mandalay.mean(), data_1.Mandalay.std())

        # # create sample population
        # mandalay_pop = np.random.normal(data_1.Mandalay.mean(),data_1.Mandalay.std(),1000)
        # naypyitaw_pop = np.random.normal(data_1.Naypyitaw.mean(),data_1.Naypyitaw.std(),1000)
        # yangon_pop = np.random.normal(data_1.Yangon.mean(),data_1.Yangon.std(),1000)

        # hist_data = [mandalay_pop, naypyitaw_pop, yangon_pop]

        # group_labels = ['Mandalay', 'naypyitaw', 'yangon']

        # # Create distplot with curve_type set to 'normal'
        # fig = ff.create_distplot(hist_data, group_labels, 
        #                         bin_size=.2, show_rug=False)

        # # Add title
        # fig.add_vline(x=data_1.Mandalay.mean(), line_width=2, line_dash="dash", line_color="#A56CC1")
        # fig.add_vline(x=data_1.Naypyitaw.mean(), line_width=2, line_dash="dash", line_color="#A6ACEC")
        # fig.add_vline(x=data_1.Yangon.mean(), line_width=2, line_dash="dash", line_color="#63F5EF")
        # fig.add_vline(x=ci[0], line_width=2, line_dash="dash", line_color="black")
        # fig.add_vline(x=ci[1], line_width=2, line_dash="dash", line_color="black")
        # st.plotly_chart(fig,use_container_width=True)

    with st.expander('show plot'):
            # Confidence interval 
            ci = stats.norm.interval(0.95, data_1.Mandalay.mean(), data_1.Mandalay.std())

            # create sample population
            mandalay_pop = np.random.normal(data_1.Mandalay.mean(),data_1.Mandalay.std(),10000)
            naypyitaw_pop = np.random.normal(data_1.Naypyitaw.mean(),data_1.Naypyitaw.std(),10000)
            yangon_pop = np.random.normal(data_1.Yangon.mean(),data_1.Yangon.std(),10000)

            ci = stats.norm.interval(0.95, data_1.Mandalay.mean(),data_1.Mandalay.std())
            plt.figure(figsize=(16,5))

            sns.distplot(mandalay_pop, label='Mandalay Daily Average Gross Sales*Pop',color='blue')
            sns.distplot(naypyitaw_pop, label='Naypyitaw Daily Average Gross Sales*Pop',color='red')
            sns.distplot(yangon_pop, label='Yangon Daily Average Gross Sales*Pop',color='green')

            plt.axvline(data_1.Mandalay.mean(), color='blue', linewidth=2, label='Mandalay mean')
            plt.axvline(data_1.Naypyitaw.mean(), color='red',  linewidth=2, label='Naypyitaw mean')
            plt.axvline(data_1.Yangon.mean(), color='green',  linewidth=2, label='Yangon mean')

            plt.axvline(ci[1], color='black', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
            plt.axvline(ci[0], color='black', linestyle='dashed', linewidth=2)

            plt.axvline(naypyitaw_pop.mean()+f_stat*naypyitaw_pop.std(), color='orange', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
            plt.axvline(naypyitaw_pop.mean()-f_stat*naypyitaw_pop.std(), color='orange', linestyle='dashed', linewidth=2)

            plt.axvline(yangon_pop.mean()+f_stat*yangon_pop.std(), color='yellow', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
            plt.axvline(yangon_pop.mean()-f_stat*yangon_pop.std(), color='yellow', linestyle='dashed', linewidth=2)
            plt.legend()
            st.pyplot()