import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

df = df[df['Order Number'] != 'None']
st.write("Here's the list of the Orders made so far")
edited_df = st.experimental_data_editor(df)

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.OrderContact}")
