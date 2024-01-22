import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

df = df[df['Order Number'] != " "]
st.write("Here's the list of the Orders made so far")
edited_df = st.data_editor(
    df,
    column_config={
        "Order Number": "Order ID",
        "Order Status": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "Order Date": "Ordered Date",
      "OrderContact": "Ordered By",
      "Order Type": "Order Type",
      "Expected Order Date": "Expected Delivery date",
      "Notes": "Notes",

    },
    disabled=["Notes"],
    hide_index=True,
)

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.OrderContact}")
