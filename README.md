🧠 Agentic Long-Term Memory Chatbot
This project contains an advanced chatbot framework built with OpenAI models, agentic behavior, long-term memory support via SQL & ChromaDB, and a Gradio-powered UI. It supports three chatbot variants:

🤖 Basic Chatbot – Tracks session history and user info.

🧠 Agentic Chatbot v2 – Enables tool-calling, long-term SQL memory, and summarization.

🧠 Agentic Chatbot v3 – Adds ChromaDB vector memory with hybrid search capabilities.

📁 Project Structure
graphql
Copy
Edit
Agentic-LongTerm-Memory/
├── config/
│   └── config.yml                  # Configs for models, DB, etc.
├── src/
│   ├── utils/
│   │   ├── chat_in_terminal.py     # CLI interface
│   │   ├── chat_in_ui.py           # Gradio UI logic
│   │   ├── basic_chatbot_v1.py     # Basic memory chatbot
│   │   ├── chatbot_agentic_v2.py   # Agent with SQL tools
│   │   ├── chatbot_agentic_v3.py   # Agent with ChromaDB
│   ├── prepare_sqldb.py            # Sets up SQL schema
│   ├── prepare_vectordb.py         # Initializes ChromaDB
│   ├── check_sqldb.py              # Tests SQL setup
│   ├── check_vectordb.py           # Tests vector DB setup
│   ├── startfile.py                # Entry script to launch everything
├── requirements.txt
└── README.md                       # ← You are here
🚀 Setup & Run
🧩 1. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
Make sure your OpenAI key and database credentials are set via .env or config/config.yml.

🧠 2. Prepare Memory Backends
Run this once to initialize memory systems:

bash
Copy
Edit
python src/prepare_sqldb.py
python src/prepare_vectordb.py
🖥️ 3. Launch the Chatbot UI
bash
Copy
Edit
python startfile.py
This launches a Gradio UI at http://localhost:7860 or the port chosen by your deployment platform.

🤖 Chatbot Versions
🧱 Basic Chatbot (v1)
A simple chatbot that:

Tracks chat history in a SQL DB

Maintains a short-term summary

Adapts replies based on user info

Use case: lightweight, memory-aware conversations.

🧠 Agentic Chatbot v2
Adds function-calling tools and a loop-based prompt strategy:

Searches SQL-based history

Adds or retrieves user data

Allows OpenAI to invoke tools like search_chat_history()

Supports fallback handling

Use case: More dynamic, stateful conversations.

🧠 Agentic Chatbot v3
Adds ChromaDB (vector DB) support for long-term semantic memory:

Indexes chat summaries and turns as embeddings

Supports hybrid retrieval (SQL + vector)

Adds contextually relevant past data to the prompt

Use case: Deep memory, RAG-style interaction using structured + unstructured memory.

🧪 Testing & Validation
You can test whether your memory components are working via:

bash
Copy
Edit
python src/check_sqldb.py
python src/check_vectordb.py
📊 Architecture Diagrams
Basic Chatbot v1


Agentic Chatbot v2


Agentic Chatbot v3 (Coming Soon!)
Add a diagram like chatbot_agentic_v3.png to images/ if available.

🛠 Tech Stack
Layer	Tool
LLM API	OpenAI Chat Models
UI	Gradio
Memory (short)	SQLite
Memory (long)	ChromaDB
Orchestration	Custom Python with function calling

📌 Notes
You can switch between chatbot versions using the dropdown in the Gradio UI.

startfile.py automatically runs the appropriate setup scripts and starts the app.

Custom tools and functions are stored in the utils and integrated into each chatbot.

