import Feature_01
import streamlit as st

From Feature_01 import return_even

original_list = [i for i in range(10)]

even_list = return_even(original_list)


st.write("hooray, we connected everything")

st.write(even_list)

