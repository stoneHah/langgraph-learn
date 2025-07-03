"""
LangGraph Example Script

A simple example demonstrating basic LangGraph usage.
"""

import os
from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class GraphState:
    """State class for the LangGraph."""
    
    def __init__(self):
        self.messages = []
        self.context = {}


def chat_node(state: GraphState) -> Dict[str, Any]:
    """Chat node that processes user input."""
    print("Processing in chat node...")
    
    # Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Get the last message
    if state.messages:
        user_message = state.messages[-1]
        response = llm.invoke(f"User: {user_message}")
        state.messages.append(f"Assistant: {response.content}")
    
    return {"messages": state.messages}


def create_simple_graph():
    """Create a simple LangGraph workflow."""
    
    # Create the graph
    workflow = StateGraph(GraphState)
    
    # Add nodes
    workflow.add_node("chat", chat_node)
    
    # Set entry point
    workflow.set_entry_point("chat")
    
    # Set finish point
    workflow.set_finish_point("chat")
    
    # Compile the graph
    app = workflow.compile()
    
    return app


def main():
    """Main function to run the example."""
    print("LangGraph Example - Simple Chat Bot")
    print("=" * 40)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("请先设置 OPENAI_API_KEY 环境变量！")
        print("可以创建 .env 文件并添加：OPENAI_API_KEY=your_key_here")
        return
    
    # Create the graph
    app = create_simple_graph()
    
    # Initialize state
    initial_state = GraphState()
    initial_state.messages = ["Hello, how can you help me today?"]
    
    # Run the workflow
    try:
        result = app.invoke(initial_state)
        
        print("对话结果:")
        for message in result["messages"]:
            print(f"  {message}")
            
    except Exception as e:
        print(f"运行出错: {e}")
        print("请检查您的API密钥和网络连接。")


if __name__ == "__main__":
    main() 