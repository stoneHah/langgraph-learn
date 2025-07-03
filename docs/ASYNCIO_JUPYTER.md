# Jupyter 中的 Asyncio 使用指南

## 问题描述

在Jupyter Notebook中运行异步代码时，经常会遇到以下错误：

```
RuntimeError: asyncio.run() cannot be called from a running event loop
```

## 问题原因

Jupyter Notebook 内部已经运行了一个事件循环，而 `asyncio.run()` 试图创建一个新的事件循环。在已经存在事件循环的环境中，不能再创建新的事件循环。

## 解决方案

### 方案1：直接使用 await（推荐）

在Jupyter中，可以直接使用 `await` 关键字，无需 `asyncio.run()`：

```python
# ❌ 错误的做法
asyncio.run(say_after(2, "hello world"))

# ✅ 正确的做法
await say_after(2, "hello world")
```

### 方案2：使用 nest-asyncio

如果必须使用 `asyncio.run()`，可以安装并使用 `nest-asyncio`：

```bash
# 安装 nest-asyncio
uv add --optional jupyter nest-asyncio
```

```python
# 在notebook开头运行
import nest_asyncio
nest_asyncio.apply()

# 现在可以使用 asyncio.run() 了
asyncio.run(say_after(2, "hello world"))
```

### 方案3：使用项目提供的设置模板

```python
# 在notebook开头运行
from examples.jupyter_setup import setup_jupyter_async

# 或者直接导入（会自动设置）
import examples.jupyter_setup
```

## 完整示例

### 1. 基本用法

```python
import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)
    return message

# 在Jupyter中直接使用await
result = await say_after(2, "Hello World!")
print(f"结果: {result}")
```

### 2. 并发执行

```python
import asyncio
import time

async def concurrent_tasks():
    start_time = time.time()
    
    # 创建多个任务
    tasks = [
        asyncio.create_task(say_after(1, "任务1")),
        asyncio.create_task(say_after(2, "任务2")),
        asyncio.create_task(say_after(1.5, "任务3"))
    ]
    
    # 等待所有任务完成
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"总耗时: {end_time - start_time:.2f}秒")
    return results

# 运行并发任务
results = await concurrent_tasks()
```

### 3. 错误处理

```python
async def safe_async_operation():
    try:
        # 设置超时
        result = await asyncio.wait_for(
            say_after(3, "长时间任务"), 
            timeout=2.0
        )
        return result
    except asyncio.TimeoutError:
        print("操作超时！")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

# 运行安全的异步操作
result = await safe_async_operation()
```

### 4. 异步HTTP请求

```python
import aiohttp
import asyncio

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error: {e}"

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# 使用示例
urls = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/2'
]

# 并发获取多个URL
results = await fetch_multiple_urls(urls)
```

## 常见错误和解决方法

### 1. 忘记使用 await

```python
# ❌ 错误
task = say_after(2, "hello")  # 这只是创建了协程对象

# ✅ 正确
result = await say_after(2, "hello")
```

### 2. 在同步函数中调用异步函数

```python
# ❌ 错误
def sync_function():
    return say_after(2, "hello")  # 不能在同步函数中直接调用异步函数

# ✅ 正确
async def async_function():
    return await say_after(2, "hello")
```

### 3. 混用 asyncio.run() 和 await

```python
# ❌ 错误（在Jupyter中）
asyncio.run(say_after(2, "hello"))

# ✅ 正确
await say_after(2, "hello")
```

## 最佳实践

1. **在Jupyter中优先使用 `await`**：这是最简单和推荐的方法
2. **使用 `asyncio.create_task()` 创建并发任务**：可以同时执行多个异步操作
3. **合理使用 `asyncio.gather()`**：等待多个任务完成
4. **添加错误处理**：使用 try-except 和 `asyncio.wait_for()` 处理超时
5. **如果需要 `asyncio.run()`**：使用 `nest-asyncio` 库

## 环境设置

为了更好地在Jupyter中使用异步代码，建议在项目中安装以下依赖：

```bash
# 安装Jupyter相关依赖（包含nest-asyncio和aiohttp）
uv sync --extra jupyter
```

这将安装：
- `nest-asyncio`: 支持嵌套事件循环
- `aiohttp`: 异步HTTP客户端
- `jupyter`: Jupyter Notebook环境
- `ipykernel`: IPython内核

## 参考资源

- [Asyncio 官方文档](https://docs.python.org/3/library/asyncio.html)
- [nest-asyncio 项目](https://github.com/erdewit/nest_asyncio)
- [aiohttp 文档](https://docs.aiohttp.org/) 