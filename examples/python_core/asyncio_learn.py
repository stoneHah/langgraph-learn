import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

task = asyncio.create_task(say_after(2,"hello world"))
print(task)

asyncio.run(task)
# asyncio.run(say_after(2,"hello world"))
