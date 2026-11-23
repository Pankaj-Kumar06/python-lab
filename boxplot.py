import matplotlib.pyplot as plt
maths = [78, 85, 67, 90, 73, 81, 69, 94, 76, 88]
physics = [72, 88, 70, 92, 75, 79, 68, 90, 74, 85]
chem = [75, 82, 65, 88, 78, 83, 72, 92, 79, 86]
english = [80, 84, 72, 91, 76, 80, 70, 95, 77, 89]
plt.figure(figsize=(7, 4.5))
plt.boxplot([maths, physics, chem, english])
plt.xticks([1, 2, 3, 4], '''["Maths", "Physics", "Chemistry", "English"]''')
plt.title("Subject-wise Marks Distribution")
plt.ylabel("Marks")
plt.grid(axis="y")
plt.show()