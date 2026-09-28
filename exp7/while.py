# Print numbers from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1

print("Loop finished!")

#PRNT NATURAL NUMBER UPTO N 
n = int(input("Enter the value of N: "))

count = 1
while count <= n:
    print(count)
    count += 1

    #PRINT EVEN NUMBERS UPTO N 
n = int(input ("Enter a even number "))
count = 2
while count <=n:
    print (count)
    count += 2

# print multiples of 2
n = int(input ("Enter a number N : "))
limit = 2*n
count = 2
while count <=n:
    print (count)
    count +=2
#print in pyramid
n = int(input("Enter a input N:"))
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