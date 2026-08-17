import streamlit as st

from modules.home import show_home
from modules.upload import show_upload
from modules.visualization import show_visualization
from modules.insights import show_insights


# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="PharmaPulse",
    page_icon="🏥",
    layout="wide"
)


# =====================================
# Sidebar
# =====================================

st.sidebar.title("PharmaPulse")

page = st.sidebar.radio(
    "Navigation",
    (
        "Home",
        "Upload Dataset",
        "Visualization",
        "Business Insights"
    )
)


# =====================================
# Page Routing
# =====================================

if page == "Home":
    show_home()

elif page == "Upload Dataset":
    show_upload()

elif page == "Visualization":
    show_visualization()

elif page == "Business Insights":
    show_insights()