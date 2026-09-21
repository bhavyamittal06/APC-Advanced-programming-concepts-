def add(a,b): return a+b

# mathutils/number.py
def palindrome(n): return str(n)==str(n)[::-1]

# mathutils/statistics.py
def mean(lst): return sum(lst)/len(lst)

# main.py
from mathutils.basic import add
print(add(2,3))