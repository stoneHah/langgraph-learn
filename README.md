# LangGraph Learn

一个用于学习LangGraph的Python项目。

## 项目设置

本项目使用 [uv](https://github.com/astral-sh/uv) 作为包管理器和依赖解析器。

### 安装依赖

```bash
# 安装基础依赖
uv sync

# 安装开发依赖
uv sync --extra dev

# 安装Jupyter依赖（包含 nest-asyncio 和 aiohttp）
uv sync --extra jupyter

# 安装所有依赖
uv sync --all-extras
```

### 运行项目

```bash
# 激活虚拟环境并运行Python脚本
uv run python your_script.py

# 或者先激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows

# 然后直接运行
python your_script.py
```

### 添加新依赖

```bash
# 添加生产依赖
uv add package_name

# 添加开发依赖
uv add --dev package_name

# 添加可选依赖组
uv add --optional jupyter package_name
```

### 开发工具

```bash
# 代码格式化
uv run black .

# 代码检查
uv run flake8

# 类型检查
uv run mypy .

# 运行测试
uv run pytest
```

## Jupyter 异步编程

### 常见问题

如果在Jupyter中遇到 `RuntimeError: asyncio.run() cannot be called from a running event loop` 错误，请参考以下解决方案：

#### 快速解决方法

```python
# ❌ 错误的做法
asyncio.run(my_async_function())

# ✅ 正确的做法
await my_async_function()
```

#### 使用项目提供的设置

```python
# 在Jupyter notebook开头运行
from examples.jupyter_setup import setup_jupyter_async
# 或直接导入
import examples.jupyter_setup
```

#### 详细文档

查看 [Jupyter 中的 Asyncio 使用指南](docs/ASYNCIO_JUPYTER.md) 获取完整的解决方案和最佳实践。

## 项目结构

```
langgraph-learn/
├── src/                    # 源代码目录
├── tests/                  # 测试目录
├── examples/               # 示例代码
│   ├── jupyter_setup.py   # Jupyter异步设置
│   └── python_core/        # Python核心概念示例
├── docs/                   # 文档目录
│   └── ASYNCIO_JUPYTER.md  # Asyncio使用指南
├── pyproject.toml         # 项目配置和依赖
├── .python-version        # Python版本
├── .gitignore            # Git忽略文件
└── README.md             # 项目说明
```

## 环境变量

创建一个 `.env` 文件来存储环境变量：

```env
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_TRACING_V2=true
```

## 许可证

MIT License 