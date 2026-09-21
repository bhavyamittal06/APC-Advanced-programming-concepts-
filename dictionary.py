# Dictionary Experiments (1-35)

## 1. Student Details Dictionary


student = {
    "roll_no": 101,
    "name": "Bhavya",
    "department": "CSE",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)



## 2. Employee Information

employee = {
    "id": 1001,
    "name": "Rohan",
    "salary": 50000
}

key = input("Enter key: ")
print(employee.get(key, "Key not found"))


## 3. Add New Product


products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Bottle": 100,
    "Pencil": 5
}

products["Eraser"] = 3
print(products)


## 4. Update Student Marks


students = {"Amit": 80, "Riya": 75, "Siya": 90}

name = input("Enter student name: ")
if name in students:
    students[name] = int(input("Enter new marks: "))

print(students)


## 5. Remove City


cities = {
    "Mumbai": 20000000,
    "Delhi": 18000000,
    "Pune": 7000000
}

city = input("Enter city to remove: ")
cities.pop(city, None)

print(cities)

## 6. Check Employee ID


employees = {
    101: "Aman",
    102: "Rohan",
    103: "Priya"
}

eid = int(input("Enter employee ID: "))

if eid in employees:
    print("Exists")
else:
    print("Does not exist")


## 7. Count Key-Value Pairs


students = {"A": 80, "B": 90, "C": 70}
print("Total pairs:", len(students))


## 8. Display Keys, Values and Items


d = {"A": 1, "B": 2, "C": 3}

print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())


## 9. Programming Languages and Creators


languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie"
}

for lang, creator in languages.items():
    print(lang, ":", creator)


## 10. Accept Five Students and Marks


students = {}

for i in range(5):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print(students)


## 11. Highest Marks


students = {"A": 80, "B": 95, "C": 70}

topper = max(students, key=students.get)
print(topper, students[topper])


## 12. Lowest Marks


students = {"A": 80, "B": 95, "C": 70}

student = min(students, key=students.get)
print(student, students[student])


## 13. Average Marks


students = {"A": 80, "B": 95, "C": 70}

avg = sum(students.values()) / len(students)
print("Average:", avg)


## 14. Character Frequency


s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


## 15. Word Frequency


sentence = input("Enter sentence: ")

words = sentence.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)


## 16. Merge Two Dictionaries


d1 = {"A": 1, "B": 2}
d2 = {"C": 3, "D": 4}

d1.update(d2)

print(d1)


## 17. Common Keys


d1 = {"A": 1, "B": 2, "C": 3}
d2 = {"B": 5, "C": 7, "D": 8}

print(set(d1.keys()) & set(d2.keys()))


## 18. Common Values


d1 = {"A": 1, "B": 2, "C": 3}
d2 = {"X": 2, "Y": 3, "Z": 5}

print(set(d1.values()) & set(d2.values()))


## 19. Remove Duplicate Values


d = {"A": 1, "B": 2, "C": 2, "D": 3}

new_d = {}

for k, v in d.items():
    if v not in new_d.values():
        new_d[k] = v

print(new_d)


## 20. Sort Dictionary by Keys


d = {"C": 3, "A": 1, "B": 2}

for k in sorted(d):
    print(k, d[k])


## 21. Squares 1 to 10


d = {i: i*i for i in range(1, 11)}
print(d)


## 22. Squares of Even Numbers


d = {i: i*i for i in range(2, 21, 2)}
print(d)


## 23. Frequency of Numbers


nums = [1,2,2,3,4,4,4]

freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)


## 24. Cubes 1 to 10


d = {i: i**3 for i in range(1, 11)}
print(d)


## 25. Student Management System


students = {}

while True:
    print("\n1.Add 2.Update 3.Delete 4.Search 5.Display 6.Highest 7.Average 8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Name: ")
        marks = int(input("Marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Name: ")
        if name in students:
            students[name] = int(input("New Marks: "))

    elif choice == 3:
        name = input("Name: ")
        students.pop(name, None)

    elif choice == 4:
        name = input("Name: ")
        print(students.get(name, "Not Found"))

    elif choice == 5:
        print(students)

    elif choice == 6:
        if students:
            top = max(students, key=students.get)
            print(top, students[top])

    elif choice == 7:
        if students:
            print(sum(students.values()) / len(students))

    elif choice == 8:
        break


## 26. Employee Salary Analysis


employees = {
    "A": 60000,
    "B": 40000,
    "C": 70000,
    "D": 55000
}

print("Highest:", max(employees.values()))
print("Lowest:", min(employees.values()))
print("Average:", sum(employees.values()) / len(employees))

for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)


## 27. Product Inventory


products = {
    "Pen": 5,
    "Book": 15,
    "Bag": 8
}

products["Bottle"] = 20
products["Pen"] = 10

products.pop("Bag", None)

search = input("Enter product: ")
print(products.get(search, "Not Found"))

for p, q in products.items():
    if q < 10:
        print(p, q)


## 28. Phone Directory


contacts = {}

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == 2:
        name = input("Name: ")
        print(contacts.get(name, "Not Found"))

    elif ch == 3:
        name = input("Name: ")
        if name in contacts:
            contacts[name] = input("New Phone: ")

    elif ch == 4:
        name = input("Name: ")
        contacts.pop(name, None)

    elif ch == 5:
        print(contacts)

    elif ch == 6:
        break


## 29. Book Dictionary


books = {}

while True:
    print("\n1.Add 2.Search 3.Remove 4.Display 5.Count 6.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        bid = input("Book ID: ")
        name = input("Book Name: ")
        books[bid] = name

    elif ch == 2:
        bid = input("Book ID: ")
        print(books.get(bid, "Not Found"))

    elif ch == 3:
        bid = input("Book ID: ")
        books.pop(bid, None)

    elif ch == 4:
        print(books)

    elif ch == 5:
        print("Total Books:", len(books))

    elif ch == 6:
        break

## 30. Group Students by Department


students = {
    "Amit": "CSE",
    "Riya": "IT",
    "Rohan": "CSE",
    "Siya": "IT"
}

result = {}

for name, dept in students.items():
    result.setdefault(dept, []).append(name)

print(result)

## 31. Group Words by Length

words = ["cat", "dog", "apple", "bat", "orange"]

result = {}

for word in words:
    result.setdefault(len(word), []).append(word)

print(result)


## 32. Two Sum Using Dictionary


nums = [2, 7, 11, 15]
target = 9

d = {}

for i, num in enumerate(nums):
    diff = target - num

    if diff in d:
        print(d[diff], i)

    d[num] = i


## 33. First Non-Repeating Character


s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break

## 34. First Repeating Character


s = input("Enter string: ")

seen = {}

for ch in s:
    if ch in seen:
        print(ch)
        break
    seen[ch] = 1


## 35. Word Length Frequency

paragraph = input("Enter paragraph: ")

words = paragraph.split()

freq = {}

for word in words:
    length = len(word)
    freq[length] = freq.get(length, 0) + 1

print(freq)
