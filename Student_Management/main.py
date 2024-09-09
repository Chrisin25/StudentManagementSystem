from Student_Management.school_module import School

new_school=School()
new_school.add_student()
for student in new_school.students:
    student.add_grades()
for student in new_school.students:
    student.display_student_details()
#Raise an exception when attempting to remove or add a student with an invalid student_id.
#Handle cases where grades are invalid (e.g., non-numeric or outside the range 0-100)