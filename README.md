_**TravelAI Agent Hub 🌍🤖**_

A multi-agent AI system to plan travel itineraries and generate engaging content for each day. Built using LangChain, Gemini API (Google), FastAPI, and Streamlit.

**Features:**
1. Travel Planner Agent: Generates full-day itineraries based on destination, number of days, and interests.
2. Content Curator Agent: Enhances each day's plan into engaging paragraphs.
3. Multi-Agent Workflow: Planner → Curator (A2A communication).
4. Front-end Dashboard: Built with Streamlit to interact with the agents.
5. Database Persistence: Stores user requests and generated itineraries.
6. FastAPI backend.

**Tech Stack:**
- Python 3.10+
- LangChain – orchestrate LLM calls
- langchain-google-genai – Gemini model integration
- FastAPI – backend API server
- Streamlit – frontend UI
- SQLite – persistence

**To-Do:**
1. Lang Graph implementation
2. Persistent Memory (DB and across sessions)
3. Multi-agent communication
4. MCP and A2A setup
5. Multiple sessions
6. Cloud Deployment
