def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def power(a, b):
    return a ** b


def greet(name):
    return f"Hello {name}"


def is_even(num):
    return num % 2 == 0


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 2))
    print(power(2, 3))
    print(greet("Soujanya"))
    print(is_even(10))
    print(factorial(5))
