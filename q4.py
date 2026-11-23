students = []

n = int(input("Enter the no. of enrolled students"))

for i in range(n):
    roll = int(input("enter the roll no. of the students:"))
    name = (input("enter the name:"))

    count = int(input("enter the number of courses"))
    courses = []

    for j in range(count):
        course = input("enter the name of course:")
        courses.append(course)

    student = (roll,name,courses)
    students.append(student)

python_students = set()
cpp_students = set()

for student in students:
    name = student[1]
    courses = student[2]
    for course in courses:
        if course.lower() == "python":
            python_students.add(name)
        else:
            cpp_students.add(name)

print("python:", python_students)
print("cpp:",cpp_students)


print("common:", python_students & cpp_students)
print("only python:", python_students-cpp_students)
print("only cpp:",cpp_students - python_students)



