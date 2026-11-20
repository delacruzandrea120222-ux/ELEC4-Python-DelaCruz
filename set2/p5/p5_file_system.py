
# Name: Andrea G. Dela Cruz
# Section: IV-BSIT-C
# Activity: P5 - Student Information File System
# Date: November 20, 2026

from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.txt")


def load_records():
    records = []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.rstrip("\n").split("|")

                if len(parts) == 4:
                    records.append({
                        "id": parts[0],
                        "name": parts[1],
                        "course": parts[2],
                        "average": parts[3]
                    })

    except FileNotFoundError:
        pass

    return records


def save_records(records):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for record in records:
            file.write(
                f"{record['id']}|{record['name']}|"
                f"{record['course']}|{record['average']}\n"
            )


def get_average():
    while True:
        try:
            value = float(input("General average (0-100): "))

            if 0 <= value <= 100:
                return value

            print("Average must be from 0 to 100.")

        except ValueError:
            print("Enter a valid number.")


def add_record(records):
    student_id = input("Student ID: ").strip()

    if any(record["id"] == student_id for record in records):
        print("That ID already exists.")
        return

    name = input("Full name: ").strip()
    course = input("Course/Section: ").strip()
    average = get_average()

    records.append({
        "id": student_id,
        "name": name,
        "course": course,
        "average": str(average)
    })

    save_records(records)
    print("Record saved.")


def display_records(records):
    print("\n===== STUDENT RECORDS =====")

    if not records:
        print("No records yet.")
        return

    for record in records:
        print(
            f"{record['id']} | {record['name']} | "
            f"{record['course']} | {record['average']}"
        )


def search_record(records):
    student_id = input("ID to search: ").strip()

    for record in records:
        if record["id"] == student_id:
            print("\nSTUDENT FOUND")
            print(f"ID: {record['id']}")
            print(f"Name: {record['name']}")
            print(f"Course/Section: {record['course']}")
            print(f"Average: {record['average']}")
            return

    print("Student ID not found.")


def update_record(records):
    student_id = input("ID to update: ").strip()

    for record in records:
        if record["id"] == student_id:
            record["name"] = input("New full name: ").strip()
            record["course"] = input("New course/section: ").strip()
            record["average"] = str(get_average())

            save_records(records)
            print("Record updated.")
            return

    print("Student ID not found.")


def main():
    print("Name: Andrea G. Dela Cruz")

    records = load_records()

    while True:
        print("\n===== STUDENT FILE SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search by ID")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            display_records(records)
        elif choice == "3":
            search_record(records)
        elif choice == "4":
            update_record(records)
        elif choice == "5":
            save_records(records)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
