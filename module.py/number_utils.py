def prime(n):
    for i in range(2,n):
        if n%i==0:return False
    return True

def palindrome(n):
    return str(n)==str(n)[::-1]

def armstrong(n):
    s=0
    for d in str(n):
        s+=int(d)**len(str(n))
    return s==n

def perfect(n):
    return sum(i for i in range(1,n) if n%i==0)==n

# main.py
from number_utils import *
print(prime(11))