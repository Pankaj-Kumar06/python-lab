import matplotlib.pyplot as plt

subjects = [1, 2, 3, 4, 5]
student_A = [70, 80, 75, 90, 85]
student_B = [60, 65, 80, 75, 95]

plt.plot(subjects, student_A, marker='o', label='Student A')
plt.plot(subjects, student_B, marker='s', label='Student B')

plt.title("Student Comparison")
plt.xlabel("Subject Number")
plt.ylabel("Marks")

plt.legend()
plt.grid(True)

plt.show()