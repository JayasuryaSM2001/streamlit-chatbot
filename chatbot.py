import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = "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"

st.title("AI Chatbot 💬")
st.write("Ask me anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.text_input("You:", key="user_input")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )

    bot_reply = response["choices"][0]["message"]["content"]

    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display bot response
    with st.chat_message("assistant"):
        st.write(bot_reply)
