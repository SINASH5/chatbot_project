import streamlit as st
import requests

# Streamlit UI
st.title("Chatbot")

user_input = st.text_input("You:")
if st.button("Send"):
    if user_input:
        try:
            response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
            
            if response.status_code == 200:
                bot_reply = response.json().get("response", "Error: No response received")
            else:
                bot_reply = f"Error: Server returned status code {response.status_code}"
        
        except requests.exceptions.RequestException:
            bot_reply = "Error: Unable to connect to the server"
        
        st.write(f"You: {user_input}")
        st.write(f"Bot: {bot_reply}")
