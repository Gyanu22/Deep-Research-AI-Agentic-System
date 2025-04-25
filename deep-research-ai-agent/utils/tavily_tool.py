import os
from dotenv import load_dotenv
import logging
from langchain_community.tools.tavily_search.tool import TavilySearchResults

load_dotenv()
logging.basicConfig(level=logging.INFO)

def get_tavily_tool(k=5):
    """
    Initialize TavilySearchResults tool with top 5 search results.
    Requires TAVILY_API_KEY in .env or environment variables.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        logging.warning("⚠️ TAVILY_API_KEY not found in environment variables.")
    
    return TavilySearchResults(k=5, api_key=api_key)
