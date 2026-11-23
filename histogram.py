import matplotlib.pyplot as plt

marks = [35, 40, 45, 48, 50, 52, 55, 56, 60, 62,
         65, 68, 70, 72, 75, 78, 80, 85, 90, 95]

plt.hist(marks, bins=5, color='orange', edgecolor='black',label='marks analysis')

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.legend()
plt.grid(False)
print("count per bins",)
plt.show()