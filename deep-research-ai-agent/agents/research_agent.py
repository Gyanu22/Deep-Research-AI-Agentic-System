# import logging
# import os
# from dotenv import load_dotenv
# from langchain.agents import Tool, initialize_agent
# from langchain.agents.agent_types import AgentType
# from langchain_google_genai import ChatGoogleGenerativeAI
# from utils.tavily_tool import get_tavily_tool

# load_dotenv()
# logging.basicConfig(level=logging.INFO)

# def research_agent(user_query: str) -> str:
#     try:
#         # Initialize the Tavily search tool
#         tavily_tool = Tool(
#             name="tavily_search",
#             func=get_tavily_tool().run,
#             description="Web search using the Tavily API"
#         )

#         # Initialize the Gemini LLM
#         llm = ChatGoogleGenerativeAI(
#             model="gemini-2.0-flash-001",
#             temperature=0.6,
#             max_tokens=500,
#             timeout=None,
#             max_retries=2,
#             google_api_key=os.getenv("GOOGLE_API_KEY")
#         )

#         # Create the agent with Tavily tool and Gemini
#         agent = initialize_agent(
#             tools=[tavily_tool],
#             llm=llm,
#             agent=AgentType.OPENAI_FUNCTIONS,
#             verbose=True
#         )

#         # Explicit prompt to guide Gemini to use the tool
#         tool_prompt = f"""
# Use the Tavily API to search the web and summarize this question:

# {user_query}

# Return a clear, informative answer based on the search.
# """

#         # Use invoke instead of run (run is deprecated)
#         search_results = agent.invoke({"input": tool_prompt})

#         search_prompt = f"Search the web and summarize the following query using Tavily:\n\n{user_query}"
#         search_results = agent.invoke({"input": search_prompt})


#         if "I can't directly answer" in str(search_results) or "would you like me to search" in str(search_results).lower():
#             logging.warning("Gemini skipped Tavily. Possibly tool wasn't triggered.")
#             return "No useful research data found."


#         # Detect if Gemini didn't use Tavily and returned useless output
#         bad_responses = ["I can't", "would you like me to search", "I don't have access"]
#         if any(phrase.lower() in str(search_results).lower() for phrase in bad_responses):
#             logging.warning("Gemini skipped Tavily. Possibly tool wasn't triggered.")
#             return "No useful research data found."

#         if not search_results or not str(search_results).strip():
#             logging.warning("Tavily or Gemini returned empty result.")
#             return "No useful research data found."

#         logging.info("Research agent executed successfully.")
#         return str(search_results)

#     except Exception as e:
#         logging.error(f"Research agent error: {e}")
#         return "An error occurred while performing the research."




import logging
import os
from dotenv import load_dotenv
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.tavily_tool import get_tavily_tool

load_dotenv()
logging.basicConfig(level=logging.INFO)

def research_agent(user_query: str) -> str:
    try:
        tavily_tool = Tool(
            name="tavily_search",
            func=get_tavily_tool().run,
            description="Web search using the Tavily API"
        )

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-001",
            temperature=0.6,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

        agent = initialize_agent(
            tools=[tavily_tool],
            llm=llm,
            agent=AgentType.OPENAI_FUNCTIONS,
            verbose=True
        )

        tool_prompt = f"""
Use the Tavily API to search the web and summarize this question:

{user_query}

Return a clear, informative answer based on the search.
"""

        search_results = agent.invoke({"input": tool_prompt})

        bad_responses = [
            "I can't", "would you like me to search", "I don't have access"
        ]
        if any(phrase.lower() in str(search_results).lower() for phrase in bad_responses):
            logging.warning("Gemini skipped Tavily. Possibly tool wasn't triggered.")
            return "No useful research data found."

        if not search_results or not str(search_results).strip():
            logging.warning("Tavily or Gemini returned empty result.")
            return "No useful research data found."

        logging.info("Research agent executed successfully.")
        return str(search_results)

    except Exception as e:
        logging.error(f"Research agent error: {e}")
        return "An error occurred while performing the research."
