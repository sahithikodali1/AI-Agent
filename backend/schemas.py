from pydantic import BaseModel
from typing import List, Dict

#Use basemodel from Pydantic (data validation + parsing library) - handles all issues of traditional JSON
#basemodel provides validation - serialization - type coercion - docs generation automatically
#[old way] JSON data is read for required field - throw error when data is missing/data type mismatch

class TravelRequest(BaseModel):
    location: str
    days: int
    interests: List[str]

class TravelResponse(BaseModel):
    itinerary: Dict[str, list]
    content: Dict[str, str]