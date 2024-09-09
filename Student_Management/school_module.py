import uuid


class Student:
    def __init__(self):
        self.student_id = uuid.uuid4()
        self.name = input("student name: ")
        self.grades = []
        self.average_grade = 0

    def add_grades(self):
            for i in range(5):
                self.grades.append(input("enter grade:"))

    def calculate_average_grade(self):
        grade_sum = 0
        for grade in self.grades:
            grade_sum += grade
        self.average_grade = grade_sum / 5

    def display_student_details(self):
        print("Student details:")
        print("student id:", self.student_id)
        print("Student name:", self.name)
        print("grades:", self.grades)
        self.calculate_average_grade()
        print("average grade", self.average_grade)


class School:
    def __init__(self):
        self.students = []

    def add_student(self):
        new_student = Student()
        self.students.append(new_student)

    def remove_student(self, student_id):
        student_found = False
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("student removed")
                student_found = True
            if not student_found:
                print("student not found")

    def search_student(self, student_id):
        student_found = False
        for student in self.students:
            if student.student_id == student_id:
                print(student)
                student_found = True
            if not student_found:
                print("student not found")

    def generate_student(self):
        for student in self.students:
            yield student


class AdvancedSchool(School):
    def find_advanced_students(self, threshold, new_school):
        for student in new_school:
            if student.average_grade > threshold:
                print(student)
