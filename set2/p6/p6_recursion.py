
# Name: Andrea G. Dela Cruz
# Section: IV-BSIT-C
# Activity: P6 - Recursion Toolkit
# Date: November 20, 2026

# Calculates factorial using recursion.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Calculates a Fibonacci number using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Calculates the sum from 1 to n using recursion.
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Searches for a value in a list using recursion.
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


# Generates Fibonacci terms recursively.
def fibonacci_terms(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    previous = fibonacci_terms(n - 1)
    return previous + [previous[-1] + previous[-2]]


def main():
    print("Name: Andrea G. Dela Cruz")

    while True:
        print("\n===== RECURSION TOOLKIT =====")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum from 1 to n")
        print("4. Search list")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "5":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                n = int(input("Enter n (0 or greater): "))
                if n < 0:
                    print("Use a non-negative number.")
                else:
                    print("Factorial:", factorial(n))

            elif choice == "2":
                n = int(input("How many terms? "))
                if n < 0:
                    print("Use a non-negative number.")
                else:
                    if n == 0:
                        print("No term")
                    else:
                        print("Nth value (zero-based):", fibonacci(n - 1))
                    print("First terms:", fibonacci_terms(n))

            elif choice == "3":
                n = int(input("Enter n (0 or greater): "))
                if n < 0:
                    print("Use a non-negative number.")
                else:
                    print("Sum:", sum_numbers(n))

            elif choice == "4":
                raw = input("Enter list items separated by commas: ")
                items = [item.strip() for item in raw.split(",") if item.strip()]
                target = input("Value to search: ").strip()
                print("Found:", search(items, target))

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid whole number.")


if __name__ == "__main__":
    main()
