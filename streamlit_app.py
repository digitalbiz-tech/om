import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import os

diff_df = ""
#def update(conn,edited_df,df):
#  print("in update")

st.set_page_config(page_title="Order Management", layout="wide")

def change_state(df,edited_df,tab3,key):
  tab3.write(st.session_state)
  #df_diff = pd.concat([df,edited_df]).drop_duplicates(keep=False)
  #diff_df = pd.merge(df, edited_df, on='Order Number', how = 'inner', indicator=True)
  #diff_df = diff_df[diff_df._merge != 'both'] # Filter out records from both
  tab3.dataframe(edited_df)
  #diff_df = df.compare(edited_df)
  #print(diff_df)
  #os.write(1,b'Something was executed.\n')
  st.session_state['df_value']=edited_df
  
  
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Order", usecols=[0,1,2,3,4,5,6,7,8,9,10],ttl=5)
order_detail_df = conn.read(worksheet="OrderDetails", usecols=[0,1,2,3,4,5,6,7,8],ttl=5)
#order_detail_df = order_detail_df.style.highlight_null(props="color: transparent;") 

#df = df[df['Order Number'] != " "]
#df = df.set_index(df.columns[0])
diff_df = df
tab1, tab2, tab3 = st.tabs(["Order", "Order Details", "Catalog"])
tab3.dataframe(diff_df)
tab2.write("Details of Order")
tab2.dataframe(order_detail_df,
                  column_config={
        "Order Number": st.column_config.NumberColumn(
            "Order ID",
            help="Order ID",
            width="small",
            format="%d",
            disabled = True,
        ),
        "Product CatalogID": st.column_config.TextColumn(
            "CatalogID",
            help="WhatsApp Product Catalog ID",
        disabled = True,        
        ),

        "OrderText": st.column_config.TextColumn(
            "Title",
            help="WhatsApp Product Catalog ID",
        disabled = True,        
        ),
        "product_retailer_id": st.column_config.TextColumn(
            "Product ID",
            help="WhatsApp Product ID",
        disabled = True,
        ),
        "quantity": st.column_config.NumberColumn(
            "Quantity",
            help="Quantity",
            width="small",
            format="%d",
            disabled = True,
        ),
        "item_price": st.column_config.NumberColumn(
            "Price",
            help="Price",
            width="small",
            format="£%d",
            disabled = True,
        ),
    
    },
    hide_index=True
)

tab1.write("Here's the list of the Orders made so far")

if "df_value" not in st.session_state:
  st.session_state.df_value = df
edited_df=st.session_state['df_value']

edited_df = tab1.data_editor(
    df,
    key = "Order Number",
    width = 1500,
    column_config={
        "Order Number": st.column_config.NumberColumn(
            "Order Number",
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
      "Order Quantity": st.column_config.NumberColumn(
            "Order Quantity",
            help="Order Quantity",
            format="%d",
            disabled = True,
        ),
          "Order Amount": st.column_config.NumberColumn(
            "Order Amount",
            help="Order Amount",
            format="£%d",
            disabled = True,
        ),    
      "Expected Order Date": st.column_config.TextColumn(
            "Expected Order Date",
            help="Expected Order Date",
            disabled=True,
        ),
      "Notes": st.column_config.TextColumn(
            "Notes",
            help="Notes",
            disabled=True,
        ),
        "WA_MID": st.column_config.TextColumn(
            "WA_MID",
            help="WA_MID",
            disabled=True,
        ),
    },
  on_change=  change_state,
  args=(df,edited_df,tab3),
)
#update(conn, edited_df)
#conn.update(worksheet="Order", data=edited_df)
# Print results.
#for row in df.itertuples():
#    st.write(f"{row.OrderContact}")
