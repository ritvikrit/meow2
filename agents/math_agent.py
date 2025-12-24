from langgraph.prebuilt import create_react_agent
from ..tools.math_tool import add, multiply


def math_agent(model):
    return create_react_agent(
        model=model,
        tools=[add, multiply],
        name="math_expert",
        prompt="You are a math expert. Always use one tool at a time."
    )