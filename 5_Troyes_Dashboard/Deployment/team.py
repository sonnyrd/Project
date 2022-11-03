# Import Library ##
import streamlit as st
import streamlit_nested_layout
import pandas as pd
import plotly.graph_objects as go

# import function py
from function_lib import *

def app():
  # load css style
  def local_css(file_name):
      with open(file_name) as f:
          st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
  local_css("style.css")

  # Title
  # st.write("<h1 style='text-align: center; '>Troyes</h1>", unsafe_allow_html=True)


  ##################### Dataframe ##########################
  # Loading data frame
  df =pd.read_csv("https://raw.githubusercontent.com/sonnyrd/datasets/main/troyes_matchlog.csv")
  df.fillna(0)
  # create point column
  df['point'] = df['result'].map({'W':3,'D':1,'L':0})

  # create goal diff
  df['goals_diff'] = df['goals_for']-df['goals_against']

  # recalculate pct
  df['shots_on_target_pct'] = (df['shots_on_target']/df['shots_total'])

  # list opponent
  list_opponent = df['team'].unique().tolist()
  list_opponent.insert(0,'Ligue1')
  list_opponent.remove('Troyes')


  param_title = 'Average Point'
  param_trend = 'point'

  ###########################################################
  with st.container():
    col1,col2,col3,col4,col5 = st.columns([1.5,0.5,0.5,0.5,0.5])
    with col1:
      st.markdown(match_result(df),unsafe_allow_html=True)
    with col2:
      st.markdown(cal_card(df,'Average Point','point','Ligue1'),unsafe_allow_html=True)
      if st.button(label="See Trend",key=0):
        param_title = 'Average Point'
        param_trend = 'point'
    with col3:
      st.markdown(cal_card(df,'Average Scored','goals_for','Ligue1'),unsafe_allow_html=True)
      if st.button(label="See Trend",key=1):
        param_title = 'Average Score'
        param_trend = 'goals_for' 
    with col4:
      st.markdown(cal_card(df,'Average Concede','goals_against','Ligue1'),unsafe_allow_html=True)
      if st.button(label="See Trend",key=2):
        param_title = 'Average Concede'
        param_trend = 'goals_against' 
    with col5:
      st.markdown(cal_card(df,'Average Possesion','possession','Ligue1'),unsafe_allow_html=True)
      if st.button(label="See Trend",key=3):
        param_title = 'Average Possesion'
        param_trend = 'possession' 
  #############################################################
  with st.container():
    col1,col2,col3,col4,col5 = st.columns([0.9,1.3,1.1,0.1,0.1])
    with col1:
      st.markdown(ligue1_table(df),unsafe_allow_html=True)
    with col2:
      st.write("")
      option = st.selectbox(
      'Select Comparison',
      list_opponent,
      index=0)
      fig = go.Figure()
      fig = radar_chart(df,option)
      st.plotly_chart(fig,use_container_width=True)
    with col3:
      st.write("")
      st.write("")
      st.write("")
      st.write("")
      st.plotly_chart(func_trend(df,param_title,param_trend))
      with st.expander('insight',expanded=True):
        st.write(insight_point(df))

  ###############################################################
  with st.container():
    st.markdown(title_name('Offensive'),unsafe_allow_html=True)
    st.write("")
    col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
    with col1:
      st.markdown(cal_card(df,'Shots On Target','shots_on_target','Ligue1'),unsafe_allow_html=True)
    with col2:
      st.markdown(cal_card2(df,'% Shots On Target','shots_on_target_pct','Ligue1'),unsafe_allow_html=True)
    with col3:
      st.markdown(cal_card(df,'Goals per Shot on Target','goals_per_shot_on_target','Ligue1'),unsafe_allow_html=True)
    with col4:
      st.markdown(cal_card(df,'Goals','goals_for','Ligue1'),unsafe_allow_html=True)
    with col5:
      st.markdown(cal_card(df,'Expected Goals','xg','Ligue1'),unsafe_allow_html=True)
    with col6:
      st.markdown(cal_card(df,'Goal Creation Attemp','gca','Ligue1'),unsafe_allow_html=True)

  with st.container():
    st.plotly_chart(funct_goals_xg(df))

  ###############################################################
  # df
  with st.container():
    st.markdown(title_name('Defensive (Goal Keeper)'),unsafe_allow_html=True)
    st.write("")
    col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
    with col1:
      st.markdown(cal_card(df,'GK Shots Againts','gk_shots_on_target_against','Ligue1'),unsafe_allow_html=True)
    with col2:
      st.markdown(cal_card2(df,'% GK Saves','gk_saves','Ligue1'),unsafe_allow_html=True)
    with col3:
      st.markdown(cal_card(df,'Cleansheet','gk_clean_sheets','Ligue1'),unsafe_allow_html=True)
    with col4:
      st.markdown(cal_card(df,'Goals Against','goals_against','Ligue1'),unsafe_allow_html=True)
    with col5:
      st.markdown(cal_card(df,'Expected Goals Againts','gk_psxg','Ligue1'),unsafe_allow_html=True)

  st.write("")

  with st.container():
    st.markdown(title_name('Defensive (Player)'),unsafe_allow_html=True)
    st.write("")
    col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
    with col1:
      st.markdown(cal_card(df,'%  Dribblers Tackled','dribble_tackles_pct','Ligue1'),unsafe_allow_html=True)
    with col2:
      st.markdown(cal_card2(df,'% Succesful Pressure','pressure_regain_pct','Ligue1'),unsafe_allow_html=True)
