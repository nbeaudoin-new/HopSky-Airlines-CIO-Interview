import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
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
    page_title="HopSky Airlines CIO Team",
    initial_sidebar_state="collapsed"
)

# Add CSS for styling
st.markdown("""
<style>
    .stImage > div > img {
        border-radius: 15px;
    }
    h1 {
        text-align: center;
    }
    .stChatInput {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 70% !important;
        max-width: 900px !important;
        padding: 20px !important;
    }
    .stChatInput > div > div > textarea {
        min-height: 120px !important;
        font-size: 18px !important;
        padding: 15px !important;
        line-height: 1.6 !important;
    }
    .main .block-container {
        padding-bottom: 200px;
    }
</style>
""", unsafe_allow_html=True)

# Header with image in upper right corner
col_header_left, col_header_right = st.columns([3, 1])
with col_header_left:
    st.markdown("<h1 style='text-align: center; margin-top: 0;'>HopSky Airlines CIO Team</h1>", unsafe_allow_html=True)
with col_header_right:
    try:
        st.image("image.png", width=150)
    except FileNotFoundError:
        pass  # Image not found, continue without it

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Large centered prompt box - Streamlit's chat_input is already at bottom, CSS handles centering
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

