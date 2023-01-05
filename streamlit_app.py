import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('my parents new healthy diner');
streamlit.header('BREAKFAST MENU');
streamlit.text('Dosa');
streamlit.text('Onion Dosa');
streamlit.text('chola poori');
streamlit.text('Idle');
streamlit.text('masala Dosa');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit');

# Let's put a pick list here so they can pick the fruit they want to include 

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']);
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice')

def get_fruitvice_data (fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("select some fruit to show information.")
  else:
    back_from_function= get_fruitvice_data (fruit_choice)
    streamlit.dataframe(back_from_function)
     
  
except URLError as e:
  streamlit.error()

def insertrow_snowflake(add_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from pc_rivery_db.public.fruit_load_list('from streamlit')")
      return "thanks for adding"+add_Fruit


add_my_fruit=streamlit.text_input('what fruit did you like to add?')
if streamlit.button("add a fruit to the list"):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function=insertrow_snowflake(add_fruit)
   streamlit.text(back_from_function)



