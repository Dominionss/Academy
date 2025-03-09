import asyncio


async def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


async def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


async def square(n):
    return n * n


async def cube(n):
    return n * n * n


async def main():
    numbers = list(range(1, 11))

    fib_results = await asyncio.gather(*[fibonacci(n) for n in numbers])
    fact_results = await asyncio.gather(*[factorial(n) for n in numbers])
    square_results = await asyncio.gather(*[square(n) for n in numbers])
    cube_results = await asyncio.gather(*[cube(n) for n in numbers])

    print("Fibonacci:", fib_results)
    print("Factorial:", fact_results)
    print("Squares:", square_results)
    print("Cubes:", cube_results)


if __name__ == "__main__":
    import time
    start_time = time.time()
    asyncio.run(main())
    print(f"Asynchronous execution time: {time.time() - start_time:.4f} seconds")
