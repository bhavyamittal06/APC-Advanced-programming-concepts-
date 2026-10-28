s = input("Enter string: ")
for i in s:
    if s.count(i) > 1:
        print(i, end=" ")
