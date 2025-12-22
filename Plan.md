# Plan: Simple Streamlit + LangChain Chatbot

## Overview

This project implements a minimal chatbot web application.

* **Frontend**: Streamlit
* **LLM Orchestration**: LangChain
* **Model**: OpenAI GPT-4o-mini
* **System Prompt**: Reads from `prompt.txt`
* **API**: Uses OpenAI's API (via LangChain) to generate responses
* **Stateless**: The application is stateless, meaning no persistent memory; each user session is independent, and chat history is not stored between sessions
* **Design Goal**: Simple, deployable, and suitable for public Streamlit Community Cloud hosting

## Tasks

### Setup & Dependencies

- [ ] Create `requirements.txt` with the following dependencies:
  - `streamlit>=1.28.0`
  - `langchain>=0.1.0`
  - `langchain-openai>=0.0.5`
  - `python-dotenv>=1.0.0`
- [ ] Create `.env.example` template file with placeholder for `OPENAI_API_KEY`
- [ ] Create `.gitignore` to exclude `.env` and Python cache files

### Core Files

- [ ] Create `prompt.txt` with a sample system prompt (e.g., "You are a helpful assistant.")
- [ ] Create `app.py` as the main Streamlit application file

### Implementation in `app.py`

- [ ] Import required libraries: `streamlit`, `langchain`, `langchain_openai`, `dotenv`, `os`
- [ ] Load environment variables using `python-dotenv` (to load the `.env` file)
- [ ] Read system prompt from `prompt.txt` with error handling (for file not found)
- [ ] Validate `OPENAI_API_KEY` exists in the environment (show error if missing)
- [ ] Initialize LangChain ChatOpenAI model with `model="gpt-4o-mini"` and the API key from the environment
- [ ] Create Streamlit UI:
  - [ ] Set page title to "HopSky Airlines CIO Bot" using `st.set_page_config()` with `initial_sidebar_state="collapsed"` to disable the sidebar
  - [ ] Add a header displaying "HopSky Airlines CIO Bot"
  - [ ] Add text input for the user message
  - [ ] Add send button
  - [ ] Add display area for chat messages (using Streamlit session state for in-page display only)
- [ ] Implement chat logic:
  - [ ] Initialize session state for the messages list (if needed for UI)
  - [ ] On user input, append the user message to the session state
  - [ ] Call LangChain LLM with the system prompt + user message
  - [ ] Append the assistant response to the session state
  - [ ] Display all messages in chat format

