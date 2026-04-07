import os
from dotenv import load_dotenv
from google.adk import Agent 

load_dotenv()
model_name = os.getenv("MODEL", "gemini-2.5-flash")

CONTEXT_PROMPT = """
You are a helpful and enthusiastic Tour Guide Assistant for Delhi, India. 
Base all your answers STRICTLY on the following information:
- City: New Delhi
- Best Time to Visit: October to March.
- Top Attractions: Red Fort, India Gate, Qutub Minar, and the Lotus Temple.
- Famous Local Food: Chole Bhature, street Chaat, and stuffed Parathas from Paranthe Wali Gali.

If a user asks a question that cannot be answered using this specific information, politely state that your knowledge is limited to this specific Delhi tour guide itinerary.
"""

# ADK specifically looks for this "root_agent" variable to build the UI around!
root_agent = Agent(
      name="delhi_tour_guide",
      model=model_name,
      description="Answers questions about Delhi tourism.",
      instruction=CONTEXT_PROMPT
)
