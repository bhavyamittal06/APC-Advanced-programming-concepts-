students = {
    "Aarav": 78,
    "Bhavya": 92,
    "Riya": 85,
    "Kunal": 92,
    "Sneha": 67,
}

highest = max(students.values())
average = sum(students.values()) / len(students)
toppers = [name for name, marks in students.items() if marks == highest]

print("Highest Marks :", highest)
print("Average Marks : %.2f" % average)
print("Topper(s)     :", ", ".join(toppers))

# Top 3 students
print("\nTop 3 Students:")
ranked = sorted(students.items(), key=lambda x: x[1], reverse=True)
for rank, (name, marks) in enumerate(ranked[:3], start=1):
    print(rank, name, marks)

#3 current working directory

import os

print("Current Working Directory:", os.getcwd())