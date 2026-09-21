#33 Square of a number 

square = lambda x: x * x
print(square(5))

# 34. Cube of a number
cube = lambda x: x ** 3
print(cube(4))

# 35. Check even or odd
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(8))

# 36. Maximum of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))

# 37. Simple Interest
si = lambda p, r, t: (p * r * t) / 100
print(si(10000, 5, 2))

# 38. Squares of all numbers using map()
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, nums))
print(result)

# 39. Cubes of all numbers using map()
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 3, nums))
print(result)

# 40. Sum of corresponding elements of two lists
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)

# 41. Extract even numbers using filter()
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

# 42. Extract prime numbers using filter()
nums = [2, 3, 4, 5, 6, 7, 8, 9, 11]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

result = list(filter(lambda x: is_prime(x), nums))
print(result)


# 43. Extract positive numbers
nums = [-5, -2, 0, 3, 7, -1, 9]
result = list(filter(lambda x: x > 0, nums))
print(result)

# 44. Numbers greater than 50
nums = [10, 60, 45, 80, 100, 30]
result = list(filter(lambda x: x > 50, nums))
print(result)


# 45. Words having more than 5 characters
words = ["apple", "banana", "cat", "elephant", "dog"]
result = list(filter(lambda x: len(x) > 5, words))
print(result)

# 46. Sort words according to length
words = ["apple", "banana", "cat", "elephant", "dog"]
result = sorted(words, key=lambda x: len(x))
print(result)

# 48. Sort employees according to salary
employees = [("Amit", 50000), ("Riya", 70000), ("Karan", 45000)]
result = sorted(employees, key=lambda x: x[1])
print(result)


# 49. Student records operations
students = [("Amit", 80), ("Riya", 92), ("Karan", 70), ("Siya", 85)]

# a) Average marks
avg = sum(map(lambda x: x[1], students)) / len(students)
print("Average:", avg)

# b) Students above 75
above75 = list(filter(lambda x: x[1] > 75, students))
print("Above 75:", above75)

# c) Sort by marks
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted:", sorted_students)


# 50. Employee records operations
employees = [
    ("Amit", "IT", 40000),
    ("Riya", "HR", 60000),
    ("Karan", "IT", 45000)
]

# a) Salary > 50000
high_salary = list(filter(lambda x: x[2] > 50000, employees))
print(high_salary)

# b) Increase salary by 10%
updated = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))
print(updated)

# c) Sort by salary
sorted_emp = sorted(employees, key=lambda x: x[2])
print(sorted_emp)



# 51. Product records operations
products = [
    ("Laptop", 50000, 2),
    ("Phone", 20000, 5),
    ("Mouse", 500, 10)
]

# a) Total value
total_value = list(map(lambda x: (x[0], x[1] * x[2]), products))
print(total_value)

# b) Products costing more than 1000
costly = list(filter(lambda x: x[1] > 1000, products))
print(costly)

# c) Sort by total value
sorted_products = sorted(products, key=lambda x: x[1] * x[2])
print(sorted_products)

# Program using functions, map(), filter(), and lambda expressions

# Function to find length of every word
def word_lengths(words):
    return list(map(lambda x: len(x), words))

# Function to extract words having more than 5 characters
def long_words(words):
    return list(filter(lambda x: len(x) > 5, words))

# Function to sort words according to length
def sort_by_length(words):
    return sorted(words, key=lambda x: len(x))

# Main Program
words = ["apple", "banana", "cat", "elephant", "dog", "computer"]

print("Original List:", words)

# a) Length of every word
print("Lengths of words:", word_lengths(words))

# b) Words having more than five characters
print("Words with more than 5 characters:", long_words(words))

# c) Words sorted according to length
print("Words sorted by length:", sort_by_length(words))

#1
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))

#2

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(check_even_odd(7))

#3
def greater(a, b):
    if a > b:
        return a
    return b

print(greater(10, 20))

#4

def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest(10000, 5, 2))

#5
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(11))

#6
def area_circle(r):
    return 3.14 * r * r

print(area_circle(5))

#Sum of First n Natural Numbers
def sum_n(n):
    return n * (n + 1) // 2

print(sum_n(10))
#8. Power Function
def power(base, exponent):
    return base ** exponent

print(power(2, 5))
#9. Largest Element in a List (Without max())
def largest(lst):
    largest_num = lst[0]

    for num in lst:
        if num > largest_num:
            largest_num = num

    return largest_num

print(largest([10, 25, 8, 40, 15]))
# 10. Count Vowels in a String
def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("Programming"))

# 11. Reverse a String
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))


# 12. Check Palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))


# 13. Average of Numbers in a List
def average(lst):
    return sum(lst) / len(lst)

print(average([10, 20, 30, 40, 50]))


# 14. Count Occurrences of an Element
def count_occurrences(lst, element):
    return lst.count(element)

print(count_occurrences([1, 2, 3, 2, 4, 2], 2))


# 15. Return Unique Elements from a List
def unique_elements(lst):
    return list(set(lst))

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))


# 16. Find Second Largest Number
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

print(second_largest([10, 20, 30, 40, 50]))


# 17. First n Fibonacci Numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
print()


# 18. Student Percentage and Grade
def student_result(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return percentage, grade

per, grade = student_result([80, 85, 90, 75, 95])
print("Percentage:", per)
print("Grade:", grade)


# 19. Electricity Bill Calculation
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

print(electricity_bill(250))


# 20. Gross Salary Calculation
def gross_salary(basic):
    hra = 0.20 * basic
    da = 0.10 * basic
    return basic + hra + da

print(gross_salary(50000))


# 21. Total Bill After Discount
def total_bill(price, quantity):
    total = price * quantity

    if total > 5000:
        total *= 0.90     # 10% discount

    return total

print(total_bill(1000, 6))


# 22. Minimum, Maximum, Sum and Average
def statistics(lst):
    minimum = min(lst)
    maximum = max(lst)
    total = sum(lst)
    avg = total / len(lst)

    return minimum, maximum, total, avg

print(statistics([10, 20, 30, 40, 50]))


# 23. Student Records Processing
def grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

students = [
    ["Amit", 1, [80, 85, 90, 75, 95]],
    ["Riya", 2, [70, 75, 80, 85, 90]],
    ["Karan", 3, [60, 65, 70, 75, 80]]
]

totals = []

for name, roll, marks in students:
    total = sum(marks)
    percentage = total / 5
    totals.append(total)

    print("Name:", name)
    print("Roll No:", roll)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade(percentage))
    print()

print("Class Average:", sum(totals) / len(totals))
print("Highest Score:", max(totals))
print("Lowest Score:", min(totals))


# 24. Bank Account Operations
balance = 10000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient Balance")

def balance_enquiry():
    print("Current Balance:", balance)

deposit(5000)
withdraw(3000)
balance_enquiry()


# 25. Library Management System using Dictionary

books = {
    "Python": True,
    "Java": True,
    "C++": True
}

def add_book(book):
    books[book] = True

def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        print("Book Issued")
    else:
        print("Book Not Available")

def return_book(book):
    if book in books:
        books[book] = True
        print("Book Returned")

def search_book(book):
    if book in books:
        print("Book Found")
    else:
        print("Book Not Found")

def display_books():
    print("Available Books:")
    for book, status in books.items():
        if status:
            print(book)

display_books()


# 26. Electricity Bill with Slabs, Tax and Discount

def calculate_bill(units):
    if units <= 100:
        amount = units * 5
    elif units <= 200:
        amount = 100 * 5 + (units - 100) * 7
    else:
        amount = 100 * 5 + 100 * 7 + (units - 200) * 10

    fixed_charge = 100
    tax = 0.05 * amount

    total = amount + fixed_charge + tax

    if total > 2000:
        total *= 0.90

    return total

print(calculate_bill(250))


# 27. Hospital Billing System

def consultation_charge():
    return 500

def laboratory_charge():
    return 1000

def medicine_charge():
    return 1500

def room_charge(days):
    return days * 2000

def final_bill(category, days):
    total = consultation_charge() + laboratory_charge() + medicine_charge() + room_charge(days)

    if category == "Senior":
        total *= 0.90
    elif category == "Employee":
        total *= 0.85

    return total

print(final_bill("Senior", 3))


# 28. Shopping Invoice System

cart = {}

def add_product(name, price):
    cart[name] = price

def remove_product(name):
    if name in cart:
        del cart[name]

def subtotal():
    return sum(cart.values())

def apply_coupon(total):
    if total > 5000:
        return total * 0.90
    return total

def gst(total):
    return total * 0.18

def final_invoice():
    total = subtotal()
    total = apply_coupon(total)
    total += gst(total)
    return total

add_product("Laptop", 50000)
add_product("Mouse", 500)

print(final_invoice())


# 29. Recursive Binary Search

def binary_search(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 0, len(arr)-1, 40))


# 30. Decimal to Binary using Recursion

def decimal_to_binary(n):
    if n == 0:
        return ""

    return decimal_to_binary(n // 2) + str(n % 2)

num = 13
print(decimal_to_binary(num))


# 31. Palindrome using Recursion

def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

print(palindrome("madam"))


# 32. Calculator using Function as Argument

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(operation, a, b):
    return operation(a, b)

print(calculate(add, 10, 5))
print(calculate(subtract, 10, 5))
print(calculate(multiply, 10, 5))
print(calculate(divide, 10, 5))