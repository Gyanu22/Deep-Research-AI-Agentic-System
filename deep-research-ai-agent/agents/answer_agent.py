# import os
# import logging
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()
# logging.basicConfig(level=logging.INFO)

# def answer_agent(research_summary):
#     try:
#         if not research_summary or not research_summary.strip():
#             raise ValueError("No valid research summary provided")

#         llm = ChatGoogleGenerativeAI(
#             model="gemini-2.0-flash-001",
#             google_api_key=os.getenv("GOOGLE_API_KEY"),
#             temperature=0.6
#         )

#         prompt = PromptTemplate(
#             input_variables=["info"],
#             template="""
# You are a knowledgeable assistant. Based on the following research information, write a clear, structured, and detailed answer to the user’s query.

# Research Info:
# {info}

# Instructions:
# - Use bullet points where appropriate
# - Avoid repetition
# - Ensure readability and conciseness
# """
#         )

#         # New: LangChain RunnableSequence pipeline
#         chain = prompt | llm | StrOutputParser()
#         final_answer = chain.invoke({"info": research_summary})

#         logging.info("Answer agent completed successfully.")
#         return final_answer

#     except Exception as e:
#         logging.error(f"Answer agent failed: {e}")
#         return "An error occurred while generating the final answer."



import os
import logging
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
logging.basicConfig(level=logging.INFO)

def answer_agent(research_summary):
    try:
        if not research_summary or not research_summary.strip():
            raise ValueError("No valid research summary provided")

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-001",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.3
        )

        prompt = PromptTemplate(
            input_variables=["info"],
            template="""
You are a knowledgeable assistant. Based on the following research information, write a clear, structured, and detailed answer to the user’s query.

Research Info:
{info}

Instructions:
- Use bullet points where appropriate
- Avoid repetition
- Ensure readability and conciseness
"""
        )

        chain = prompt | llm | StrOutputParser()
        final_answer = chain.invoke({"info": research_summary})

        logging.info("Answer agent completed successfully.")
        return final_answer

    except Exception as e:
        logging.error(f"Answer agent failed: {e}")
        return "An error occurred while generating the final answer."
