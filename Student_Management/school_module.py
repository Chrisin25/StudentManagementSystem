class Student:
    id=100
    def __init__(self):
        Student.id+=1
        self.student_id = Student.id
        self.name = input("student name: ")
        self.grades = []
        self.average_grade = 0

    def add_grades(self):
            try:
                for i in range(5):
                    grade=int(input("enter grade:"))
                    if grade<0 or grade>100:
                        raise ValueError
                    else:
                        self.grades.append(grade)
            except ValueError:
               print("Invalid grade.enter a grade between 0 and 100")


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
        new_student.add_grades()
        self.students.append(new_student)

    def remove_student(self, student_id):
        try:
            student_found = False
            for student in self.students:
                if student.student_id == student_id:
                    self.students.remove(student)
                    print("student removed")
                    student_found = True
            if not student_found:
                raise Exception
        except Exception:
            print("Invalid student id")

    def search_student(self, student_id):
        student_found = False
        for student in self.students:
            if student.student_id==student_id:
                print(student.display_student_details())
                student_found = True
        if not student_found:
            print("student not found")

    def generate_student(self):
        for student in self.students:
            yield student


class AdvancedSchool(School):
    def __init__(self):
        super().__init__()
        self.advanced_students=[]
    def find_advanced_students(self, threshold, students):
        for student in students:
            if student.average_grade > threshold:
                self.advanced_students.append(student)
        return self.advanced_students
