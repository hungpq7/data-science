import streamlit as st
st.set_page_config(layout='wide')

st.sidebar.radio('Approach', ['Fundamental', 'Technical'])

st.write('Hello Streamlit')