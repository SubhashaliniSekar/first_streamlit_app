import streamlit 
import pandas
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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacoda','Strawberries']);

# Display the table on the page.

streamlit.dataframe(my_fruit_list);
