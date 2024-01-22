import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

st.write("Here's our first attempt at using data to create a table:")
df2 = pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]}))
edited_df = st.experimental_data_editor(df2)

# Print results.
for row in df.itertuples():
    st.write(f"{row.OrderContact}")
