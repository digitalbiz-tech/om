import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Order", usecols=[0,1,2,3,4,5,6,7,8],ttl=5)
order_detail_df = conn.read(worksheet="OrderDetails", usecols=[0,1,2,3,4,5,6],ttl=5)

#df = df[df['Order Number'] != " "]
#df = df.set_index(df.columns[0])

tab1, tab2, tab3 = st.tabs(["Order", "Order Details", "Catalog"])
tab2.write("Details of Order")
tab2.dataframe(order_detail_df)

tab1.write("Here's the list of the Orders made so far")
edited_df = tab1.data_editor(
    df,
    width = 1500,
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
            help="Order Status",
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
            "Contact",
            help="Order Mobile Number",
            format="%d",
            disabled = True,
        ),
        "Order Type": st.column_config.SelectboxColumn(
            "Order Type",
            help="Order Type",
            options=[
                "Sample",
                "Actual",
            ],
            required=True,
        ),
    
        "Order By": st.column_config.TextColumn(
            "Person",
            help="Order By",
            disabled=True,
        ),
        
      "Expected Order Date": "Expected Delivery date",
      "Notes": "Notes",
        "WA_MID": "WA_MID",
    },
    disabled=["Order Date", "OrderContact", "Notes"],
    hide_index=True,
)

conn.update(worksheet="Order", data=edited_df)
# Print results.
#for row in df.itertuples():
#    st.write(f"{row.OrderContact}")
