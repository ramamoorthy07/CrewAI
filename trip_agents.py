from crewai import Agent
from langchain_groq import ChatGroq
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
import os
os.environ['GROQ_API_KEY']='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'
os.environ['SERPER_API_KEY']='1e6f4512db57f60d6f088b77058e4e31b44cbebd'

llm=ChatGroq(
  temperature=0,
  groq_api_key=os.environ['GROQ_API_KEY'],
  model_name="llama3-8b-8192",

)
class TripAgents():

  def city_selection_agent(self):
    return Agent(
        role='City Selection Expert',
        goal='Select the best city based on weather, season, and prices',
        backstory=
        'An expert in analyzing travel data to pick ideal destinations',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
        allow_delegation=False,
        llm=llm)

  def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
        allow_delegation=False,
        llm=llm)

  def travel_concierge(self):
    return Agent(
        role='Amazing Travel Concierge',
        goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
        backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
            CalculatorTools.calculate,
        ],
        verbose=True,
        allow_delegation=False,
        llm=llm)
