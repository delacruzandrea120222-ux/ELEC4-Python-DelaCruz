
# Name: Andrea G. Dela Cruz
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator
# Date: November 20, 2026

def enter_grades():
    grades = []

    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))
            if number_of_grades > 0:
                break
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1} (0-100): "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)


def determine_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def display_results(grades):
    if not grades:
        print("No grades available. Please enter grades first.")
        return

    print("\n===== STUDENT GRADE RESULTS =====")
    print(f"Grades: {grades}")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest_grade(grades)}")
    print(f"Lowest Grade: {get_lowest_grade(grades)}")
    print(f"Status: {determine_status(grades)}")
    print("=================================")


def main():
    student_grades = []

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("Name: Andrea G. Dela Cruz")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_grades = enter_grades()
            print("Grades successfully entered!")

        elif choice == "2":
            display_results(student_grades)

        elif choice == "3":
            print("Thank you for using the Student Grade Calculator!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()



