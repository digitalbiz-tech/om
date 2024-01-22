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
        "Order Status": st.column_config.SelectboxColumn(
            "Status of your Order",
            help="Order status",
            width="medium",
            options=[
                "Submitted",
                "Ready For Collection",
                "Dispatched",
                "Closed",
            ],
            required=True,
        ),
      "Order Date": "Ordered Date",
      "OrderContact": "Ordered By",
      "Order Type": "Order Type",

        "Order Type": st.column_config.SelectboxColumn(
            "Type of your order",
            help="Order Type",
            width="medium",
            options=[
                "Sample",
                "Actual",
            ],
            required=True,
        ),
        
      "Expected Order Date": "Expected Delivery date",
      "Notes": "Notes",
    },
    disabled=["Order Date", "OrderContact", "Notes"],
    hide_index=True,
)

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.OrderContact}")
