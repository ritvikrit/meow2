"""
Demo script showing the multi-agent system in action.
This demonstrates the workflow without requiring API keys.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from tools.math_tool import add, multiply
from tools.research_tool import web_search


def simulate_supervisor(query):
    """Simulate the supervisor deciding which agent to use."""
    print(f"Supervisor: Received query: '{query}'")
    
    if any(word in query.lower() for word in ['+', '-', '*', '/', 'calculate', 'math', 'sum', 'multiply', 'add']):
        print("Supervisor: Routing to math_agent")
        return "math"
    elif any(word in query.lower() for word in ['search', 'find', 'research', 'companies', 'info']):
        print("Supervisor: Routing to research_agent")
        return "research"
    else:
        print("Supervisor: Handling directly")
        return "direct"


def math_agent_demo(query):
    """Demonstrate math agent functionality."""
    print("Math Agent: Processing math query...")
    
    import re
    
    # Extract numbers and operators
    add_match = re.search(r'(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)', query)
    mult_match = re.search(r'(\d+(?:\.\d+)?)\s*\*\s*(\d+(?:\.\d+)?)', query)
    
    if add_match:
        a = float(add_match.group(1))
        b = float(add_match.group(2))
        result = add(a, b)
        response = f"The result of {a} + {b} is {result}"
    elif mult_match:
        a = float(mult_match.group(1))
        b = float(mult_match.group(2))
        result = multiply(a, b)
        response = f"The result of {a} * {b} is {result}"
    else:
        response = "I can perform basic math operations. Try queries like '5 + 3' or '4 * 7'."
    
    print(f"Math Agent: {response}")
    return response


def research_agent_demo(query):
    """Demonstrate research agent functionality."""
    print("Research Agent: Performing web search...")
    
    result = web_search(query)
    response = f"Search results: {result[:200]}..."
    
    print(f"Research Agent: {response}")
    return response


def interactive_demo():
    print("=== Interactive Multi-Agent System Demo ===\n")
    print("Enter queries like:")
    print("- '5 + 3' for addition")
    print("- '4 * 7' for multiplication") 
    print("- 'search FAANG' for research")
    print("- 'quit' to exit\n")
    
    while True:
        query = input("Enter your query: ").strip()
        if query.lower() == 'quit':
            break
            
        print(f"\n--- Processing: {query} ---")
        agent = simulate_supervisor(query)
        
        if agent == "math":
            response = math_agent_demo(query)
        elif agent == "research":
            response = research_agent_demo(query)
        else:
            response = "I can help with math calculations or research queries."
        
        print(f"Final Response: {response}")
        print("-" * 50)
    
    print("\n=== Demo Complete ===")


def demo():
    print("=== Multi-Agent System Demo ===\n")
    
    # Demo queries
    queries = [
        "What is 2 + 3?",
        "Find information about FAANG companies",
        "Calculate 4 * 5"
    ]
    
    for query in queries:
        print(f"\n--- Processing: {query} ---")
        agent = simulate_supervisor(query)
        
        if agent == "math":
            response = math_agent_demo(query)
        elif agent == "research":
            response = research_agent_demo(query)
        else:
            response = "I can help with math calculations or research queries."
        
        print(f"Final Response: {response}")
        print("-" * 50)
    
    print("\n=== Demo Complete ===")
    print("This shows how the supervisor routes tasks to specialized agents,")
    print("and how each agent uses its tools to complete tasks.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        interactive_demo()
    else:
        demo()