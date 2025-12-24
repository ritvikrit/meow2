from langgraph.prebuilt import create_react_agent
from ..tools.research_tool import web_search


def research_agent(model):
    return create_react_agent(
        model=model,
        tools=[web_search],
        name="research_expert",
        prompt="You are a world class researcher with access to web search. Do not do any math."
    )
