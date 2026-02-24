from agents.agent_utils import run_llm
import json

class TravelPlannerAgent:
    def __init__(self):
        self.name = "Travel Itinerary Planner"

    def generate_itinerary(self, location: str, days: int, interests: list):
        prompt = f"""
        You are a travel planning assistant. 
        Plan a {days}-day itinerary of the trip for {location} based on these interests: {interests}.
        Give a day-wise itinerary in paragraphs with approximate times at each location.
        Return the itinerary as a JSON object where keys are "day_1", "day_2", ..., "day_{days}" 
        and values are paragraphs describing the full day, including places to visit, timing, 
        and activities. Example:
        {{
            "day_1": "Morning: Visit Louvre Museum (2 hours), Afternoon: Walk around Notre Dame Cathedral (1 hour), Evening: Dinner at local cafe",
            "day_2": "..."
        }}
        Ensure the JSON is valid.
        """

        response = run_llm(prompt)

        # Safe parsing
        try:
            itinerary = json.loads(response)
        except json.JSONDecodeError:
            # Fallback: parse as lines if GPT fails to return JSON
            lines = [line.strip() for line in response.split("\n") if line.strip()]
            itinerary = {f"day_{i+1}": lines[i] if i < len(lines) else "" for i in range(days)}

        return itinerary
    
    