import streamlit as st
from PIL import Image
import pandas as pd

logo = Image.open("res/logo_V2.png")

st.set_page_config(
    page_title= "Home",
    page_icon= logo
)
st.image(Image.open("res/1.png"))
st.markdown("# RADI: Realtime Audio Description of Image")
st.image(Image.open("res/logo_V1.png"), width=100)
st.sidebar.markdown("# Home page")

st.title("Major Project")

df = pd.DataFrame([["Ajay H Hegde","1DA19CS010"],["Anirudh B Mitta", "1DA19CS014"],["Beluvigi Shreegagana", "1DA19CS027"],["Mohammad Rooh Ullah", "1DA19CS089"]], columns=["Name","USN"],index=[1,2,3,4])

st.subheader("Done By:")
st.table(data=df)

st.subheader("Guided By: ")
st.write("Prof. AshaRani K P")
st.write("Assistant Professor")
st.write("Dept. of CSE, Dr. AIT")
