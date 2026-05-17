from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from dotenv import load_dotenv
import os

load_dotenv()

# ── Agent's Notebook (remembers everything) ────────────────────────────────────
class AgentState(TypedDict):
    topic: str
    search_results: str
    report: str
    steps: List[str]

# ── Step 1: Search the Internet ────────────────────────────────────────────────
def search_web(state: AgentState):
    search = TavilySearchResults(
        max_results=5,
        tavily_api_key=os.getenv('TAVILY_API_KEY')
    )
    results = search.invoke(state['topic'])
    content = '\n\n'.join([r['content'] for r in results])
    state['search_results'] = content
    state['steps'].append('Searched web for: ' + state['topic'])
    return state

# ── Step 2: Write the Report ───────────────────────────────────────────────────
def write_report(state: AgentState):
    llm = ChatGroq(
        model_name='llama-3.3-70b-versatile',
        api_key=os.getenv('GROQ_API_KEY')
    )
    prompt = f"""You are a professional research analyst.
Based on the search results below, write a clear and structured 
research report on the topic: {state['topic']}

Search Results:
{state['search_results']}

Write the report with these sections:
- Executive Summary (3-4 sentences overview)
- Key Findings (5 bullet points)  
- Detailed Analysis (2-3 paragraphs)
- Conclusion (2-3 sentences)

Make it professional, clear and informative.
"""
    response = llm.invoke(prompt)
    state['report'] = response.content
    state['steps'].append('Research report written successfully')
    return state

# ── Build the Agent Graph (Flowchart) ──────────────────────────────────────────
def create_agent():
    graph = StateGraph(AgentState)

    # Add steps
    graph.add_node('search',       search_web)
    graph.add_node('write_report', write_report)

    # Define flow: search → write → done
    graph.set_entry_point('search')
    graph.add_edge('search',       'write_report')
    graph.add_edge('write_report', END)

    return graph.compile()

# ── Main Function (called by app.py) ───────────────────────────────────────────
def run_research(topic: str):
    agent = create_agent()
    initial_state = {
        'topic':          topic,
        'search_results': '',
        'report':         '',
        'steps':          []
    }
    result = agent.invoke(initial_state)
    return result['report'], result['steps']