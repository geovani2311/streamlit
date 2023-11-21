import streamlit as st 
from PIL import Image

st.set_page_config(page_title=None,
                page_icon=None, 
                layout="wide", 
                initial_sidebar_state="auto", 
                menu_items=None)

st.header('Data science, data analysis in another perspective', divider='rainbow')
st.subheader("When you think and some problems that you have to resolve in your job like a data sciencist or data analyts, you have to use tecnhiques and hard skill for solve, so let's go, you extract the data using, transform and load in dashboarb or anything else, and answear the question, but have you ever before, there is something is it impossible to respond, just extract, transform e load the data, exiting a big big world outside, and the this analysts think it's not necessary explore the world to find news things, is like me and my pc, and just solve the problem..., Noo it's wrong, the good analyts explore the world, he know's about the human behavior, he goes to the mall and see the guy buying a expansive price for a simple gift that have a big brand, and he asks himself: why that guy is buying a simple gift for high price, is the worth?, in this case the analyst asks to himself about the behavior guy, but it's only happen because he goes to the mall, conclusion is, it's not only you and pc for be a great analyst, but understanding the world and how the brain works in single individual")

image = Image.open('dog_suits.jpg')      

with st.sidebar:
    st.header("Development by Geovani Lima Cardoso")
    st.image(image, width=200,)
    st.subheader("linkedin:https://www.linkedin.com/in/geovani-lima-cardoso-760212158/")