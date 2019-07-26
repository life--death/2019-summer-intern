import time

async def function():
    n = 100
    while n:
        print("num",n)
        time.sleep(0.1)
        n -= 1
    return "Hello World"

async def await_coroutine():
    result = await function()
    print(result)

await_coroutine()