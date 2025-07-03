# 快速开始指南

## 1. 安装依赖

首先确保您已经安装了 [uv](https://github.com/astral-sh/uv)。

```bash
# 同步所有依赖
uv sync --all-extras
```

## 2. 设置环境变量

复制环境变量模板并填入您的API密钥：

```bash
# Windows
copy env.example .env

# Linux/macOS
cp env.example .env
```

然后编辑 `.env` 文件，填入您的API密钥。

## 3. 运行示例

```bash
# 运行LangGraph示例
uv run python src/example_langgraph.py
```

## 4. 开发工作流

```bash
# 格式化代码
uv run black .

# 检查代码风格
uv run flake8

# 运行类型检查
uv run mypy .

# 运行测试
uv run pytest
```

## 5. 添加新包

```bash
# 添加生产依赖
uv add requests

# 添加开发依赖
uv add --dev ipython

# 查看已安装的包
uv tree
```

## 6. 项目结构说明

- `src/` - 源代码目录
- `tests/` - 测试文件目录
- `pyproject.toml` - 项目配置文件
- `.python-version` - Python版本指定
- `env.example` - 环境变量模板

Happy coding! 🚀 