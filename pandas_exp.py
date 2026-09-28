import pandas as pd

# ==========================================================
# 1. Student DataFrame
# ==========================================================
students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
    "Python": [80, 90, 70, 85, 60],
    "DBMS": [75, 88, 65, 90, 70],
    "Mathematics": [85, 92, 72, 88, 65]
}

df = pd.DataFrame(students)
df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print(df)
print("\nStudents with Average > 75")
print(df[df["Average"] > 75])

# ==========================================================
# 2. Employee DataFrame
# ==========================================================
employees = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Raj", "Anita", "Vikas", "Pooja", "Rohit"],
    "Department": ["IT", "HR", "Sales", "IT", "Finance"],
    "Salary": [55000, 45000, 60000, 70000, 50000],
    "Experience": [5, 3, 7, 10, 4]
}

df = pd.DataFrame(employees)

print("\nEmployees with Salary > 50000")
print(df[df["Salary"] > 50000])

print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())

print("\nEmployee with Highest Experience")
print(df.loc[df["Experience"].idxmax()])

# ==========================================================
# 3. Product Sales DataFrame
# ==========================================================
products = {
    "Product_ID": [101, 102, 103, 104],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Category": ["Electronics"] * 4,
    "Price": [50000, 500, 1500, 10000],
    "Quantity": [2, 20, 10, 5]
}

df = pd.DataFrame(products)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("\nProduct with Highest Sales")
print(df.loc[df["Total_Amount"].idxmax()])

# ==========================================================
# 4. Patient DataFrame
# ==========================================================
patients = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["A", "B", "C", "D", "E"],
    "Age": [65, 45, 70, 55, 80],
    "Disease": ["Diabetes", "Fever", "Cancer", "Heart", "Asthma"],
    "Medical_Charges": [60000, 15000, 90000, 45000, 70000]
}

df = pd.DataFrame(patients)

print("\nPatients Above 60 Years")
print(df[df["Age"] > 60])

print("Average Medical Charge:", df["Medical_Charges"].mean())
print("Maximum Medical Charge:", df["Medical_Charges"].max())

print("\nMedical Charges > 50000")
print(df[df["Medical_Charges"] > 50000])

# ==========================================================
# 5. Orders DataFrame
# ==========================================================
orders = {
    "Order_ID": [1, 2, 3, 4],
    "Customer": ["Amit", "Neha", "Rahul", "Priya"],
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Quantity": [1, 2, 1, 3],
    "Price": [50000, 20000, 30000, 10000],
    "Discount": [2000, 1000, 1500, 500]
}

df = pd.DataFrame(orders)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("\nAll Orders")
print(df)

print("\nOrders Above 5000")
print(df[df["Final_Amount"] > 5000])

print("\nHighest Value Order")
print(df.loc[df["Final_Amount"].idxmax()])

print("Average Order Value:", df["Final_Amount"].mean())

# ==========================================================
# 6. Attendance DataFrame
# ==========================================================
attendance = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["A", "B", "C", "D", "E"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [90, 60, 80, 70, 95]
}

df = pd.DataFrame(attendance)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("\nAttendance Below 75%")
print(df[df["Attendance_Percentage"] < 75])

# ==========================================================
# 7. Retail Shop Sales
# ==========================================================
sales = {
    "Product_ID": [1, 2, 3, 4],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Category": ["Electronics"] * 4,
    "Price": [50000, 500, 1500, 10000],
    "Quantity": [2, 25, 15, 5]
}

df = pd.DataFrame(sales)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("\nProducts with Sales > 10000")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with Maximum Sales")
print(df.loc[df["Total_Sales"].idxmax()])

print("Average Sales:", df["Total_Sales"].mean())

# ==========================================================
# 8. Student Marks Series
# ==========================================================
marks = pd.Series({
    "Amit": 85,
    "Neha": 92,
    "Rahul": 70,
    "Priya": 88,
    "Karan": 60
})

print("\nStudent Marks Series")
print(marks)

print("Marks of Amit:", marks["Amit"])
print("Maximum:", marks.max())
print("Minimum:", marks.min())
print("Average:", marks.mean())
print("Above 75")
print(marks[marks > 75])

# ==========================================================
# 9. Product Price Series
# ==========================================================
prices = pd.Series({
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 10000
})

print("\nProduct Prices")
print(prices)

print("\nPrice Increased by 10%")
print(prices * 1.10)

print("Most Expensive Product:", prices.idxmax())
print(prices[prices > 1000])

# ==========================================================
# 10. Patient Age Series
# ==========================================================
ages = pd.Series({
    "P101": 65,
    "P102": 45,
    "P103": 70,
    "P104": 35,
    "P105": 80
})

print("\nAverage Age:", ages.mean())
print("Oldest Patient:", ages.idxmax(), ages.max())
print("Youngest Patient:", ages.idxmin(), ages.min())
print(ages[ages > 60])

# ==========================================================
# 11. Attendance Series
# ==========================================================
attendance_series = pd.Series({
    "Amit": 95,
    "Neha": 70,
    "Rahul": 85,
    "Priya": 92,
    "Karan": 65
})

print("\nAverage Attendance:", attendance_series.mean())
print("Below 75%")
print(attendance_series[attendance_series < 75])

print("Above 90%")
print(attendance_series[attendance_series > 90])

print("Highest Attendance:", attendance_series.max())

# ==========================================================
# 12. students.csv
# ==========================================================
students_df = pd.read_csv("students.csv")

print(students_df.head())
print(students_df.tail())

students_df["Total"] = (
    students_df["Python"] +
    students_df["DBMS"] +
    students_df["Maths"]
)

students_df["Average"] = students_df["Total"] / 3

print(students_df[students_df["Average"] > 75])

print("\nHighest Average Student")
print(students_df.loc[students_df["Average"].idxmax()])

print("\nSubject Wise Average")
print(students_df[["Python", "DBMS", "Maths"]].mean())

# ==========================================================
# 13. employees.csv
# ==========================================================
emp_df = pd.read_csv("employees.csv")

print(emp_df[emp_df["Department"] == "CSE"])

print("Average Salary:", emp_df["Salary"].mean())
print("Highest Salary:", emp_df["Salary"].max())
print("Lowest Salary:", emp_df["Salary"].min())

print(emp_df[emp_df["Salary"] > 50000])

print("\nDepartment Wise Average Salary")
print(emp_df.groupby("Department")["Salary"].mean())

# ==========================================================
# 14. patients.csv
# ==========================================================
patient_df = pd.read_csv("patients.csv")

print(patient_df[patient_df["Age"] > 60])

print("Average Expense:",
      patient_df["Medical_Expense"].mean())

print("\nHighest Expense Patient")
print(patient_df.loc[
    patient_df["Medical_Expense"].idxmax()
])

print("\nDisease Count")
print(patient_df["Disease"].value_counts())

print(patient_df[
    patient_df["Medical_Expense"] > 50000
])

# ==========================================================
# 15. weather.csv
# ==========================================================
weather_df = pd.read_csv("weather.csv")

print("Maximum Temperature:",
      weather_df["Temperature"].max())

print("Minimum Temperature:",
      weather_df["Temperature"].min())

print("Average Temperature:",
      weather_df["Temperature"].mean())

print(weather_df[
    weather_df["Temperature"] > 35
])

print("\nCity Wise Average Temperature")
print(weather_df.groupby("City")["Temperature"].mean())