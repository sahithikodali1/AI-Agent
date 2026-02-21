#import libraries and packages
import sys
import os
from pathlib import Path

from fastapi import FastAPI
#import classes
from agents.travel_planner_agent import TravelPlannerAgent
from agents.content_curator_agent import ContentCuratorAgent
from backend.database import init_db, save_session
from backend.schemas import TravelRequest, TravelResponse

#add path to parent folder [only testing purpose]
# sys.path.append(str(Path(__file__).resolve().parent))

#controller (API) - service layer (agents) - model (llm)
# 1. User clicks button (Frontend)
# 2. POST request sent
# 3. FastAPI receives JSON
# 4. Pydantic validates
# 5. Planner Agent runs
# 6. Curator Agent runs
# 7. Data saved
# 8. JSON returned
# 9. Frontend renders

# ✅ API Controller - FAST API
# ✅ Schema Validation Layer - Pydantic
# ✅ Multi-Agent Service Layer - Planner -> curator
# ✅ Persistence Layer - Database
# ✅ Async Endpoint - calls agents

# FastAPI() → creates server app
# @app.post() → registers endpoint
# Request arrives → router matches path
# FastAPI validates input (Pydantic)
# Function executes
# Return dict → auto JSON response

# | Concept  | Real World |
# | -------- | ---------- |
# | Endpoint | Menu item  |
# | API      | Waiter     |
# | Request  | Order      |
# | Backend  | Kitchen    |
# | Response | Food       |


#create web server instance - web application object (HTTP request/packet - communication to backend)
#fastAPI is framework
app = FastAPI(title="TravelAI Agent Hub")

# Instantiate Agents - only once and reuse these agents (singleton-style service)
planner_agent = TravelPlannerAgent()
curator_agent = ContentCuratorAgent()

#initialize Database once server starts
init_db()

#Use basemodel from Pydantic (data validation + parsing library) - handles all issues of traditional JSON
#basemodel provides validation - serialization - type coercion - docs generation automatically
#[old way] JSON data is read for required field - throw error when data is missing/data type mismatch

#API endpoint - URL+HTTP method to trigger code ; triggers function on server
#Register route to a function when a path is called
# Below means: function - gen_itinerary, mathod - POST, path - /generate_itinerary
# User Request
#      ↓
# Uvicorn Server
#      ↓
# FastAPI Router
#      ↓
# Matched Endpoint
#      ↓
# Your Function Runs
#      ↓
# Response Returned

# generate itinerary, given schema
@app.post("/generate_itinerary", response_model=TravelRequest) 

#async allows - concurrent users requests to not block; scalable APIs
#parameter injection to FASTAPI call; POST sends request to server
async def generate_itinerary(request: TravelRequest):
    # Travel Planner generates itinerary
    itinerary = planner_agent.generate_itinerary(
        location=request.location,
        days=request.days,
        interests=request.interests
    )

    # Content Curator generates content for each day
    content = curator_agent.generate_content(itinerary) #A2A communication: Planner -> curator

    # Save session in DB
    save_session(request.model_dump(), itinerary, content) # db can't store class objects, so convert to dict

    return {"itinerary": itinerary, "content": content} #fastAPI converts to JSON - instead of calling json.dumps()