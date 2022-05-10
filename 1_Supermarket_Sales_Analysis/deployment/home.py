import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

def app():
    st.markdown(
    '''
    <style>
    h2   {background-color: #b7d7e8;
            color: #000000;
        font-family: "Arial";
        font-size: 40px;
        text-align: left;
        border-radius: 15px 30px;
        margin: 0px 0px 20px 0px;
        }
    </style>
    <h2>Main Page</h2>

    <p>&nbsp;</p>
    <h4 style="text-align: center;">App ini dibuat sebagai Dashboard untuk melakukan visualisasi  Data terhadap sales supermarket sales di kota Mandalay, Naypyitaw, dan Yangon.</h3>
    <p style="text-align: left;">&nbsp;</p>
    <p style="text-align: left;">&nbsp;</p>
    <p>&nbsp;</p>
    <p><strong>&nbsp;</strong></p>   

    <h2>Feature</h2>
    
    <h4>1. Sales performance</h3>
    <h4>2. Customer Profile</h3>
    <h4>3. Hypothesis Testing</h3>
    <p style="text-align: left;">&nbsp;</p>
    <p>&nbsp;</p>
    <p><strong>&nbsp;</strong></p>  
    '''
    ,unsafe_allow_html=True)