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
        "Order Number": st.column_config.NumberColumn(
            "Order ID",
            help="Order ID",
            width="small",
            format="%d",
            disabled = True,
        ),
        "Order Status": st.column_config.SelectboxColumn(
            "Status of your Order",
            help="Order status",
            width="small",
            options=[
                "Submitted",
                "Ready For Collection",
                "Dispatched",
                "Closed",
            ],
            required=True,
        ),
      "Order Date": "Ordered Date",
      "OrderContact": st.column_config.NumberColumn(
            "OrderContact",
            help="Order Mobile Number",
            width="small",
            format="%d",
            disabled = True,
        ),
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
    
        "Order By": st.column_config.TextColumn(
            "Person who has made the order",
            help="Order By",
            width="medium",
            disabled=True,
        ),
        
      "Expected Order Date": "Expected Delivery date",
      "Notes": "Notes",
    },
    disabled=["Order Date", "OrderContact", "Notes"],
    hide_index=True,
)

conn.write(edited_df)
# Print results.
#for row in df.itertuples():
#    st.write(f"{row.OrderContact}")
