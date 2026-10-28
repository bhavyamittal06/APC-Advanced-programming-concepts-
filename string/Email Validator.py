s = input("Enter paragraph: ")
words = s.split()
done = []
for w in words:
    if w not in done:
        print(w, words.count(w))
        done.append(w)
