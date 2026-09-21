1. #String length:
text = input("Enter a string: ")
count = 0
for ch in text:
    count += 1
print("Length of the string is:", count)

2. #Character Count:
text = "Hello World! 123"
vowels = 0
consonants = 0
digits = 0
spaces = 0
specials = 0
for char in text:
    if char in "aeiouAEIOU":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        specials += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", specials)

3. #Reverse String:
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


4. #palidrome check
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

5. # uppercase and lowercase count 
s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

6. # Replace characters 

s = input("Enter a string: ")
old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")

result = s.replace(old_char, new_char)

print("Updated string:", result)

7. # Remove spaces
s = input("Enter a string: ")

result = s.replace(" ", "")

print("String without spaces:", result)

8. #Frequency of a character 

s = input("Enter a string: ")
ch = input("Enter the character to find: ")

count = s.count(ch)

print(f"'{ch}' appears {count} times.")

9. # first and last character 
s = input("Enter a string: ")

if len(s) > 0:
    print("First character:", s[0])
    print("Last character:", s[-1])
else:
    print("String is empty.")


10. #ASCII values
s = input("Enter a string: ")

for ch in s:
    print(ch, "->", ord(ch))

11. #Word count
s = input("Enter a sentence: ")

words = s.split()

print("Total words:", len(words))

12.#longest word
s = input("Enter a sentence: ")

words = s.split()

longest = max(words, key=len)

print("Longest word:", longest)

13.#Shortest word
s = input("Enter a sentence: ")

words = s.split()

shortest = min(words, key=len)

print("Shortest word:", shortest)


14.#Title case
s = input("Enter a sentence: ")

result = s.title()

print("Title Case:", result)

15.#Duplicate characters 
s = input("Enter a string: ")

duplicates = set()

for ch in s:
    if s.count(ch) > 1:
        duplicates.add(ch)

print("Duplicate characters:")
for ch in duplicates:
    print(ch)

16.# Remove Duplicate Characters

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)

 17.# Substring Search

main_string = input("Enter main string: ")
substring = input("Enter substring: ")

if substring in main_string:
    print("Substring found")
else:
    print("Substring not found")

18.# Count Occurrences of a Word

sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

count = sentence.split().count(word)

print("Occurrences:", count)

19.# Password Validator

import re

password = input("Enter password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"\d", password) and
    re.search(r"[@$!%*?&#]", password)):
    print("Valid Password")
else:
    print("Invalid Password")

20.# Run-Length Encoding

s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

print("Encoded String:", result)

21.# String Compression

s = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        compressed += s[i] + str(count)
        count = 1

compressed += s[-1] + str(count)

if len(compressed) < len(s):
    print("Compressed String:", compressed)
else:
    print("Original String:", s)

22.# Most Frequent Character

s = input("Enter a string: ")

max_char = max(s, key=s.count)

print("Most Frequent Character:", max_char)
print("Frequency:", s.count(max_char))

23.# Caesar Cipher

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in message:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch) - base + shift) % 26 + base)
    else:
        encrypted += ch

print("Encrypted Message:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        decrypted += chr((ord(ch) - base - shift) % 26 + base)
    else:
        decrypted += ch

print("Decrypted Message:", decrypted)

24.# Email Validator

import re

email = input("Enter email address: ")

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

25.# Word Frequency Dictionary

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency Dictionary:")
for word, count in frequency.items():
    print(word, ":", count)

26.# Character Frequency

s = input("Enter a string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Character Frequencies:")
for ch, count in freq.items():
    print(ch, ":", count)

27.# Anagram Check

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")

