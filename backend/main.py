#import libraries and packages
from fastapi import FastAPI
from pydantic import BaseModel

#import classes
from agents.travel_planner_agent import TravelPlannerAgent
from agents.content_curator_agent import ContentCuratorAgent
from backend.database import init_db, save_session