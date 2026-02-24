from agents.agent_utils import run_llm
import json

class TravelPlannerAgent:
    def __init__(self):
        self.name = "Travel Itinerary Planner"

    def generate_and_curate_itinerary(self, location: str, days: int, interests: list, style: str = "engaging, descriptive, friendly"):
        """
        Single function that:
        1️⃣ Generates multi-day itinerary in paragraphs (1 call)
        2️⃣ Enhances the full itinerary in one pass (1 call)
        Total API calls: 2
        """
        # 1.Generate full itinerary
        generate_prompt = f"""
        You are a travel planner.
        Plan a {days}-day trip for {location} based on these interests: {interests}.
        Write the full itinerary as paragraphs for each day, including approximate times and activities.
        Each day should start with "Day X:" followed by a descriptive paragraph.
        Return plain text, no JSON or lists.
        """
        raw_itinerary = run_llm(generate_prompt)

        # # 22.Curate / enhance in one go
        # enhance_prompt = f"""
        # You are a professional travel content writer.
        # Enhance the following itinerary in a {style} style.
        # Keep all activities, timings, and places, but make it more engaging, smooth, and readable.

        # Itinerary:
        # {raw_itinerary}
        # """
        # curated_itinerary = run_llm(enhance_prompt)

        return raw_itinerary
    
