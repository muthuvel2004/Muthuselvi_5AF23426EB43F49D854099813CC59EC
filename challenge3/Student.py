class Student:
    def __init__(self, name, roll_no, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students = [
    Student("joysha", "004", 8.5),
    Student("sofi", "002", 9.5),
    Student("janani", "003", 9.0),
    Student("kavitha", "001", 10.0),
    Student("seetha", "005", 9.9)
]

sorted_students = sort_students(students)
print("\nstudents in descending order of CGPA\n")
for student in sorted_students:
    print("Name: {:<10} Roll No: {:<5} CGPA: {:.1f}".format(student.name, student.roll_no, student.cgpa))
