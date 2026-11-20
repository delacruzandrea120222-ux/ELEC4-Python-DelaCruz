
# Name: Andrea G. Dela Cruz
# Section: IV-BSIT-C
# Activity: P8 - Inheritance and Polymorphism
# Date: November 20, 2026

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello! I am", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course, year_level):
        super().__init__(name, age)
        self.course = course
        self.year_level = year_level

    def introduce(self):
        print("\n===== STUDENT INTRODUCTION =====")
        print("Hello! I am", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Year Level:", self.year_level)


class Teacher(Person):
    def __init__(self, name, age, subject, department):
        super().__init__(name, age)
        self.subject = subject
        self.department = department

    def introduce(self):
        print("\n===== TEACHER INTRODUCTION =====")
        print("Hello! I am", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)
        print("Department:", self.department)


def main():
    print("Name: Andrea G. Dela Cruz")
    print("\n===== INHERITANCE AND POLYMORPHISM =====")

    person = Person("Morgan Lee", 30)
    student = Student("Andrea Cruz", 18, "BSIT", 4)
    teacher = Teacher("Pat Ferrer", 35, "Python", "IT Department")

    people = [person, student, teacher]

    for individual in people:
        individual.introduce()


if __name__ == "__main__":
    main()
