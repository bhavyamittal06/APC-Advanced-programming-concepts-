#barchart 


import matplotlib.pyplot as plt

students = ["Amit", "Riya", "Rahul", "Neha", "Priya"]
marks = [75, 85, 60, 90, 80]

plt.bar(students, marks, color="skyblue")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students' Marks")

plt.show()



import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 45, 55, 65, 75, 90]

plt.scatter(hours, marks, color="red")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()



import matplotlib.pyplot as plt

ages = [18, 19, 20, 18, 21, 20, 19, 22,
        18, 20, 21, 19, 22, 20, 18, 21]

plt.hist(ages, bins=5, color="skyblue", edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Students")
plt.show()


import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [28, 30, 29, 32, 31, 33, 30]

plt.plot(days, temperature, marker="o", color="blue")

plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Weekly Temperature")

plt.show()


import matplotlib.pyplot as plt

expenses = [3000, 2000, 1500, 1000, 500]
categories = ["Food", "Rent", "Travel", "Shopping", "Other"]

plt.pie(expenses, labels=categories, autopct="%1.1f%%",
        startangle=90)

plt.title("Monthly Expenses")
plt.show()



import matplotlib.pyplot as plt

marks = [35, 40, 45, 50, 55, 55, 60, 65,
         65, 70, 75, 75, 80, 85, 90, 90]

plt.hist(marks, bins=5, color="green", edgecolor="black")

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Students' Marks")

plt.show()
