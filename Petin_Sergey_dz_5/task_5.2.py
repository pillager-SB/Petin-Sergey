def non_yield(n):
    print(*[num for num in range(1, n + 1, 2)])  # List Comprehension
    print(*(num for num in range(1, n + 1, 2)))  # Generator Comprehensions


non_yield(15)
