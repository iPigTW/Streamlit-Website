import streamlit as st
st.set_page_config(page_title="Social Media", page_icon=":pig:", layout="wide", initial_sidebar_state="expanded")
st.sidebar.title("iPig's Website")
st.sidebar.success("Select a page above")

with st.container():
    st.title("My Social Medias")
    st.link_button(label="YouTube", url="https://youtube.com/@ipigtaiwan")
    st.link_button(label="Discord", url="https://discord.com/users/1113319860760494161")
    st.link_button(label="Github", url="https://github.com/ipigtw")
    