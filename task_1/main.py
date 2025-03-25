def caching_fibonacci() -> callable:
    cache = {}  

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

fib = caching_fibonacci()

# Example of using the function 
print(fib(10))  # 55
print(fib(15))  # 610
