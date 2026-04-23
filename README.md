# 🏥 HCP CRM AI Agent - Task 1

An intelligent, AI-powered CRM designed for Healthcare Professional (HCP) management. This platform features a real-time conversational agent that automates data entry and retrieval using a multi-tool LangGraph workflow.

## ✨ Core Features
- **Contextual AI Chat:** Powered by LangGraph to route user intent to specific database or UI tools.
- **Automated Form Filling:** AI extracts HCP details from natural language and populates a Redux-managed form.
- **SQL Persistence:** All logged interactions are stored in a local MySQL database.
- **Modern UI:** Built with React, utilizing the **Google Inter** font and a responsive dual-pane layout.

## 🛠️ Tech Stack
- **Frontend:** React.js, Redux Toolkit, CSS3
- **Backend:** FastAPI (Python), Uvicorn
- **AI Orchestration:** LangGraph, LangChain, OpenAI/Gemini
- **Database:** MySQL 8.0, SQLAlchemy ORM

---

## 🤖 AI Agent Tools
The LangGraph agent is equipped with 5 specialized tools:
1. `log_interaction`: Parsed text into structured JSON and saves to MySQL.
2. `edit_interaction`: Allows conversational updates to the current form state.
3. `get_interactions`: Queries MySQL for historical data and returns a formatted table.
4. `suggest_next_action`: Provides strategic follow-up recommendations.
5. `schedule_task`: Simulates task/meeting scheduling based on user input.

---

## 🚀 Getting Started

###  Database Setup
Create a MySQL database named `hcp_crm` and run the following:
```sql
CREATE TABLE interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hcp_name VARCHAR(255),
    topics TEXT,
    sentiment VARCHAR(50),
    date VARCHAR(50),
    materials TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

---

## Backend Setup

cd backend
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload

---


## 3. Frontend Setup
cd frontend
npm install
npm start
