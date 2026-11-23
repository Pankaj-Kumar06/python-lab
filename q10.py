import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [45000, 52000, 48000, 61000, 58000, 65000, 62000, 70000, 68000, 75000, 72000, 80000]
plt.figure(figsize=(9, 4.5))
plt.plot(months, sales, marker="o", color="green", linestyle="-", linewidth=2, label="Sales")
hi = sales.index(max(sales)) # index of highest sales
lo = sales.index(min(sales))
plt.annotate("Highest", xy=(months[hi], sales[hi]), xytext=(months[hi - 2], sales[hi]),
arrowprops=dict(arrowstyle="->"))
plt.annotate("Lowest", xy=(months[lo], sales[lo]), xytext=(months[lo + 1], sales[lo] - 2500),
arrowprops=dict(arrowstyle="->"))
plt.ylim(40000, 85000) # leave room so the labels stay inside the plot
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Sales (Rs)")
plt.grid(True)
plt.legend()
plt.show()
print("Highest:", months[hi], max(sales), "| Lowest:", months[lo], min(sales))