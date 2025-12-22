import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Validate OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Error: OPENAI_API_KEY not found in environment variables. Please set it in your .env file or Streamlit Cloud secrets.")
    st.stop()

@st.cache_resource
def load_system_prompt():
    """Load and cache the system prompt from prompt.txt"""
    try:
        with open("prompt.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None  # Return None to handle error outside cached function

@st.cache_resource
def initialize_llm():
    """Initialize and cache the LangChain ChatOpenAI model"""
    return ChatOpenAI(model="gpt-4o-mini", api_key=api_key, temperature=0.7)

# Load system prompt (cached)
system_prompt = load_system_prompt()
if system_prompt is None:
    st.error("Error: prompt.txt file not found. Please create it with a system prompt.")
    st.stop()
    system_prompt = "You are a helpful assistant."

# Initialize LLM (cached)
llm = initialize_llm()

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
        white-space: nowrap;
        overflow: hidden;
    }
    .stChatInput {
        position: fixed;
        bottom: 40px !important;
        left: 50%;
        transform: translateX(-50%);
        width: 70% !important;
        max-width: 900px !important;
        padding: 20px !important;
    }
    .stChatInput > div > div > textarea {
        min-height: 180px !important;
        font-size: 18px !important;
        padding: 15px !important;
        line-height: 1.6 !important;
    }
    .main .block-container {
        padding-bottom: 260px;
    }
</style>
""", unsafe_allow_html=True)

# Header with logo in upper right corner
col_header_left, col_header_right = st.columns([3, 1])
with col_header_left:
    st.markdown("<h1 style='text-align: center; margin-top: 0; white-space: nowrap;'>HopSky Airlines CIO Team</h1>", unsafe_allow_html=True)
with col_header_right:
    try:
        st.image("image.png", width=150)
    except (FileNotFoundError, Exception) as e:
        # Logo not found or error loading - continue without it
        pass

# Large centered image 2 - much bigger
col_img_left, col_img_center, col_img_right = st.columns([0.3, 3, 0.3])
with col_img_center:
    try:
        st.image("image 2.png", use_container_width=True)
    except (FileNotFoundError, Exception) as e:
        # Image not found or error loading - continue without it
        pass

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
            try:
                response = llm.invoke(messages)
                assistant_response = response.content
                
                # Display assistant response
                st.markdown(assistant_response)
                
                # Append assistant response to session state
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                error_message = f"Sorry, I encountered an error: {str(e)}. Please try again."
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

