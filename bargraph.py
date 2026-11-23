import matplotlib.pyplot as plt

subjects = ["Math", "Python", "DSA", "Physics"]
marks = [80, 90, 75, 65]
marks2 =[70,60,50,55]
hi = max(marks)
low = min(marks)
colors = []
for i in marks:
    if i==hi:
        colors.append('green')
    elif i==low:
        colors.append('red')
    else:
        colors.append('blue')
plt.figure(figsize=(9,6))
plt.bar(subjects,marks,color = colors,edgecolor = 'orange',width = 0.35,label = "mark scored")
plt.grid(True)
plt.title("Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()

plt.show()