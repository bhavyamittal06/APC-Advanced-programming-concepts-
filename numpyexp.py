import numpy as np

# 1. One-dimensional array containing 10 integers
print("1. One-Dimensional Array")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Array:", arr1)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)
print("Number of Dimensions:", arr1.ndim)

# --------------------------------------------------

# 2. Arithmetic Operations on Two Arrays
print("\n2. Arithmetic Operations")
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])

print("Array A:", a)
print("Array B:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# --------------------------------------------------

# 3. Maximum, Minimum, Sum, and Average
print("\n3. Array Statistics")
arr2 = np.array([12, 45, 67, 23, 89, 34, 56, 78, 90, 11])

print("Array:", arr2)
print("Maximum:", np.max(arr2))
print("Minimum:", np.min(arr2))
print("Sum:", np.sum(arr2))
print("Average:", np.mean(arr2))

# --------------------------------------------------

# 4. Boolean Indexing for Even and Odd Numbers
print("\n4. Even and Odd Numbers")
arr3 = np.arange(1, 21)

even = arr3[arr3 % 2 == 0]
odd = arr3[arr3 % 2 != 0]

print("Original Array:", arr3)
print("Even Numbers:", even)
print("Odd Numbers:", odd)

# --------------------------------------------------

# 5. Reshaping Array
print("\n5. Reshaping Array")
arr4 = np.arange(1, 13)

print("Original Array:", arr4)

print("\n2 x 6 Matrix:")
print(arr4.reshape(2, 6))

print("\n3 x 4 Matrix:")
print(arr4.reshape(3, 4))

print("\n4 x 3 Matrix:")
print(arr4.reshape(4, 3))

# --------------------------------------------------

# 6. Matrix Addition
print("\n6. Matrix Addition")
mat1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

mat2 = np.array([[9, 8, 7],
                 [6, 5, 4],
                 [3, 2, 1]])

print("Matrix 1:")
print(mat1)

print("Matrix 2:")
print(mat2)

print("Addition:")
print(mat1 + mat2)

# --------------------------------------------------

# 7. Matrix Multiplication
print("\n7. Matrix Multiplication")
m1 = np.array([[1, 2],
               [3, 4]])

m2 = np.array([[5, 6],
               [7, 8]])

print("Matrix 1:")
print(m1)

print("Matrix 2:")
print(m2)

print("Multiplication:")
print(np.matmul(m1, m2))

# --------------------------------------------------

# 8. Transpose of a 3 x 4 Matrix
print("\n8. Transpose of Matrix")
mat3 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

print("Original Matrix:")
print(mat3)

print("Transpose:")
print(mat3.T)

# --------------------------------------------------

# 9. Operations on a 4 x 4 Array
print("\n9. First Row and Last Column")
arr5 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

print("4 x 4 Array:")
print(arr5)

print("First Row:", arr5[0])
print("Last Column:", arr5[:, -1])

import numpy as np

#10 

import numpy as np

# Create a NumPy array containing numbers from 1 to 20
arr = np.arange(1, 21)

print("Original Array:", arr)

# First 5 elements
print("First 5 elements:", arr[:5])

# Last 5 elements
print("Last 5 elements:", arr[-5:])

# Alternate elements
print("Alternate elements:", arr[::2])

# Elements in reverse order
print("Elements in reverse order:", arr[::-1])

# 11. Slicing Operations
print("11. Slicing Operations")
arr = np.arange(1, 21)
print("Array:", arr)
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[-5:])
print("Alternate elements:", arr[::2])
print("Reverse order:", arr[::-1])

# --------------------------------------------------

# 12. Replace elements greater than 50 with 0
print("\n12. Replace Values > 50 with 0")
arr = np.array([10, 25, 60, 75, 40, 90, 15, 55, 30, 80])
print("Original Array:", arr)
arr[arr > 50] = 0
print("Modified Array:", arr)

# --------------------------------------------------

# 13. Sorting an Unsorted Array
print("\n13. Sorting Array")
arr = np.array([45, 12, 78, 34, 9, 67, 23])
print("Original Array:", arr)
print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])

# --------------------------------------------------

# 14. Unique Elements
print("\n14. Unique Elements")
arr = np.array([1, 2, 2, 3, 4, 4, 5, 6, 6, 7])
print("Original Array:", arr)
print("Unique Elements:", np.unique(arr))

# --------------------------------------------------

# 15. Concatenate Arrays
print("\n15. Concatenate Arrays")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Horizontal Concatenation:")
print(np.hstack((a, b)))

print("Vertical Concatenation:")
print(np.vstack((a, b)))

# --------------------------------------------------

# 16. Student Marks Statistics
print("\n16. Marks Statistics")
marks = np.array([78, 85, 92, 67, 88, 74, 95, 81, 69, 90])

print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

# --------------------------------------------------

# 17. Students Above Average
print("\n17. Students Above Average")
marks = np.array([55, 60, 72, 85, 90, 45, 78, 88, 67, 73,
                  81, 92, 58, 64, 70, 76, 83, 95, 62, 89])

avg = np.mean(marks)
print("Class Average:", avg)
print("Marks Above Average:", marks[marks > avg])

# --------------------------------------------------

# 18. 3D Array Information
print("\n18. 3D Array Information")
arr3d = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:\n", arr3d)
print("Dimensions:", arr3d.ndim)
print("Shape:", arr3d.shape)
print("Size:", arr3d.size)

# --------------------------------------------------

# 19. Access Elements in 3D Array
print("\n19. Accessing Elements")
arr3d = np.arange(1, 25).reshape(2, 3, 4)

print("First Element:", arr3d[0, 0, 0])
print("Last Element:", arr3d[1, 2, 3])
print("Element [0,1,2]:", arr3d[0, 1, 2])
print("Element [1,2,3]:", arr3d[1, 2, 3])

# --------------------------------------------------

# 20. Sum Operations on 3D Array
print("\n20. Sum Operations")
arr3d = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of All Elements:", np.sum(arr3d))
print("Sum of Each Layer:\n", np.sum(arr3d, axis=(1, 2)))
print("Sum Along Rows:\n", np.sum(arr3d, axis=1))
print("Sum Along Columns:\n", np.sum(arr3d, axis=2))

# --------------------------------------------------

# 21. Replace Values > 50 in Random 3D Array
print("\n21. Replace Values > 50 with 0")
arr3d = np.random.randint(1, 101, size=(2, 3, 4))

print("Original Array:\n", arr3d)
arr3d[arr3d > 50] = 0
print("Modified Array:\n", arr3d)

# --------------------------------------------------

# 22. Statistics of Random 3D Array
print("\n22. Statistics of Random 3D Array")
arr3d = np.random.randint(1, 101, size=(3, 4, 5))

print("Mean:", np.mean(arr3d))
print("Median:", np.median(arr3d))
print("Standard Deviation:", np.std(arr3d))
print("Variance:", np.var(arr3d))
print("Minimum:", np.min(arr3d))
print("Maximum:", np.max(arr3d))

# --------------------------------------------------

# 23. Flatten a 3D Array
print("\n23. Flatten 3D Array")
arr3d = np.arange(1, 25).reshape(2, 3, 4)

print("Original Array:\n", arr3d)
print("Flattened Array:\n", arr3d.flatten())

# --------------------------------------------------

# 24. Flatten and Calculate Statistics
print("\n24. Statistics on Flattened Array")
arr3d = np.arange(1, 28).reshape(3, 3, 3)
flat = arr3d.flatten()

print("Flattened Array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))

# --------------------------------------------------

# 25. Filter Elements from Flattened Random 3D Array
print("\n25. Filtering Elements")
arr3d = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr3d.flatten()

avg = np.mean(flat)

print("Elements Greater Than 50:")
print(flat[flat > 50])

print("Even Numbers:")
print(flat[flat % 2 == 0])

print("Elements Less Than Average:")
print(flat[flat < avg])

# --------------------------------------------------

# Additional: 4x4 Matrix Row and Column Sums
print("\nAdditional: Row and Column Sums")
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print("Matrix:\n", matrix)
print("Row Sums:", np.sum(matrix, axis=1))
print("Column Sums:", np.sum(matrix, axis=0))