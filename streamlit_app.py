import streamlit
import snowflake.connector
streamlit.title('My Parents New Healthy Diner')

cnx = st.connection("snowflake")
my_cur = my_cnx.cursor()
