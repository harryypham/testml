
import streamlit as st
from model import *

with st.form("my_form"):
   st.write("Inside the form")
   usr_inp = st.text_input('Write sth', 'Life of Brian')
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       out = generate_output(usr_inp)
       st.write(out)

st.write("Outside the form")



