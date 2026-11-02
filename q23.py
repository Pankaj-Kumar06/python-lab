import xml.etree.ElementTree as ET

# Create root element
root = ET.Element("students")

# Take number of students
n = int(input("Enter number of students: "))

# Take student details from user
for i in range(n):
    print("\nEnter details of student", i + 1)

    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    department = input("Enter department: ")
    cgpa = input("Enter CGPA: ")

    student = ET.SubElement(root, "student")

    ET.SubElement(student, "roll").text = roll
    ET.SubElement(student, "name").text = name
    ET.SubElement(student, "department").text = department
    ET.SubElement(student, "cgpa").text = cgpa

# Generate XML file
tree = ET.ElementTree(root)
tree.write("students.xml", encoding="utf-8", xml_declaration=True)

print("\nXML file created successfully.")


# Modify student information
search_roll = input("\nEnter roll number to modify: ")

tree = ET.parse("students.xml")
root = tree.getroot()

found = False

for student in root.findall("student"):
    roll = student.find("roll").text

    if roll == search_roll:
        print("Student found.")

        new_name = input("Enter new name: ")
        new_department = input("Enter new department: ")
        new_cgpa = input("Enter new CGPA: ")

        student.find("name").text = new_name
        student.find("department").text = new_department
        student.find("cgpa").text = new_cgpa

        found = True
        break

if found:
    tree.write("students.xml", encoding="utf-8", xml_declaration=True)
    print("Student information modified successfully.")
else:
    print("Student not found.")


# Display final XML data
print("\nUpdated Student Information:")

for student in root.findall("student"):
    print("Roll:", student.find("roll").text)
    print("Name:", student.find("name").text)
    print("Department:", student.find("department").text)
    print("CGPA:", student.find("cgpa").text)