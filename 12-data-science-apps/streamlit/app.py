import numpy as np
import pandas as pd

import streamlit as st
st.set_page_config(layout='wide')

st.sidebar.radio('Approach', ['Fundamental', 'Technical'])

st.write('Hello world')