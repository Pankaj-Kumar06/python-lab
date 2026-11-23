#for the normal storing and searching the student detail
def search_rollno(students):
    roll = int(input("enter the roll no. to search:"))
    found = False
    for student in students:
        if student["roll"] == roll:
            print(student)
            found = True
    if not found:
        print("No student with this roll no. are available")

def delete_rollno(students):
    roll = int(input("enter the roll no. to delete:"))
    found = False
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            found = True
    if not found:
            print("No student with this roll no. are available")
def insert_rollno(students):
        name = input("Enter the name of sutdent")
        roll = int(input("Enter the roll no. of student"))
        cgpa = float(input("Enter the cgpa of student"))

        student = {
            "name" : name,
            "roll" : roll,
            "cgpa" : cgpa
        }
        students.append(student)  
def display(students):
    for student in students:
        print(student)
def main():
    students = []
    n = int(input("enter the number of students :"))

    for i in range(n):
        name = input("Enter the name of sutdent")
        roll = int(input("Enter the roll no. of student"))
        cgpa = float(input("Enter the cgpa of student"))

        student = {
            "name" : name,
            "roll" : roll,
            "cgpa" : cgpa
        }
        students.append(student)

    while True:
        print("\n 1. insert_student")
        print("2.search student")
        print("3. delete student")
        print("4.display")
        print("5.extit")

        choice = int(input("enter the choice as per menu"))

        match choice:
            case 1:
                search_rollno(students)
            case 2:
                delete_rollno(students)
            case 3:
                insert_rollno(students)
            case 4:
                display(students)
            case 5:
                exit()
            case _:
                print("invalid choice")
if __name__ == "__main__":
    main()