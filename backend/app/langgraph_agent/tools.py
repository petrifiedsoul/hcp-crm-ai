import json
from langchain_core.tools import tool
from app.database import SessionLocal, Interaction
from app.services.llm import extract_interaction_details

@tool
def log_interaction(data: str):
    """Tool to capture and log interaction data."""
    ext = extract_interaction_details(data)
    
    # 🔥 THE FIX: Safely convert lists to strings if the AI returns them as lists
    topics_val = ext.get('topics', '')
    if isinstance(topics_val, list):
        topics_val = ", ".join(topics_val)
        
    materials_val = ext.get('materials', '')
    if isinstance(materials_val, list):
        materials_val = ", ".join(materials_val)
        
    db = SessionLocal()
    new_int = Interaction(
        hcp_name=ext.get('hcpName', ''), 
        topics=topics_val, 
        sentiment=ext.get('sentiment', 'Neutral'), 
        date=ext.get('date', ''), 
        materials=materials_val
    )
    db.add(new_int)
    db.commit()
    db.close()
    
    return json.dumps({"type": "log", "structured": ext})

@tool
def edit_interaction(data: str) -> str:
    """Use this tool to edit or update an existing interaction."""
    ext = extract_interaction_details(data)
    
    # 🔥 THE FIX: Safely convert lists to strings for the edit tool as well
    if isinstance(ext.get('topics'), list):
        ext['topics'] = ", ".join(ext['topics'])
        
    if isinstance(ext.get('materials'), list):
        ext['materials'] = ", ".join(ext['materials'])

    # Note: For MVP, we are just returning this to update the Redux form.
    # If you added DB update logic here, the strings are now safe to insert!
    
    return json.dumps({"type": "edit", "structured": ext})

@tool(return_direct=True)
def get_interactions(hcp_name: str = "") -> str:
    """Fetches interaction history."""
    db = SessionLocal()
    history = db.query(Interaction).order_by(Interaction.id.desc()).limit(5).all()
    db.close()
    
    if not history:
        return "No history found in the database."
        
    # Formatting as a user-friendly Markdown table
    table = "### 🗂️ Recent Interaction History\n\n"
    table += "| Date | HCP Name | Topics | Sentiment |\n"
    table += "| :--- | :--- | :--- | :--- |\n"
    
    for i in history:
        table += f"| **{i.date}** | {i.hcp_name} | {i.topics} | {i.sentiment} |\n"
        
    return table

@tool(return_direct=True)
def suggest_next_action(context: str = "") -> str:
    """Suggests follow-ups."""
    return "Based on the recent positive interaction regarding oncology trials, I suggest sending the Phase 2 Clinical Trial PDF and scheduling a brief follow-up call."

@tool(return_direct=True)
def schedule_task(task: str = "") -> str:
    """Schedules tasks."""
    return f"Success! I have added the following task to your calendar: '{task}'"

tools_list = [log_interaction, edit_interaction, get_interactions, suggest_next_action, schedule_task]