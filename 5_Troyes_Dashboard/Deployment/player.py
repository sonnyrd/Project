import streamlit as st
from streamlit_option_menu import option_menu

# import function py
from function_lib import *
from function_lib2 import *

def app():

    # load css style
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    local_css("style.css")

    # load dataframe

    df_player = pd.read_csv('https://raw.githubusercontent.com/sonnyrd/datasets/main/player_stat.csv')
    df_goalkeeper = pd.read_csv('https://raw.githubusercontent.com/sonnyrd/datasets/main/keeper_stat.csv')

    df_player.drop_duplicates(subset=['player'],keep='last',inplace=True)
    df_player[['position','position1']] = df_player['position'].str.split(',',expand=True)
    df_player['position'] = df_player['position'].map({'FW':'Forward','DF':'Defender','MF':'Midfielder','GK':'Goalkeeper'}).fillna(df_player['position'])
    df_player['position1'] = df_player['position1'].map({'FW':'Forward','DF':'Defender','MF':'Midfielder','GK':'Goalkeeper'}).fillna(df_player['position1'])

    pos_select = st.selectbox('Select Position',('Forward','Midfielder','Defender','Goalkeeper'))
    
    if pos_select == 'Forward':
        st.markdown(title_name('Forward'),unsafe_allow_html=True)

        col1,col2,col3,col4,col5,col6 = st.columns([1,1.85,1,1,1,1])
        with col1:
            player_name = st.selectbox('Select Player',pos_player(df_player,'Forward'))
        with col3:
            st.markdown(card(df_player,'games','Appearances',player_name),unsafe_allow_html=True)
        with col4:
            st.markdown(card(df_player,'minutes','Minutes Played',player_name),unsafe_allow_html=True)
        with col5:
            st.markdown(card(df_player,'goals','Goals',player_name),unsafe_allow_html=True)
        with col6:
            st.markdown(card(df_player,'assists','Assists',player_name),unsafe_allow_html=True)

        col1,col2,col3 = st.columns(3)
        with col1:
            st.plotly_chart(shooting_sca_gca(df_player,'Forward',player_name))
        with col2:
            st.plotly_chart(passing_and_possesion(df_player,'Forward',player_name))
        with col3:
            st.plotly_chart(defense(df_player,'Forward',player_name))


#####################################
    if pos_select == 'Midfielder':
        st.markdown(title_name('Midfielder'),unsafe_allow_html=True)

        col1,col2,col3,col4,col5,col6 = st.columns([1,1.5,1,1,1,1])
        with col1:
            player_name = st.selectbox('Select Player',pos_player(df_player,'Midfielder'))
        with col3:
            st.markdown(card(df_player,'games','Appearances',player_name),unsafe_allow_html=True)
        with col4:
            st.markdown(card(df_player,'minutes','Minutes Played',player_name),unsafe_allow_html=True)
        with col5:
            st.markdown(card(df_player,'goals','Goals',player_name),unsafe_allow_html=True)
        with col6:
            st.markdown(card(df_player,'assists','Assists',player_name),unsafe_allow_html=True)

        col1,col2,col3 = st.columns(3)
        with col1:
            st.plotly_chart(shooting_sca_gca(df_player,'Midfielder',player_name))
        with col2:
            st.plotly_chart(passing_and_possesion(df_player,'Midfielder',player_name))
        with col3:
            st.plotly_chart(defense(df_player,'Midfielder',player_name))

#####################################
    if pos_select == 'Defender':
        st.markdown(title_name('Defender'),unsafe_allow_html=True)

        col1,col2,col3,col4,col5,col6 = st.columns([1,1.5,1,1,1,1])
        with col1:
            player_name = st.selectbox('Select Player',pos_player(df_player,'Defender'))
        with col3:
            st.markdown(card(df_player,'games','Appearances',player_name),unsafe_allow_html=True)
        with col4:
            st.markdown(card(df_player,'minutes','Minutes Played',player_name),unsafe_allow_html=True)
        with col5:
            st.markdown(card(df_player,'goals','Goals',player_name),unsafe_allow_html=True)
        with col6:
            st.markdown(card(df_player,'assists','Assists',player_name),unsafe_allow_html=True)

        col1,col2,col3 = st.columns(3)
        with col1:
            st.plotly_chart(shooting_sca_gca(df_player,'Defender',player_name))
        with col2:
            st.plotly_chart(passing_and_possesion(df_player,'Defender',player_name))
        with col3:
            st.plotly_chart(defense(df_player,'Defender',player_name))


#####################################
    if pos_select == 'Goalkeeper':
        st.markdown(title_name('Goalkeeper'),unsafe_allow_html=True)

        col1,col2,col3,col4,col5,col6 = st.columns([1,1.5,1,1,1,1])
        with col1:
            player_name = st.selectbox('Select Player',pos_player(df_player,'Goalkeeper'))
        with col3:
            st.markdown(card(df_player,'games','Appearances',player_name),unsafe_allow_html=True)
        with col4:
            st.markdown(card(df_player,'minutes','Minutes Played',player_name),unsafe_allow_html=True)
        with col5:
            st.markdown(card(df_player,'goals','Goals',player_name),unsafe_allow_html=True)
        with col6:
            st.markdown(card(df_player,'assists','Assists',player_name),unsafe_allow_html=True)

        col1,col2,col3 = st.columns(3)
        with col1:
            st.plotly_chart(goalkeeping(df_goalkeeper,'Goalkeeper',player_name))
        with col2:
            st.plotly_chart(passing_and_possesion(df_player,'Goalkeeper',player_name))  
        with col3:
            st.plotly_chart(defense(df_player,'Goalkeeper',player_name))


