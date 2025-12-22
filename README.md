# HopSky Airlines CIO Bot

A conversational AI chatbot built with Streamlit and LangChain, designed to facilitate interviews with Chief Information Officers (CIOs) and their technical teams.

## Purpose

This application is part of the **Caltech CTME (Center for Technology and Management Education) course** project, specifically designed to conduct interviews with CIOs and their technical teams. The chatbot serves as an intelligent interview assistant that can engage in meaningful conversations about technology leadership, strategic IT decisions, and technical implementations.

**Note**: HopSky Airlines is a fictional company based in Santa Fe, New Mexico, created for educational purposes as part of this course project.

## Features

- 🤖 **AI-Powered Conversations**: Powered by OpenAI's GPT-4o-mini model via LangChain
- 💬 **Interactive Chat Interface**: Clean, user-friendly Streamlit web interface
- 📝 **Customizable System Prompts**: System prompts loaded from `prompt.txt` for easy customization
- 🔒 **Secure API Key Management**: Environment variable-based configuration
- ☁️ **Cloud-Ready**: Designed for easy deployment on Streamlit Community Cloud
- 📊 **Session-Based Chat**: Maintains conversation context within each user session

## Tech Stack

- **Frontend**: Streamlit 1.28.0+
- **LLM Orchestration**: LangChain 0.1.0+
- **AI Model**: OpenAI GPT-4o-mini
- **Environment Management**: python-dotenv
- **Language**: Python 3.9+

## Project Structure

```
HopSky-Airlines-CIO-Interview/
├── app.py                 # Main Streamlit application
├── prompt.txt             # System prompt configuration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── Plan.md               # Project plan and task list
└── README.md             # This file
```

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- OpenAI API key
- pip (Python package manager)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nbeaudoin-new/HopSky-Airlines-CIO-Interview.git
   cd HopSky-Airlines-CIO-Interview
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

   The app will open in your browser at `http://localhost:8501`

### Customizing the System Prompt

Edit `prompt.txt` to customize the chatbot's behavior, personality, and interview focus. The system prompt defines how the AI will conduct interviews with CIOs and technical teams.

## Usage

1. **Start a conversation**: Type your message in the chat input at the bottom of the screen
2. **Send messages**: Press Enter or click the send button to submit your message
3. **View history**: All messages in the current session are displayed in the chat interface
4. **New session**: Refresh the page to start a new conversation (stateless design)

## Deployment

### Streamlit Community Cloud

This application is configured for easy deployment on Streamlit Community Cloud:

1. Push your code to a GitHub repository
2. Connect your repository to Streamlit Cloud
3. Set the `OPENAI_API_KEY` as a secret in Streamlit Cloud settings
4. Deploy!

The application will automatically redeploy when you push changes to the main branch.

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Model Configuration

The application uses GPT-4o-mini by default. You can modify the model in `app.py`:

```python
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key, temperature=0.7)
```

## Development

### Key Components

- **`app.py`**: Main application logic, UI components, and chat functionality
- **`prompt.txt`**: System prompt that defines the chatbot's role and behavior
- **`requirements.txt`**: Python package dependencies

### Architecture

- **Stateless Design**: Each user session is independent; no persistent storage
- **Session State**: Uses Streamlit's session state for in-page conversation history
- **LangChain Integration**: Leverages LangChain for LLM orchestration and message handling

## License

This project is part of the Caltech CTME course curriculum.

## Author

Developed as part of the Caltech CTME course project for interviewing CIOs and technical teams.

## Support

For issues or questions related to this project, please refer to the course materials or contact your instructor.

