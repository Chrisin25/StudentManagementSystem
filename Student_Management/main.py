from Student_Management.school_module import School, AdvancedSchool

new_school=School()
print("new school created")
stop=False
while not stop:
    choice = int(input("Enter your choice:1.add student 2.remove student 3.search student 4.display student."))
    if choice==1:
        new_school.add_student()
    elif choice==2:
        student_id = int(input("enter student id:"))
        new_school.remove_student(student_id)
    elif choice==3:
        student_id=int(input("enter student id:"))
        new_school.search_student(student_id)
    elif choice==4:
        for student in new_school.generate_student():
            student.display_student_details()
    else:
        print("invalid choice")
    response=input("do you want to continue: y or n")
    if response=="n":
        stop=True
for student in new_school.generate_student():
    student.display_student_details()

new_advanced_school=AdvancedSchool()
student_list=new_advanced_school.find_advanced_students(60,new_school.students)
if not student_list:
    print("No student present in advanced school")
else:
    print("Advanced school students:")
    for student in student_list:
        student.display_student_details()
