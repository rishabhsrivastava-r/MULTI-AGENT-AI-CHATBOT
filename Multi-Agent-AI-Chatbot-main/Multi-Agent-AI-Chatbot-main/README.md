# 🤖 Multi-Agent AI Chatbot

An intelligent **Multi-Agent AI Chatbot** built using **Python**, **Groq LLM**, and **Streamlit**. The chatbot uses multiple specialized AI agents coordinated by a central controller to answer user queries efficiently and accurately.

---

## 🚀 Features

- 🧠 Multi-Agent Architecture
- 🤖 Groq LLM Integration
- 🌐 Web Search Agent
- 📝 Conversation Memory
- 🎯 Intelligent Query Routing
- 💬 Interactive Streamlit Interface
- ⚡ Fast Response Generation
- 🔒 Secure API Key Management using `.env`

---

## 🛠️ Tech Stack

- Python 3.11+
- Streamlit
- Groq API
- Python-dotenv
- Requests
- JSON

---

## 📂 Project Structure

```
Multi-Agent-AI-Chatbot/
│
├── app.py               # Streamlit application
├── coordinator.py       # Coordinates all AI agents
├── llm.py               # Groq LLM initialization
├── memory.py            # Conversation memory
├── web_agent.py         # Web search agent
├── requirements.txt
├── .env                 # Environment variables (Not pushed to GitHub)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/SharvatoshPandey21/Multi-Agent-AI-Chatbot.git

cd Multi-Agent-AI-Chatbot
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

## 🧠 How It Works

```
                User Query
                     │
                     ▼
            Coordinator Agent
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     Memory Agent        Web Agent
          │                     │
          └──────────┬──────────┘
                     ▼
                 Groq LLM
                     │
                     ▼
               Final Response
```

---

## 📸 Demo

> Add screenshots or GIFs here.

Example:

```
images/demo.png
```

---

## 📦 Requirements

- Python 3.11+
- Groq API Key
- Internet Connection

---

## Future Improvements

- Voice Chat
- PDF Question Answering
- File Upload Support
- RAG Pipeline
- LangGraph Integration
- Vector Database
- Multi-LLM Support
- Authentication
- Chat History Database
- Docker Deployment

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sharvatosh Pandey**

B.Tech Computer Science & Engineering

Shri Ramswaroop Memorial College of Engineering & Management

Lucknow, Uttar Pradesh

GitHub:
https://github.com/SharvatoshPandey21

---

## ⭐ Support

If you like this project,

⭐ Star this repository

🍴 Fork the repository

🐞 Report issues

🚀 Contribute to improve the project.
