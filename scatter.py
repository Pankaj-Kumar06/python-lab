import matplotlib.pyplot as plt

subjects = ["Math", "Python", "DSA", "Physics"]
marks = [80, 90, 75, 65]

plt.scatter(subjects, marks, color='green')

plt.title("Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()