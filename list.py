#1 example
fruits = ["Apple" , " orange" , " banana" , " grapes"]
print(fruits[1])
print(fruits[2])

# 2nd 
numbers = [10, 20 , 20 , 40 , 50]
print(numbers[1])
print(numbers[4])
print(numbers[3])

#3rd  
colors = [ "purple" ,"pink " , " blue"]
colors[1] = "brown"
print(colors[1])

#4th 
numbers = [10, 20, 30, 40]

numbers.append(50)     # add at end
numbers.insert(0, 5)   # add at index 0
numbers.insert(2, 15)  # add at index 2
print(numbers)


#5th 
students = [ "bhavya", " riya " ,"siya" , "diya"]
students.pop (0)
students.pop (2)

print(students)

#6th 
numbers = [10, 20 , 30 , 15]
largest = numbers[0]
smallest = numbers[0]

for num in numbers: 
 if num > largest :
   largest = num
if num < smallest: 
  smallest = num

print("largest =",largest )
print("smallest = " ,smallest)

#7th 
numbers = [10,20,30,40]

total = sum(numbers)

average = total / len(numbers)

print(total)
print(average)


#8th

numbers = [1,2,3,4,5,6]

even = 0
odd = 0

for num in numbers:

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)

#9th
cities = ["Delhi","Mumbai","Pune","Kolhapur"]

city = input("Enter city name: ")

if city in cities:
    print("Found")
else:
    print("Not Found")


#10th

numbers = [1,2,3,4,5]

print(numbers[::-1])


#11th

numbers = [ 10, 20 , 30 , 40 , 50]
print(numbers[:5])
print(numbers[-5:])
print(numbers[::2])

#12th

lst = [10, 20, 30, 40, 50, 60]

for i in range(0, len(lst), 2):
    print(lst[i])

#13th
nums = [45, 12, 78, 23, 1, 90, 34, 56, 11, 67]

nums.sort()
print(nums)

#14th
lst = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(lst))
print(unique)

#15th
lst = [10, 40, 20, 50, 30]

lst.sort()
print("Second largest:", lst[-2])

#16th

student = [
    ["Bhavya"],
    [101],
    [85]
]

print("Name:", student[0][0])
print("Roll No:", student[1][0])
print("Marks:", student[2][0])


#17th
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

C = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print(C)

#18th

cart = []

cart.append("Milk")
cart.append("Bread")

print(cart)

cart.remove("Milk")

print(cart)

print("Total items:", len(cart))

#19th

students = ["Aman", "Riya", "Bhavya"]

print("Total Students:", len(students))

name = input("Search student: ")

if name in students:
    print("Present")
else:
    print("Not Present")


#20th

books = ["Python", "Java", "C++"]

books.append("SQL")

print(books)

books.remove("Java")

print(books)

print("Total books:", len(books))

#21th

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2

print(merged)

#22nd 

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

for item in list1:
    if item in list2:
        print(item)

#23rd

lst = [1, 2, 2, 3, 3, 3]

for item in set(lst):
    print(item, ":", lst.count(item))

#24th

lst = [1, 2, 3, 4, 5]

lst = lst[1:] + lst[:1]

print(lst)


#25th

lst = [1, 2, 2, 3, 1, 4, 5]

result = []

for item in lst:
    if item not in result:
        result.append(item)

print(result)

#26th

marks = []

for i in range(20):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above_avg = 0
below_avg = 0

for mark in marks:
    if mark > average:
        above_avg += 1
    elif mark < average:
        below_avg += 1

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above_avg)
print("Students Below Average:", below_avg)


#27ths
salaries = []

n = int(input("Enter number of employees: "))

for i in range(n):
    salary = int(input(f"Enter salary of employee {i+1}: "))
    salaries.append(salary)

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1
    if salary < 30000:
        below_30000 += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees earning above ₹50,000:", above_50000)
print("Employees earning below ₹30,000:", below_30000)

#28th

scores = []

for i in range(10):
    score = int(input(f"Enter score in match {i+1}: "))
    scores.append(score)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", centuries)
print("Half-Centuries:", half_centuries)


#29th

temps = []

for i in range(30):
    temp = float(input(f"Enter temperature of day {i+1}: "))
    temps.append(temp)

hottest = max(temps)
coldest = min(temps)
average = sum(temps) / len(temps)

above_avg = 0
below_avg = 0

for temp in temps:
    if temp > average:
        above_avg += 1
    elif temp < average:
        below_avg += 1

print("Hottest Day Temperature:", hottest)
print("Coldest Day Temperature:", coldest)
print("Average Temperature:", average)
print("Days Above Average:", above_avg)
print("Days Below Average:", below_avg)



#30th

patients = []

while True:
    print("\n1. Add Patient")
    print("2. Delete Patient")
    print("3. Search Patient")
    print("4. Display Patients")
    print("5. Count Patients")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        patients.append([name, age])

    elif choice == 2:
        name = input("Enter patient name to delete: ")

        for patient in patients:
            if patient[0] == name:
                patients.remove(patient)
                print("Patient deleted")
                break

    elif choice == 3:
        name = input("Enter patient name to search: ")

        found = False

        for patient in patients:
            if patient[0] == name:
                print("Found:", patient)
                found = True

        if not found:
            print("Patient not found")

    elif choice == 4:
        print("Patient List:")
        for patient in patients:
            print("Name:", patient[0], "Age:", patient[1])

    elif choice == 5:
        print("Total Patients:", len(patients))

    elif choice == 6:
        break

    else:
        print("Invalid Choice")












