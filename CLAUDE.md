# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LangGraph learning repository containing examples and tutorials for building AI workflows with LangGraph. The project includes Python scripts, Jupyter notebooks, and examples demonstrating chatbots, agents, memory management, routing, and parallelization patterns.

## Development Environment

### Dependencies
- Core: `langgraph`, `langchain[anthropic]`
- Install: `pip install -r requirements.txt`

### Environment Setup
Required environment variables (see `env.example`):
- `OPENAI_API_KEY`: For OpenAI models
- `ANTHROPIC_API_KEY`: For Claude models 
- `DASHSCOPE_API_KEY`: For Qwen models
- `LANGCHAIN_API_KEY`: For LangSmith tracing
- `LANGCHAIN_TRACING_V2=true`: Enable tracing
- `LANGCHAIN_PROJECT=langgraph-learn`: Project name

### Common Commands
- **Run tests**: `pytest tests/`
- **Run examples**: `python src/example_langgraph.py`
- **Start Jupyter**: `jupyter notebook` (for working with .ipynb files)

## Code Architecture

### Project Structure
- `src/`: Core Python modules with standalone LangGraph examples
- `examples/`: Educational notebooks and setup utilities
- `tests/`: Test files using pytest
- Root-level notebooks: Progressive learning tutorials (1_get_start.ipynb → 5_orchestrator_worker.ipynb)

### Key Patterns

#### LangGraph State Management
Uses TypedDict with Annotated message lists for state:
```python
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]
```

#### Memory/Checkpointing
- Uses `MemorySaver` or `InMemorySaver` for conversation persistence
- Thread-based conversation tracking with config: `{"configurable": {"thread_id": "1"}}`

#### Agent Creation
- Prebuilt agents: `create_react_agent(model, tools, prompt, checkpointer)`
- Custom graphs: `StateGraph(State)` with nodes, edges, and compilation

### Jupyter Async Considerations
The project includes special handling for asyncio in Jupyter environments:
- Use `examples/jupyter_setup.py` for async setup
- Prefer `await` over `asyncio.run()` in notebooks
- See `docs/ASYNCIO_JUPYTER.md` for detailed guidance

### LLM Integration
Supports multiple providers:
- OpenAI: `ChatOpenAI`
- Anthropic: `ChatAnthropic` 
- Custom endpoints (Qwen via DashScope)
- Base URL configuration for alternative APIs

## Development Guidelines

### File Organization
- Keep educational examples in numbered notebooks for learning progression
- Place reusable utilities in `src/`
- Async setup helpers in `examples/jupyter_setup.py`

### Error Handling
- Handle missing API keys gracefully with informative messages
- Use try-catch blocks around LLM calls
- Provide Chinese and English error messages where appropriate

### Testing
- Simple pytest structure in `tests/`
- Test basic functionality and version consistency
- Mock external API calls when needed