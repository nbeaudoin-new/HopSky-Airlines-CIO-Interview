# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app locally
streamlit run app.py
```

The app runs at `http://localhost:8501` by default. An `OPENAI_API_KEY` must be set in a `.env` file (or as a Streamlit Cloud secret) before the app will start.

## Architecture

This is a single-file Streamlit chatbot (`app.py`) with no backend, database, or routing layer.

**Startup flow:**
1. `load_dotenv()` pulls `OPENAI_API_KEY` from `.env`
2. `prompt.txt` is read and cached via `@st.cache_resource` — this is the entire CIO persona and ground-truth facts
3. A `ChatOpenAI(model="gpt-4o-mini")` instance is initialized and cached
4. Streamlit renders the UI: logo (`image.png`) top-right, a centered title, a large hero image (`image 2.png`), then the chat area

**Per-message flow:**
- On user input, the full conversation history from `st.session_state.messages` is rebuilt into LangChain message objects (`SystemMessage`, `HumanMessage`, `AIMessage`) and sent to the LLM in a single `llm.invoke()` call
- Session state is in-memory only — refreshing the page resets the conversation

**Key design constraints:**
- The system prompt in `prompt.txt` is the product. It defines the CIO persona, seven "Red Signal" ground truths about HopSky Airlines, and example Q&A pairs. Changes to `prompt.txt` directly change how the chatbot behaves — no code changes needed.
- The app is intentionally stateless and has no persistence layer.
- Deployed to Streamlit Community Cloud; `OPENAI_API_KEY` is configured as a Streamlit secret there.
