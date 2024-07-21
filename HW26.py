import os


def call_counter(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            with open(path, 'a') as f:
                f.write(f"Function '{func.__name__}' was called {wrapper.calls} times\n")
            return func(*args, **kwargs)

        wrapper.calls = 0
        return wrapper

    return decorator



@call_counter('/Users/annakuliavets/Documents/pythonQA2024/HW26.txt')
def add(a, b):
    return a + b



print(add(4, 6))
print(add(3, 5))