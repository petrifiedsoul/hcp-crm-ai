import json
import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def extract_interaction_details(text: str) -> dict:
    """Helper to extract structured JSON from user text."""
    today_date = datetime.today().strftime('%Y-%m-%d')
    
    prompt = f"""Extract interaction details from the text below into JSON format with these exact keys:
    "hcpName", "date", "topics", "sentiment", "materials".
    
    CRITICAL RULES:
    - If the text says "today", use this exact date: {today_date}
    - ALWAYS format the "date" key strictly as YYYY-MM-DD.
    - If a specific piece of information is NOT mentioned in the text, YOU MUST return an empty string "".
    - For "sentiment", ONLY use "Positive", "Neutral", or "Negative" if a reaction is explicitly described. Otherwise, strictly use "".
    
    Return ONLY raw JSON.
    Text: {text}"""
    
    try:
        response = llm.invoke(prompt)
        clean_json = response.content.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except Exception as e:
        # Also updated the fallback to use an empty string for sentiment
        return {"hcpName": "", "date": "", "topics": text, "sentiment": "", "materials": ""}