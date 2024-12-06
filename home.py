import streamlit as st
from main import caption
from main import imageUrl
from main import titleofArticle
#streamlit used for web apps and interfaces

st.set_page_config(layout="wide")
col1 , space_col, col2 = st.columns([1.5,0.5,1.5])

st.header('Contact ur own mother')
st.subheader("Welcome To Doppel News")
st.title("My Published Article")
st.write("This app will publish fresh news and article for your prying eyes!")


with col1:
    st.image(imageUrl)


with col2:
    st.title(titleofArticle)
    st.write(caption)


# st.session_state
print("Your application is running!!!")