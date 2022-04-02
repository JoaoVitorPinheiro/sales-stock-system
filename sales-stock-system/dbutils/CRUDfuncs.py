import streamlit as st
import pandas as pd
from gsheetsdb import connect

def create_query(
    query_statement,       # SELECT, INSERT, UPDATE, DELETE statements
    query_clauses          # WHERE clauses
    ):
    pass
def insert_product():
    pass
def update_product():
    pass
def delete_product():
    pass
def get_product():
    pass
def dbtest():
        # Create a connection object.
    conn = connect()
    # Perform SQL query on the Google Sheet.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    @st.cache(ttl=600)
    def run_query(query):
        rows = conn.execute(query, headers=1)
        rows = rows.fetchall()
        
        return rows

    sheet_url = 'https://docs.google.com/spreadsheets/d/1UfePNl4Rra7kfBl5h9aXijVP-RNtzzU_l7I_BV_z6ms/edit#gid=0'
    query_msg = f'SELECT * FROM "{sheet_url}"'
    rows = run_query(query_msg)
    
    df = pd.read_sql(query_msg, conn)
    st.dataframe(df)
    st.json(rows)
    st.write(type(rows))
    
    # Print results.
    for row in rows:
        st.write(f"{row.CT_NOME} custa R${row.VL_PRECO} reais")
        
    
    