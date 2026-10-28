s = input("Enter string: ")
old = input("Old character: ")
new = input("New character: ")
res = ""
for ch in s:
    if ch == old:
        res += new
    else:
        res += ch
print(res)
