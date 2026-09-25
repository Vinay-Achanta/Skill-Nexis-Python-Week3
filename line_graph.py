import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
sales = [20, 35, 30, 45, 50]

plt.plot(days, sales, marker="o")

plt.title("Weekly Sales")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.grid(True)
plt.show()