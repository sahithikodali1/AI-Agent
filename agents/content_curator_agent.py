# content_curator_agent.py
from .agent_utils import run_llm

class ContentCuratorAgent:
    def __init__(self):
        self.name = "Content Curator"

    def generate_content(self, day_paragraph: str, style: str = "engaging, descriptive, friendly"):
        """
        Enhance a single day's paragraph from the Travel Planner Agent.
        Args:
            day_paragraph (str): Paragraph describing the day's itinerary
            style (str): Desired writing style / tone
        Returns:
            str: Enhanced, polished paragraph
        """
        prompt = f"""
        You are a professional travel content writer.
        Rewrite the following itinerary paragraph in a {style} style,
        keeping all the activities, times, and places, but making it more engaging and easy to read.
        Paragraph to enhance:
        \"\"\"{day_paragraph}\"\"\"
        """
        enhanced_text = run_llm(prompt)
        return enhanced_text

    def curate_full_itinerary(self, itinerary_json: dict, style: str = "engaging, descriptive, friendly"):
        """
        Enhance the entire itinerary day-wise.
        Args: itinerary_json (dict): {"day_1": [para1, para2, ..], "day_2": [..], ...}
        Returns: dict: {"day_1": [enhanced_para1, enhanced_para2, ..], "day_2": [..], ...}
        """
        curated_itinerary = {}
        for day, paras in itinerary_json.items():
            enhanced_paras = [self.generate_content(p, style) for p in paras]
            curated_itinerary[day] = enhanced_paras
        return curated_itinerary