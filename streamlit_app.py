import streamlit
import snowflake.connector
streamlit.title('My Parents New Healthy Diner')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
