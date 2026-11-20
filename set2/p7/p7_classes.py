
# Name: Andrea G. Dela Cruz
# Section: IV-BSIT-C
# Activity: P7 - Student Management System with Classes
# Date: November 20, 2026

class Student:
    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.__grade = 0
        self.grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Invalid grade. Grade must be between 0 and 100.")

    def update_info(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Grade:", self.grade)


class Subject:
    def __init__(self, subject_code, subject_name):
        self.subject_code = subject_code
        self.subject_name = subject_name

    def display_subject(self):
        print("\n===== SUBJECT INFORMATION =====")
        print("Subject Code:", self.subject_code)
        print("Subject Name:", self.subject_name)


class Section:
    def __init__(self, section_name):
        self.section_name = section_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("\n===== STUDENT LIST =====")
        print("Section:", self.section_name)

        for student in self.students:
            print("--------------------")
            student.display_info()


def main():
    print("Name: Andrea G. Dela Cruz")

    subject = Subject("IT101", "Python Programming")
    section = Section("IV-BSIT C")

    student1 = Student("2026-001", "Andrea Cruz", "BSIT", 90)
    student2 = Student("2026-002", "Jamie Santos", "BSIT", 85)
    student3 = Student("2026-003", "Alex Reyes", "BSIT", 88)

    section.add_student(student1)
    section.add_student(student2)
    section.add_student(student3)

    subject.display_subject()

    print("\n===== UPDATING STUDENT INFORMATION =====")
    student1.update_info("Andrea Dela Cruz", "BSIT")
    student1.grade = 150
    print("Student information updated successfully.")

    section.display_students()


if __name__ == "__main__":
    main()
