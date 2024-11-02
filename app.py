import streamlit as st
import pandas as pd

st.title("Simple Streamlit App")
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
st.write("Here's a sample DataFrame:")
st.write(df)
