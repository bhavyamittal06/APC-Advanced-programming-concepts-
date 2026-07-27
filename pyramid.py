#print in pyramid
n = int(input("Enter a input N:"))
print  ( " " * (n-1) , end =" ")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j , end ="")
        print()
#print a pyramid 
n = int (input("Enter a number N :"))
for i in range(1,n+1):
    for j in range (1 , i +1):
        print(i , end= "")
        print()

#print a pyramid
n = int( input ("Enter a value of  N :"))
for i in range (1, n+1):
    for j in range(i , i+1):
        print(chr(64+j), end ="" )
        print()
#PRINT A DECLINING PYRAMID
n = int (input("Enter a value N:"))
#leading space 
print  ( " " * (n+1) , end =" ")
for i in range(n,0,-1):
    for j in range(i , i+1):
        print(chr(64+j),end="")
        print()




