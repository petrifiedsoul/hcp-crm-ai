# 🏥 **HCP CRM AI - Intelligent Healthcare CRM**

An AI-powered **Customer Relationship Management (CRM)** platform designed specifically for Healthcare Professionals (HCPs). This application features a modern dual-pane interface with a real-time conversational agent powered by **LangGraph**, capable of managing data entry, retrieval, and strategic planning through a multi-tool workflow.

---

## ✨ **Key Features**
* **Intelligent AI Assistant:** A ReAct-based agent using **LangGraph** to autonomously route user requests to 5 specialized tools.
* **Automated Form Synchronization:** AI extracts structured data from natural language to update the **Redux-managed** CRM form instantly.
* **SQL Persistence:** All logged interactions are stored in a local **MySQL** database for long-term record-keeping.
* **Professional UI:** Designed with the **Google Inter** font, featuring a clean split-pane layout for simultaneous chat and data management.

---

## 🛠️ **Tech Stack**
* **Frontend:** React.js, Redux Toolkit, CSS3
* **Backend:** FastAPI (Python), Uvicorn
* **AI Orchestration:** LangGraph, LangChain
* **Database:** MySQL 8.0, SQLAlchemy ORM

---

## 🤖 **The 5 AI Tools**
The agent is equipped with the following capabilities:
1.  **`log_interaction`**: Parses conversation into JSON and saves it to the **MySQL** database.
2.  **`edit_interaction`**: Allows conversational updates/corrections to the current **UI form**.
3.  **`get_interactions`**: Queries the database for historical data and returns a formatted **Markdown table**.
4.  **`suggest_next_action`**: Provides strategic recommendations based on interaction sentiment.
5.  **`schedule_task`**: Simulates the scheduling of follow-up tasks and calendar events.

---

## 🚀 **Getting Started**

### 1. **Database Setup**
**Create a MySQL database** named `hcp_crm` and run the following SQL command to initialize the table:

```sql
CREATE DATABASE hcp_crm;
USE hcp_crm;

CREATE TABLE interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hcp_name VARCHAR(255),
    topics TEXT,
    sentiment VARCHAR(50),
    date VARCHAR(50),
    materials TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
### 2.**Backend Setup**
```bash
# Step A: Navigate to the backend directory
cd backend

# Step B: Create a Python Virtual Environment
python -m venv venv

# Step C: Activate the environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Step D: Install required dependencies
pip install fastapi uvicorn sqlalchemy pymysql langchain langgraph langchain-openai

# Step E: Launch the development server
uvicorn app.main:app --reload


```
The backend will be active at http://localhost:8000


### 3. **Frontend Setup**
```bash
# Step A: Navigate to the frontend folder
cd frontend

# Step B: Install the project dependencies
npm install

# Step C: Start the application
npm start
```
The UI will launch at http://localhost:3000

--- 

## 💡 **Usage Example**

Log: Type "I met with Dr. Adams today. We discussed oncology trials and the sentiment was very positive."

Edit: Type "Wait, change the sentiment to neutral."

History: Type "Show me my interaction history with Dr. Adams."

Action: Type "What should be my next follow-up step?"
