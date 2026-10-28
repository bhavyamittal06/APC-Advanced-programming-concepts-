s = input("Enter sentence: ")
words = s.split()
small = words[0]
for w in words:
    if len(w) < len(small):
        small = w
print(small)
