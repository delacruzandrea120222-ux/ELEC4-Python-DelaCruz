
# Name: Andrea G. Dela Cruz
# Section: IV-BSIT-C
# Activity: P4 - Safe Menu Program
# Date: November 20, 2026

def divide_numbers():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        result = first / second
    except ValueError:
        print("Invalid input: enter numbers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Result:", result)
    finally:
        print("Division operation finished.")


def open_text_file():
    filename = input("File name to open: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You do not have permission to read that file.")
    else:
        print("\nFILE CONTENTS")
        print(content)
    finally:
        print("File operation finished.")


def main():
    print("Name: Andrea G. Dela Cruz")

    while True:
        print("\n===== SAFE MENU =====")
        print("1. Divide numbers")
        print("2. Open a text file")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_text_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu selection. Try again.")


if __name__ == "__main__":
    main()


# The try block contains statements that may cause errors.
# The except blocks handle specific errors such as invalid numbers and division by zero.
# The else block runs when no exception occurs.
# The finally block always runs, whether an exception occurs or not.
