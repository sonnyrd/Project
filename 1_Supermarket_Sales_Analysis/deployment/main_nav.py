#import library
import streamlit as st

#import .py
import home
import sales_performance
import customer_profiling
import hypothesis_testing


# Page configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/sonnyrd',
        'Report a bug': "https://github.com/sonnyrd",
        'About': "# This is Dashboard for data visualization"
    }
)
st.set_option('deprecation.showPyplotGlobalUse', False)

PAGES = {
    "Home": home,
    "Sales Performance": sales_performance,
    "Customer Profile": customer_profiling,
    "Hypothesis Testing": hypothesis_testing
}

st.sidebar.title('Navigation')
selected = st.sidebar.selectbox('select a page', list(PAGES.keys()))

page = PAGES[selected]

page.app()