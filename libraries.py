# Import Code Libraries
import numpy as np
import matplotlib.pyplot as plt

# Define and Set Array Values
days = np.array([1, 2, 3, 4, 5, 6, 7])
revenue = np.array([500, 600, 989, 700, 100, 600, 520])
costs = np.array([400, 250, 500, 700, 50, 200, 310])

# Print Array Contents
print("Days:", days)
print("Daily Revenue:", revenue)
print("Daily Costs:", costs)

# Calculate and Prints Profits
profit = revenue - costs
print("Daily Profits:", profit)
print("Average Daily Profit:", np.mean(profit))
print("Highest Daily Profit:", np.max(profit))
print("Lowest Daily Profit:", np.min(profit))

# Plot Daily Profit
plt.plot(days, profit)

# Label the Graph
plt.title("Daily Business Profit")
plt.xlabel("Day")
plt.ylabel("Profit")

# Display the Graph
plt.show()