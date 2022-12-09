#import library
import streamlit as st

#import .py
import nlp

# Page configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="🧊",
    # layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/sonnyrd',
        'Report a bug': "https://github.com/sonnyrd",
        'About': "# This is Dashboard for Hacktiv8 Talent Fair"
    }
)
st.set_option('deprecation.showPyplotGlobalUse', False)

PAGES = {
    "Auto Categorizing Article": nlp,
}

st.sidebar.title('Navigation')
selected = st.sidebar.selectbox('select a page', list(PAGES.keys()))

page = PAGES[selected]

page.app()