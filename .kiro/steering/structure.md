# Project Structure & Organization

## Root Level Files
- **Numbered Notebooks (1-5)**: Progressive learning tutorials from basic concepts to advanced patterns
  - `1_get_start.ipynb`: Initial setup and basic concepts
  - `2_workflow_agent.ipynb`: Workflow and agent patterns
  - `3_router.ipynb`: Routing mechanisms
  - `4_Parallelization.ipynb`: Parallel execution patterns
  - `5_orchestrator_worker.ipynb`: Orchestrator-worker architecture
- **Configuration**: `.env`, `env.example`, `requirements.txt`
- **Documentation**: `CLAUDE.md`, `LICENSE`

## Directory Structure

### `/src/`
Core Python modules with standalone implementations:
- Reusable LangGraph examples and utilities
- Production-ready code patterns
- `__init__.py` for proper package structure

### `/examples/`
Educational resources and setup utilities:
- Interactive Jupyter notebooks for hands-on learning
- `jupyter_setup.py`: Async environment configuration helper
- `/python_core/`: Additional Python examples

### `/tests/`
Testing infrastructure:
- pytest-based test suite
- Basic functionality and integration tests
- `__init__.py` for test package structure

### `/docs/`
Documentation and guides:
- `ASYNCIO_JUPYTER.md`: Detailed async handling guide
- Technical documentation and best practices

## File Naming Conventions
- **Notebooks**: Numbered prefix for learning progression (1_, 2_, etc.)
- **Python modules**: Snake_case naming
- **Documentation**: UPPERCASE.md for main docs, lowercase.md for specific guides

## Code Organization Patterns
- **State Management**: Use TypedDict with Annotated message lists
- **Memory/Checkpointing**: Consistent thread-based conversation tracking
- **Agent Creation**: Both prebuilt and custom graph patterns
- **Error Handling**: Graceful API key and async error management

## Development Workflow
1. Start with numbered notebooks for learning concepts
2. Extract reusable patterns to `/src/` modules
3. Add tests in `/tests/` for new functionality
4. Document special considerations in `/docs/`