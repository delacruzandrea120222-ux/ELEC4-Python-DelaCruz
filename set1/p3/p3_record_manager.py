
# Name: Andrea G. Dela Cruz
# Section: IV-BSIT-C
# Activity: P3 - Student Record Manager
# Date: November 20, 2026

students = []
student_keys = set()

MENU_OPTIONS = ("Add Student", "Remove Student", "Search Student",
                "Display All Students", "Exit")


def add_student():
    name = input("Student name: ").strip()
    key = name.casefold()

    if not name:
        print("Name cannot be empty.")
    elif key in student_keys:
        print("That student is already recorded.")
    else:
        students.append(name)
        student_keys.add(key)
        print("Student added successfully.")


def remove_student():
    name = input("Name to remove: ").strip()

    for existing in students:
        if existing.casefold() == name.casefold():
            students.remove(existing)
            student_keys.remove(existing.casefold())
            print("Student removed successfully.")
            return

    print("Student not found.")


def search_student():
    query = input("Search name: ").strip().casefold()

    if not query:
        print("Please enter a name to search.")
        return

    matches = [name for name in students if query in name.casefold()]

    if matches:
        print("\nSEARCH RESULTS")
        for name in matches:
            print(name)
    else:
        print("No matching student found.")


def display_students():
    ordered = sorted(students, key=str.casefold)

    print("\n===== STUDENT RECORDS =====")
    print(f"Total students: {len(ordered)}")

    if not ordered:
        print("No student records available.")
    else:
        for number, name in enumerate(ordered, start=1):
            print(f"{number}. {name}")

    print("===========================")


def main():
    print("Name: Andrea G. Dela Cruz")

    while True:
        print("\n===== STUDENT RECORD MANAGER =====")

        for number, option in enumerate(MENU_OPTIONS, start=1):
            print(f"{number}. {option}")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()



