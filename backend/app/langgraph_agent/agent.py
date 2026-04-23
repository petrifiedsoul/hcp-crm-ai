from langgraph.prebuilt import create_react_agent
from app.langgraph_agent.tools import tools_list
from app.services.llm import llm

agent = create_react_agent(llm, tools_list)