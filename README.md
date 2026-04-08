# Delhi Guide Agent

This is a helpful and enthusiastic AI Tour Guide Assistant for Delhi, India. 
Built using the [Google Agent Development Kit (ADK)](https://github.com/google/adk-python).

## Features
- Provides information on top attractions, food, and travel advice for Delhi.
- Strictly limited to its predefined knowledge base for accuracy.
- Developer UI included for testing and debugging.

## Setup
1. Clone this repository.
2. Install dependencies: `pip install google-adk python-dotenv`
3. Set up your `.env` file with `GOOGLE_API_KEY`.
4. Run the agent: `python app.py`

## Architecture
This agent uses the ADK Python framework to define a `delhi_tour_guide` agent with a structured system prompt.
