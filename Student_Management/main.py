from Student_Management.school_module import School, AdvancedSchool

new_school=School()
print("new school created")
stop=False
while not stop:
    choice = int(input("Enter your choice:1.add student 2.remove student 3.search student 4.generate student."))
    if choice==1:
        new_school.add_student()
    elif choice==2:
        student_id = int(input("enter student id:"))
        new_school.remove_student(student_id)
    elif choice==3:
        student_id=int(input("enter student id:"))
        new_school.search_student(student_id)
    elif choice==4:
        new_school.generate_student()
    else:
        print("invalid choice")
    response=input("do you want to continue: y or n")
    if response=="n":
        stop=True
print("Student details")
for student in new_school.students:
    student.display_student_details()
print("Advanced school students:")
new_advanced_school=AdvancedSchool()
student_list=new_advanced_school.find_advanced_students(60,new_school.students)
for student in student_list:
    student.display_student_details()
