import matplotlib.pyplot as plt

expenses = [4000, 3000, 1500, 1000, 500]
categories = ["Food", "Rent", "Travel", "Books", "Other"]

plt.pie(expenses, labels=categories, autopct='%1.1f%%')

plt.title("Monthly Expenses")
plt.show()