with open("/Users/pankajkumar/python developement/stuents.txt","r") as file:
    data = file.readlines()
print(data)

for line in data:
    student = line.split()
    name = student[0]
    marks = [int(x) for x in student[1].split(",")]
    total = sum(marks)
    avarage = total/len(marks)
    print(name,total,avarage)