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
    graph.add_node('search',       search_web)
    graph.add_node('write_report', write_report)
    graph.set_entry_point('search')
    graph.add_edge('search',       'write_report')
    graph.add_edge('write_report', END)
    return graph.compile()

# ── Research Function (called by app.py) ───────────────────────────────────────
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


# ══════════════════════════════════════════════════════════════════════════════
# CHAT AI — General Purpose Assistant
# ══════════════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT = """You are ResearchAI Assistant — a smart, friendly AI that can help with:
- Any general questions (science, history, technology, culture, etc.)
- Mathematical calculations and equation solving (show your working step by step)
- Generating flowcharts and diagrams using Mermaid.js syntax
- Research topics and explanations

IMPORTANT RULES FOR FLOWCHARTS:
- When asked for any flowchart, diagram, or visual, ALWAYS use Mermaid syntax.
- STRICT MERMAID RULES to avoid syntax errors:
  * Use ONLY simple square brackets for nodes: A[Label]
  * NEVER use parentheses () or curly braces in node labels
  * NEVER use colons : inside node labels
  * NEVER use quotes inside node labels
  * Keep labels SHORT — max 4 words per node
  * Always start with: flowchart TD
  * Example of CORRECT syntax:
```mermaid
    flowchart TD
        A[User Request] --> B[Search Web]
        B --> C[Analyze Data]
        C --> D[Write Report]
        D --> E[Done]
```
  * Example of WRONG syntax:
    A[User: sends request (POST)] ← has colon and parentheses

IMPORTANT RULES FOR MATH:
- When solving equations or doing calculations, show each step clearly.
- Use plain text math notation (e.g., x^2, sqrt(x), pi).
- Put the final answer on its own line starting with "Answer:"

Be concise, accurate, and helpful. Format responses with markdown where useful."""


def chat_with_ai(messages: list) -> str:
    """
    Send a multi-turn conversation to Groq LLaMA3 and get a response.
    
    messages: list of dicts like [{"role": "user", "content": "..."}, ...]
    Returns: AI response string
    """
    llm = ChatGroq(
        model_name='llama-3.3-70b-versatile',
        api_key=os.getenv('GROQ_API_KEY'),
        temperature=0.7,
        max_tokens=2048
    )

    # Build the full message list with system prompt first
    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    response = llm.invoke(full_messages)
    return response.content


def solve_math(expression: str) -> str:
    """
    Try to solve a math expression precisely using sympy.
    Returns a formatted string with the result, or empty string on failure.
    """
    try:
        import sympy as sp
        # Try to parse and evaluate the expression
        result = sp.sympify(expression)
        simplified = sp.simplify(result)
        # Check if it's an equation (contains =)
        if '=' in expression:
            lhs, rhs = expression.split('=', 1)
            lhs_expr = sp.sympify(lhs.strip())
            rhs_expr = sp.sympify(rhs.strip())
            x = sp.Symbol('x')
            solutions = sp.solve(lhs_expr - rhs_expr, x)
            if solutions:
                return f"**Precise Solution (sympy):** x = {', '.join(str(s) for s in solutions)}"
        else:
            return f"**Precise Result (sympy):** {simplified}"
    except Exception:
        return ""