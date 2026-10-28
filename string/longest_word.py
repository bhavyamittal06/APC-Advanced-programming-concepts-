s = input("Enter sentence: ")
words = s.split()
long = words[0]
for w in words:
    if len(w) > len(long):
        long = w
print(long)
