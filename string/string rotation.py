a = input("First string: ")
b = input("Second string: ")
if len(a) == len(b) and b in a+a:
    print("Yes")
else:
    print("No")
