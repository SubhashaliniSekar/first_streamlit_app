import streamlit 
streamlit.title('my parents new healthy diner');
streamlit.header('BREAKFAST MENU');
streamlit.text('Dosa');
streamlit.text('Onion Dosa');
streamlit.text('chola poori');
streamlit.text('Idle');
streamlit.text('masala Dosa');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.dataframe(my_fruit_list);
