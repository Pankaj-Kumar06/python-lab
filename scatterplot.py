import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
colors = [10, 20, 30, 40, 50]
sizes = [50, 100, 150, 200, 250]

plt.figure(figsize=(8, 5))

plt.scatter(x, y, c=colors, s=sizes, cmap="viridis")

plt.colorbar()
plt.title("Colored Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()