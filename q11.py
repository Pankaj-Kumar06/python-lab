import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Python", "DSA", "Physics", "Economics"]
marks = [85, 72, 90, 68, 80]

# Create figure
plt.figure(figsize=(8, 5))

# Plot the graph
plt.plot(subjects, marks, marker='o', color='blue', linestyle='-')

# Add title and labels
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Add grid
plt.grid(True)

# Display graph
plt.show()