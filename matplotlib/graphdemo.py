import matplotlib.pyplot as plt
import numpy as np

# 1. LINE PLOT
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure()
plt.plot(x, y, color="red", marker="o")
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["Values"])
plt.show()

# 2. SCATTER PLOT
x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Chart")
plt.show()

# 3. VERTICAL BAR CHART
x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.legend(["Bar"])
plt.show()

# 4. HORIZONTAL BAR CHART
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.figure()
plt.barh(x, y)
plt.title("Horizontal Bar Chart")
plt.show()

# 5. PIE CHART
x = [1, 2, 3, 4]
explode = (0.1, 0, 0, 0)
plt.figure()
plt.pie(x, explode=explode, labels=["A", "B", "C", "D"])
plt.title("Pie Chart")
plt.show()

# 6. HISTOGRAM
x = [1, 2, 3, 4, 5, 6, 7, 4]
plt.figure()
plt.hist(x, bins=[1, 2, 3, 4, 5, 6, 7])
plt.title("Histogram")
plt.show()

# 7. 3D PLOT
fig = plt.figure()
ax = plt.axes(projection="3d")
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
ax.plot3D(x, y, z, "green")
plt.title("3D Plot")
plt.show()

# 8. SUBPLOTS
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")
plt.suptitle("MY SHOP")
plt.show()
