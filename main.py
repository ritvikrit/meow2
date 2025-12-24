import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from langchain_google_genai import ChatGoogleGenerativeAI
from .orchestrator.langraph_supervisor import build_workflow


def main():
    model = ChatGoogleGenerativeAI(model="models/gemini-1.0-pro")

    workflow = build_workflow(model)
    app = workflow.compile()

    print("App compiled successfully! The multi-agent workflow is ready.")
    print("Workflow structure:")
    print(app.get_graph().draw_ascii())
    print("\nTo use it, invoke app with messages, e.g., app.invoke({'messages': [{'role': 'user', 'content': 'Your query'}]})")
    print("Note: Requires a valid Gemini API key with model access.")

    # App is ready to be used (FastAPI / CLI / scripts)


if __name__ == "__main__":
    main()
