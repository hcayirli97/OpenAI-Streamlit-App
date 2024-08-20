import streamlit as st
import openai
import os

try:
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    st.subheader("Text2Speech")
    with st.expander("Settings"):
        voice = st.selectbox(
            "Voice Options",
            [
                "nova",
                "alloy",
                "echo",
                "fable",
                "onyx",
                "shimmer"
            ])

    with st.form(key='text_form'):
        text_input = st.text_area("Enter Text", "Write a text here ...")
        submit_button = st.form_submit_button(label='Generate Audio 🎵')
    if submit_button:
        with st.spinner('Generating audio...'):
            response = client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=text_input
            )
            response.write_to_file("output.mp3")
        with open("output.mp3", "rb") as audio_file:
            st.audio(audio_file, format='audio/mp3')
except:
    st.info("API Key is incorrect. Please enter a correct API Key.")