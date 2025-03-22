import streamlit as st
from ollama import Client
import pandas as pd
import numpy as np
import time

client = Client(
  host= 'https://6fb7-155-69-184-252.ngrok-free.app/')

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Start generating your project now!"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Insert your idea"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
         stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
    
    assistant_response =["Hello there! How can I assist you today?" ]

    for chunk in assistant_response.split():
        full_response += chunk + " "
        time.sleep(0.05)

    st.session_state.messages.append({"role": "assistant", "content": full_response})