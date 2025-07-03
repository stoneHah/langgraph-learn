"""
Jupyter 异步环境设置模板

在Jupyter notebook开头运行此代码，可以解决asyncio相关问题
"""

def setup_jupyter_async():
    """设置Jupyter异步环境"""
    
    # 1. 启用嵌套事件循环支持
    try:
        import nest_asyncio
        nest_asyncio.apply()
        print("✅ nest_asyncio 已启用 - 现在可以在Jupyter中使用 asyncio.run()")
    except ImportError:
        print("❌ 需要安装 nest_asyncio: uv add --optional jupyter nest-asyncio")
        
    # 2. 设置更好的异步显示
    try:
        import asyncio
        import warnings
        
        # 抑制一些asyncio警告
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        
        print("✅ Asyncio 环境配置完成")
        
        # 显示当前事件循环状态
        try:
            loop = asyncio.get_running_loop()
            print(f"✅ 当前运行的事件循环: {type(loop).__name__}")
        except RuntimeError:
            print("ℹ️  没有运行中的事件循环")
            
    except Exception as e:
        print(f"❌ Asyncio 设置出错: {e}")
    
    # 3. 导入常用的异步库
    try:
        import aiohttp
        print("✅ aiohttp 可用")
    except ImportError:
        print("ℹ️  aiohttp 未安装 - 如需HTTP请求功能，请运行: uv add --optional jupyter aiohttp")
    
    print("\n" + "="*50)
    print("📝 使用提示:")
    print("1. 在Jupyter中直接使用 await，无需 asyncio.run()")
    print("2. 使用 asyncio.create_task() 创建并发任务")
    print("3. 使用 asyncio.gather() 等待多个任务")
    print("4. 如果遇到问题，可以使用 asyncio.run() (已启用嵌套支持)")
    print("="*50)


# 快速测试函数
async def test_async_environment():
    """测试异步环境是否正常工作"""
    import asyncio
    import time
    
    print("🧪 测试异步环境...")
    
    start_time = time.time()
    
    # 创建几个测试任务
    tasks = [
        asyncio.create_task(asyncio.sleep(0.5)),
        asyncio.create_task(asyncio.sleep(0.3)),
        asyncio.create_task(asyncio.sleep(0.1))
    ]
    
    await asyncio.gather(*tasks)
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    print(f"✅ 异步环境测试完成！耗时: {elapsed:.2f}秒")
    print("💡 如果看到这条消息，说明异步环境配置成功！")


if __name__ == "__main__":
    # 在Python脚本中运行
    setup_jupyter_async()
    
    # 测试环境
    import asyncio
    asyncio.run(test_async_environment())
else:
    # 在Jupyter中导入时自动设置
    print("🚀 正在设置Jupyter异步环境...")
    setup_jupyter_async() 