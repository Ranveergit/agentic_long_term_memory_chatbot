# 🧠 Agentic Long-Term Memory Chatbot

An advanced chatbot framework built using **OpenAI's GPT models**, featuring:

- 🤖 Conversational memory management (SQL + Vector DB)  
- 🧠 Agentic behavior through **function calling**  
- 🌐 Gradio-powered UI for seamless interaction  

Supports three intelligent chatbot variants designed for different memory and reasoning needs.

---

## 🔥 Chatbot Variants

| Version | Description |
|--------|-------------|
| 🤖 **Basic Chatbot** | Tracks session history and user info using SQL. Great for lightweight memory-aware conversations. |
| 🧠 **Agentic Chatbot v2** | Adds OpenAI **function calling** with long-term SQL memory and fallback logic. |
| 🧠 **Agentic Chatbot v3** | Introduces **ChromaDB vector memory** and hybrid retrieval (SQL + embeddings). Ideal for deep, semantic memory conversations. |

---

## 📁 Project Structure


Agentic-LongTerm-Memory/
├── config/
│ └── config.yml # Configuration for models, DB, etc.
├── src/
│ ├── utils/
│ │ ├── chat_in_terminal.py # CLI interface
│ │ ├── chat_in_ui.py # Gradio UI logic
│ │ ├── basic_chatbot_v1.py # Basic memory chatbot
│ │ ├── chatbot_agentic_v2.py # Agent with SQL tools
│ │ ├── chatbot_agentic_v3.py # Agent with ChromaDB support
│ ├── prepare_sqldb.py # Initializes SQL schema
│ ├── prepare_vectordb.py # Initializes ChromaDB
│ ├── check_sqldb.py # SQL DB test script
│ ├── check_vectordb.py # ChromaDB test script
│ ├── startfile.py # Launches the Gradio app
├── requirements.txt
└── README.md


---

## 🚀 Setup & Run

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt

python startfile.py




