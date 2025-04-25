# from langgraph.graph import StateGraph, END
# from agents.research_agent import research_agent
# from agents.answer_agent import answer_agent
# import logging
# from dataclasses import dataclass

# logging.basicConfig(level=logging.INFO)

# @dataclass
# class ResearchState:
#     query: str
#     research_data: str = ""      # Holds Tavily/Gemini research summary
#     final_answer: str = ""       # Final answer from Gemini

# def research_node(state: ResearchState) -> ResearchState:
#     logging.info("🔍 Running research node...")
#     research_data = research_agent(state.query)
#     return ResearchState(query=state.query, research_data=str(research_data))

# def answer_node(state: ResearchState) -> ResearchState:
#     logging.info("🧠 Running answer node...")
#     final_answer = answer_agent(state.research_data)
#     return ResearchState(
#         query=state.query,
#         research_data=state.research_data,
#         final_answer=str(final_answer)
#     )

# def run_graph(query: str) -> dict:
#     initial_state = ResearchState(query=query)

#     workflow = StateGraph(state_schema=ResearchState)
#     workflow.add_node("do_research", research_node)
#     workflow.add_node("answer", answer_node)

#     workflow.set_entry_point("do_research")
#     workflow.add_edge("do_research", "answer")
#     workflow.add_edge("answer", END)

#     compiled = workflow.compile()
#     final_state = compiled.invoke(initial_state)

#     return final_state.__dict__  # Return as plain dict for Streamlit or API


from langgraph.graph import StateGraph, END
from agents.research_agent import research_agent
from agents.answer_agent import answer_agent
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class ResearchState:
    query: str
    research_data: str = ""
    final_answer: str = ""

def research_node(state: ResearchState) -> ResearchState:
    logging.info("🔍 Running research node...")
    research_data = research_agent(state.query)
    return ResearchState(query=state.query, research_data=str(research_data))

def answer_node(state: ResearchState) -> ResearchState:
    logging.info("🧠 Running answer node...")
    final_answer = answer_agent(state.research_data)
    return ResearchState(
        query=state.query,
        research_data=state.research_data,
        final_answer=str(final_answer)
    )

def run_graph(query: str) -> dict:
    initial_state = ResearchState(query=query)

    workflow = StateGraph(state_schema=ResearchState)
    workflow.add_node("do_research", research_node)
    workflow.add_node("answer", answer_node)

    workflow.set_entry_point("do_research")
    workflow.add_edge("do_research", "answer")
    workflow.add_edge("answer", END)

    compiled = workflow.compile()
    final_state = compiled.invoke(initial_state)

    return final_state.__dict__
