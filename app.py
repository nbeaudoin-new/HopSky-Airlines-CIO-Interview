import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read system prompt from prompt.txt
try:
    with open("prompt.txt", "r") as f:
        system_prompt = f.read().strip()
except FileNotFoundError:
    st.error("Error: prompt.txt file not found. Please create it with a system prompt.")
    st.stop()
    system_prompt = "You are a helpful assistant."

# Validate OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Error: OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")
    st.stop()

# Initialize LangChain ChatOpenAI model
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key, temperature=0.7)

# Streamlit UI Configuration
st.set_page_config(
    page_title="AeroVista CIO Bot",
    initial_sidebar_state="collapsed"
)

# Header
st.header("AeroVista CIO Bot")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Call LangChain LLM with system prompt + user message
    messages = [SystemMessage(content=system_prompt)]
    for msg in st.session_state.messages[:-1]:  # All messages except the current user input
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))  # Assistant messages
    
    messages.append(HumanMessage(content=user_input))
    
    # Get response from LLM
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(messages)
            assistant_response = response.content
            
            # Display assistant response
            st.markdown(assistant_response)
    
    # Append assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

