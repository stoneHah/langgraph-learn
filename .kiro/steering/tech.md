# Tech Stack & Build System

## Core Dependencies
- **LangGraph**: Primary framework for building AI workflows and agents
- **LangChain**: With Anthropic integration for LLM interactions
- **Python 3.x**: Core runtime environment

## Development Environment
- **Virtual Environment**: Uses `.venv` for dependency isolation
- **Package Management**: Standard pip with `requirements.txt`
- **Jupyter Notebooks**: Primary development interface for tutorials

## LLM Provider Support
- **OpenAI**: ChatOpenAI models with custom base URL support
- **Anthropic**: Claude models via ChatAnthropic
- **DashScope**: Qwen models integration
- **Custom Endpoints**: Configurable base URLs for alternative APIs

## Environment Configuration
Required environment variables (copy from `env.example` to `.env`):
```bash
# Core API Keys
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
DASHSCOPE_API_KEY=your_key_here

# LangSmith Tracing
LANGCHAIN_API_KEY=your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=langgraph-learn

# Development
DEBUG=true
LOG_LEVEL=INFO
```

## Common Commands
```bash
# Setup environment
pip install -r requirements.txt

# Run tests
pytest tests/

# Run standalone examples
python src/example_langgraph.py

# Start Jupyter for notebooks
jupyter notebook

# Install optional Jupyter async support
pip install nest-asyncio aiohttp
```

## Async Considerations
- **Jupyter Environment**: Special handling for asyncio in notebooks
- **Use `await` directly**: Preferred over `asyncio.run()` in Jupyter
- **Setup Helper**: `examples/jupyter_setup.py` for async configuration
- **nest-asyncio**: Optional dependency for nested event loop support