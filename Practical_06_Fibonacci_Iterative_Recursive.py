"""Fibonacci Sequence Analyzer

This beginner-friendly program demonstrates both iterative and recursive
solutions for generating Fibonacci sequences, with input validation and a
simple comparison menu.
"""


def validate_positive_integer(value):
    """Return a positive integer from user input or reject invalid values."""
    if isinstance(value, bool):
        return False

    if isinstance(value, int):
        return value > 0

    if isinstance(value, str):
        stripped = value.strip()
        if stripped == "":
            return False
        try:
            number = int(stripped)
        except ValueError:
            return False
        return number > 0

    return False


def fibonacci_iterative(n):
    """Return the nth Fibonacci value using an iterative loop.

    This follows the practical's convention where n is the number of terms
    and the sequence starts as: [0, 1, 1, 2, 3, ...].
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be a positive integer.")
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    if n == 1:
        return 0

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def fibonacci_iterative_list(n):
    """Return the first n Fibonacci terms using an iterative loop."""
    if not validate_positive_integer(n):
        raise ValueError("n must be a positive integer.")

    if n == 1:
        return [0]

    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci


def fibonacci_recursive(n):
    """Return the nth Fibonacci value using recursion.

    This version follows the same practical convention as the iterative
    function and prints the same sequence values for small n.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be a positive integer.")
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_recursive_list(n):
    """Return the first n Fibonacci terms using recursion."""
    if not validate_positive_integer(n):
        raise ValueError("n must be a positive integer.")

    if n == 1:
        return [0]

    result = []
    for i in range(1, n + 1):
        result.append(fibonacci_recursive(i))
    return result


def display_indexed_table(sequence):
    """Display the Fibonacci values as a simple indexed engineering table."""
    print("\nIndexed Fibonacci table")
    print("Record | Fibonacci tag")
    print("------ | ------------")
    for index, value in enumerate(sequence, start=1):
        print(f"{index:<6} | {value}")


def compare_methods(n):
    """Compare iterative and recursive results for the same n."""
    iterative_list = fibonacci_iterative_list(n)
    recursive_list = fibonacci_recursive_list(n)

    print(f"\nFibonacci sequence for n = {n}:")
    print(iterative_list)

    print("\nIterative and recursive results:")
    print(f"  Iterative: {iterative_list}")
    print(f"  Recursive: {recursive_list}")

    if iterative_list == recursive_list:
        print("\nBoth methods produce the same Fibonacci values.")
    else:
        print("\nThe two methods differ. Please check the logic.")

    display_indexed_table(iterative_list)


def measure_execution_time(func, n):
    """Measure elapsed time for a function call."""
    import time

    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start


def get_valid_number(prompt):
    """Read a positive integer from the user with validation."""
    while True:
        user_input = input(prompt)
        if validate_positive_integer(user_input):
            return int(user_input)
        print("Invalid input. Please enter a positive integer.")


def main():
    """Run the Fibonacci Sequence Analyzer menu."""
    print("FIBONACCI SEQUENCE ANALYZER")
    print("1. Generate using iteration")
    print("2. Generate using recursion")
    print("3. Compare both methods")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "4":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3"}:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
            continue

        n = get_valid_number("Enter the number of Fibonacci terms: ")

        if choice == "1":
            values = fibonacci_iterative_list(n)
            print(f"\nIterative sequence for n = {n}: {values}")
            display_indexed_table(values)

        elif choice == "2":
            values = fibonacci_recursive_list(n)
            print(f"\nRecursive sequence for n = {n}: {values}")
            display_indexed_table(values)

        else:
            compare_methods(n)

            iterative_result, iterative_time = measure_execution_time(fibonacci_iterative, n)
            recursive_result, recursive_time = measure_execution_time(fibonacci_recursive, n)
            print(f"\nExecution time for n={n}:")
            print(f"  Iterative: {iterative_time:.6f} seconds, result={iterative_result}")
            print(f"  Recursive: {recursive_time:.6f} seconds, result={recursive_result}")


if __name__ == "__main__":
    main()
