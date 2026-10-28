s = input("Enter text: ")
k = int(input("Shift: "))
res = ""
for ch in s:
    if ch.isalpha():
        res += chr((ord(ch)-65+k)%26+65) if ch.isupper() else chr((ord(ch)-97+k)%26+97)
    else:
        res += ch
print(res)
