s = input("Enter string: ")
m = ""
c = 0
for ch in s:
    if s.count(ch) > c:
        c = s.count(ch)
        m = ch
print(m)
