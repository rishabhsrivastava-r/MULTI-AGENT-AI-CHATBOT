# 🤖 Multi-Agent AI Chatbot

An **intelligent Multi-Agent AI Chatbot** built using **Python**, **Groq LLM**, and **Streamlit**. The application employs a **multi-agent architecture** where specialized AI agents collaborate under a central coordinator to process user queries, perform web searches, maintain conversation memory, and generate accurate, context-aware responses.

---

## 🚀 Features

* 🧠 Multi-Agent Architecture
* 🤖 Groq LLM Integration
* 🌐 Web Search Agent
* 📝 Conversation Memory
* 🎯 Intelligent Query Routing
* 💬 Interactive Streamlit Interface
* ⚡ Fast Response Generation
* 🔒 Secure API Key Management using `.env`
* 📚 Modular & Scalable Codebase
* 🧩 Easy to Extend with New Agents

---

# 📸 System Workflow

```text
                 User Query
                      │
                      ▼
            Coordinator Agent
         ┌────────────┼────────────┐
         │            │            │
         ▼            ▼            ▼
   Memory Agent   Web Agent   LLM Agent
         │            │            │
         └────────────┼────────────┘
                      ▼
                 Groq LLM API
                      │
                      ▼
               Final AI Response
```

---

# 🛠 Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python 3.11+  | Backend Development             |
| Streamlit     | Web Application                 |
| Groq API      | Large Language Model            |
| Requests      | Web Search API Calls            |
| JSON          | Data Exchange                   |
| Python-dotenv | Environment Variable Management |

---

# 📂 Project Structure

```text
Multi-Agent-AI-Chatbot/
│
├── app.py                 # Streamlit Application
├── coordinator.py         # Coordinates all AI agents
├── llm.py                 # Groq LLM Initialization
├── memory.py              # Conversation Memory Module
├── web_agent.py           # Web Search Agent
├── requirements.txt
├── .env                   # API Keys (Ignored by Git)
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/SharvatoshPandey21/Multi-Agent-AI-Chatbot.git

cd Multi-Agent-AI-Chatbot
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Key

Create a **.env** file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

> **Note:** Never upload your `.env` file or API keys to GitHub.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

# 🧠 How It Works

1. The user submits a query through the Streamlit interface.
2. The **Coordinator Agent** analyzes the request.
3. The query is routed to the appropriate specialized agents.
4. The **Memory Agent** retrieves relevant conversation history.
5. The **Web Agent** fetches real-time information when required.
6. The **LLM Agent** communicates with the Groq API.
7. Responses from all agents are combined.
8. The chatbot generates a final context-aware response.

---

# 📸 Demo

Add screenshots or GIFs here.

Example project structure:

```text
images/
    ├── home.png
    ├── chat.png
    └── demo.gif
```

---

# 📦 Requirements

```text
streamlit
groq
python-dotenv
requests
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🔮 Future Enhancements

* 🎙 Voice Chat Support
* 📄 PDF Question Answering
* 📁 File Upload Support
* 🧠 Retrieval-Augmented Generation (RAG)
* 🔗 LangGraph Integration
* 🗄 Vector Database Integration
* 🤖 Multi-LLM Support
* 🔐 User Authentication
* 💬 Persistent Chat History Database
* 🐳 Docker Deployment
* ☁ Cloud Deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**RISHABH SRIVASTAVA**

**B.Tech Computer Science & Engineering**

Shri Ramswaroop Memorial College of Engineering & Management

Lucknow, Uttar Pradesh, India

**GitHub:**

https://github.com/SharvatoshPandey21

---

# ⭐ Support

If you found this project helpful:

⭐ Star the repository

🍴 Fork the repository

🐞 Report Issues

🚀 Contribute to make it even better.
