from langgraph_supervisor import create_supervisor

from ..agents.math_agent import math_agent
from ..agents.research_agent import research_agent


def build_workflow(model):
    return create_supervisor(
        agents=[
            research_agent(model),
            math_agent(model),
        ],
        model=model,
        prompt=(
            "You are a supervisor managing:\n"
            "- research_agent for information\n"
            "- math_agent for calculations\n"
        ),
    )
