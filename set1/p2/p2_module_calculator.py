
# Name: Andrea G. Dela Cruz
# Section: IV-BSIT-C
# Activity: P2 - Modules
# Date: November 20, 2026

import math

def calculate_square_root(number):
    return math.sqrt(number)

def calculate_factorial(number):
    return math.factorial(number)

def calculate_power(number, exponent):
    return math.pow(number, exponent)

def main():
    while True:
        print("\n===== MATH MODULE CALCULATOR =====")
        print("Name: Andrea G. Dela Cruz")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Power")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "4":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice.")
            continue

        try:
            number = int(input("Enter a non-negative whole number: "))

            if number < 0:
                print("Please enter a non-negative number.")
                continue

            if choice == "1":
                print("Square Root:", calculate_square_root(number))

            elif choice == "2":
                print("Factorial:", calculate_factorial(number))

            elif choice == "3":
                exponent = float(input("Enter the exponent: "))
                print("Power:", calculate_power(number, exponent))

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
