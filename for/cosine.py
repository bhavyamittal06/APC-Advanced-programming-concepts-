x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 1

for i in range(1, n + 1):
    fact = 1

    # Find factorial of 2*i
    for j in range(1, 2 * i + 1):
        fact = fact * j

    term = (x ** (2 * i)) / fact

    if i % 2 == 1:
        sum = sum - term
    else:
        sum = sum + term

print("Cos(x) =", sum)
