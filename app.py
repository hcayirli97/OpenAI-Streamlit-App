import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
import os

st.set_page_config(layout="wide")

title_container = st.empty()

title_container.title("AI Multi Model App")

open_api_key = st.sidebar.text_input(
    "Enter Your OpenAI API Key 🗝️",
    value=st.session_state.get('open_api_key', ''),
    help="Get your API key from https://openai.com/",
    type='password')


if open_api_key != '':
    title_container.empty()
    os.environ["OPENAI_API_KEY"] = open_api_key

    nav = get_nav_from_toml()

    pg = st.navigation(nav)

    add_page_title(pg)

    pg.run()