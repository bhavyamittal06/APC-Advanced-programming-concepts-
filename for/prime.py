n = int(input("Enter number: "))

r = int(n ** 0.5)

count = 0

for i in range(1, r + 1):
    if r % i == 0:
        count = count + 1

if count == 2:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
