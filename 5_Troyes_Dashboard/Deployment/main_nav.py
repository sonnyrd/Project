#import library
import streamlit as st
from streamlit_option_menu import option_menu

#import .py
import team
import player

# set page config
st.set_page_config(
    page_title="Troyes Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/sonnyrd',
        'Report a bug': "https://github.com/sonnyrd",
        'About': "# Troyes"
    }
)

st.set_option('deprecation.showPyplotGlobalUse', False)

PAGES = {
    "Team": team,
    "Player": player,
}

selected = option_menu(None, ["Team", "Player"], 
    icons=['house', 'people'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "rgb(27, 59, 102)"},
    }
)   

page = PAGES[selected]

page.app()