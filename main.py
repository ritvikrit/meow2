from langchain_openai import ChatOpenAI
from orchestrator.langgraph_supervisor import build_workflow

model = ChatOpenAI(model="gpt-4o")

workflow = build_workflow(model)
app = workflow.compile()

result = app.invoke({
    "messages": [
        {"role": "user", "content": "what is 12 * 8?"}
    ]
})

for m in result["messages"]:
    m.pretty_print()
