import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [22, 25, 23, 28, 30]

plt.plot(days, temperature, marker='o',label ="temprature flactuation")
plt.title("Temperature Over 5 Days")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.legend()
plt.show()