import json
from fastapi import APIRouter
from app.langgraph_agent.agent import agent

router = APIRouter()

@router.post("/chat")
def chat(data: dict):
    # We pass the system prompt directly in the message history here!
    system_prompt = """You are an intelligent CRM assistant for Life Science reps. 
    Always use your tools to log interactions, edit data, or fetch history. 
    After using a tool, give a brief, polite confirmation message to the user."""

    # Invoke the LangGraph Agent
    response = agent.invoke({
        "messages": [
            ("system", system_prompt),
            ("user", data["message"])
        ]
    })

    # The conversational reply from the AI
    final_message = response["messages"][-1].content
    
    # Extract the structured JSON from the tool call to send to your frontend
    structured_data = None
    for msg in reversed(response["messages"]):
        if msg.type == "tool" and msg.name in ["log_interaction", "edit_interaction"]:
            try:
                structured_data = json.loads(msg.content)
                break
            except:
                pass

    return {
        "reply": final_message,
        "data": structured_data
    }