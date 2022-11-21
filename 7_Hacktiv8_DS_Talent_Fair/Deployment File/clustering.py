import streamlit as st
import numpy as np
import pickle
import pandas as pd
from sklearn.decomposition import PCA

def app():
     #load style css
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    local_css("style.css")

    #title
    st.write("<h1 style='text-align: center; '>Customer Credit Segmentation</h1>",
            unsafe_allow_html=True)

    
    st.write('Customer Profile:')
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            var1 = st.number_input('Age',value=30)
        with col2:
            var2 = st.selectbox('Please select Gender',('male','female'))
        with col3:
            var3 = st.selectbox('Please select Job',(1,2,3,4),help=('Job (numeric: 0 - unskilled and non-resident, 1 - unskilled and resident, 2 - skilled, 3 - highly skilled)'))
        with col4:
            var4 = st.selectbox('Please select Housing',('own','free','rent'))

    st.write('Financial Profile:')
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            var5 = st.selectbox('Saving accounts',('little','moderate','quite rich','rich'))
        with col2:
            var6 = st.selectbox('Checking Account',('little','moderate','rich'))
    
    st.write('Credit information:')
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            var7 = st.number_input('Credit amount',value=1000000)
        with col2:
            var8 = st.number_input('Duration',value=12)
        with col3:
            var9 = st.selectbox('Purposes',('business','car','education','domestic appliances','furniture/equipment','radio/TV','repairs','vacation/others'))

    # Data Preprocessing
    data = {
    'Age': var1,
    'Sex': var2,
    'Job': var3,
    'Housing': var4,
    'Saving accounts': var5,
    'Checking account': var6,
    'Credit amount': var7,
    'Duration': var8,
    'Purpose': var9,
    }

    # scaling
    columns = list(data.keys())
    df = pd.DataFrame([data.values()], columns=columns)
    list_drop = ['Sex', 'Purpose']
    df = df.drop(columns=list_drop)

    with open('pipe_fe.pkl', 'rb') as f:
        pipe_fe = pickle.load(f)

    df_scale = pipe_fe.transform(df)

    # pca preprosessing
    with open('pca_pp.pkl', 'rb') as f:
        pca_pp = pickle.load(f)

    data_inf_reduce_df = pca_pp.transform(df_scale)
    data_inf_reduce_df = pd.DataFrame(data_inf_reduce_df)

    # predict
    with open('cluster_model.pkl', 'rb') as f:
        kmeans = pickle.load(f)

    if st.button('Predict'):
        pred = kmeans.predict(data_inf_reduce_df)
        data_cleaned_clustered = data_inf_reduce_df.copy()
        data_cleaned_clustered['Cluster'] = pred + 1
        st.write(f"<h1 style='text-align: center; '>Cluster :{(data_cleaned_clustered['Cluster'][0])}</h1>", unsafe_allow_html=True)
        if data_cleaned_clustered['Cluster'][0] == 1:
            st.text_area('characteristic',
            '- Age : Average Age 28 Years Old (Adult)\n\
            - Credit Amount : Average IDR 25 Milion (Low)\n\
            - Duration : Average duration 15 Month\n\
            - Job : Mostly Skilled\n\
            - Saving Account : Mostly little\n \
            - Checking Account : Mostly Moderate & Little\n \
            - Purpose : Mostly for Radio/TV, Furniture/equipment, Car')
        if data_cleaned_clustered['Cluster'][0] == 2:
            st.text_area('characteristic',
            '- Age : Average Age 48 Years Old (Senior Citizen)\n\
            - Credit Amount : Average IDR 25 Milion (Low)\n\
            - Duration : Average duration 15 Month\n\
            - Job : Mostly Skilled\n\
            - Saving Account : Mostly little\n\
            - Checking Account : Mostly Moderate & Little\n\
            - Purpose : Mostly for Radio/TV, Car')
        if data_cleaned_clustered['Cluster'][0] == 3:
            st.text_area('characteristic',
            '- Age : Average Age 34 Years Old (Adult)\n\
            - Credit Amount : Average IDR 74 Milion (High)\n\
            - Duration : Average duration 33 Month\n\
            - Job : Mostly Skilled\n\
            - Saving Account : Mostly little\n\
            - Checking Account : Mostly Moderate & Little\n\
            - Purpose : Mostly for Radio/TV, Car')            