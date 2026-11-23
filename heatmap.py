import matplotlib.pyplot as plt

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

plt.figure(figsize=(6, 5))

plt.imshow(data,cmap="gray")

plt.title("Simple Heatmap")
plt.colorbar()

plt.show()