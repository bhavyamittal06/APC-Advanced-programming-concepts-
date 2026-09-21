f = open("student.txt", "w")
f.write("Hello")
f.close()

#2 
f = open("student.txt", "r")
data = f.read()
f.close()

print(data)

#3
f = open("student.txt", "a")
f.write("\nNew Data")
f.close()

#4
f = open("student.txt", "r")

for line in f:
    print(line)

f.close()
#6

f = open("student.txt", "r")

data = f.read()      # read complete file
words = data.split() # convert into list of words

count = len(words)

print("Total words =", count)

f.close()

#7

f = open("students.txt" , "r")

data = f.read()

count = len(data)

print("Total characters =", count)
f.close()

#8

f = open("student.txt", "r")

lines = f.readlines()

for line in reversed(lines):
    print(line)

f.close()

#9
f.open("student.txt" , "r")
data = f.read
vowels = f.split ()
consonants = f.split()

count = len(vowels , consonants)

print("Total vowels =" , count)
print("Total consonants =" , count)

f.close()



f = open("student.txt", "r")

data = f.read()

vowels = 0
consonants = 0

for ch in data:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Total vowels =", vowels)
print("Total consonants =", consonants)

f.close()


#10
f=open("student.txt","r");d=f.read();a=b=c=s=0
for ch in d:
    if ch.isalpha():a+=1
    elif ch.isdigit():b+=1
    elif ch.isspace():c+=1
    else:s+=1
print(a,b,c,s);f.close()

#11
f=open("student.txt","r");w=f.read().split();print(max(w,key=len));f.close()

#12
f=open("student.txt","r");w=f.read().split();d={}
for i in w:d[i]=d.get(i,0)+1
print(d);f.close()

#13
word=input("Enter word: ");f=open("student.txt","r");count=0
for n,line in enumerate(f,1):
    if word in line:
        print(n);count+=line.count(word)
print(count);f.close()

#14
old=input("Old word: ");new=input("New word: ");f=open("student.txt","r");d=f.read();f.close();d=d.replace(old,new);f=open("student.txt","w");f.write(d);f.close()

#15
f=open("source.py","r");g=open("newfile.py","w")
for line in f:
    if not line.strip().startswith("#"):g.write(line)
f.close();g.close()

#16
f=open("student.txt","r");d=f.read().upper();f.close();g=open("upper.txt","w");g.write(d);g.close()

#17
f=open("students.txt","r");lines=f.readlines()[1:];total=0;high=0;name=""
for l in lines:
    r,n,m=l.strip().split(",");m=int(m);print(r,n,m);total+=m
    if m>high:high=m;name=n
print(name,high);print(total/len(lines))
for l in lines:
    r,n,m=l.strip().split(",")
    if int(m)>80:print(n)
f.close()

#18
f=open("employee.txt","r");lines=f.readlines();total=0;high=0;emp=""
for l in lines:
    i,n,d,s=l.strip().split(",");s=float(s);total+=s
    if s>high:high=s;emp=n
print(emp,high);print(total/len(lines))
x=float(input())
for l in lines:
    i,n,d,s=l.strip().split(",")
    if float(s)>x:print(n)
f.close()

#19
f=open("attendance.txt","r")
for l in f:
    n,p,t=l.strip().split(",");per=(int(p)/int(t))*100;print(n,per)
    if per<75:print(n)
f.close()

#20
f=open("bank.txt","r");dep=withd=0;largest=0
for l in f:
    t,amt=l.strip().split(",");amt=float(amt);largest=max(largest,amt)
    if t=="D":dep+=amt
    else:withd+=amt
print(dep,withd,dep-withd,largest);f.close()

#21
book=input();f=open("books.txt","r")
for l in f:
    bid,title,author,status=l.strip().split(",")
    if title==book:print(l)
f.close()

#22
f1=open("file1.txt","r");f2=open("file2.txt","r");f3=open("file3.txt","w");f3.write(f1.read());f3.write(f2.read());f1.close();f2.close();f3.close()

#23
f1=open("file1.txt","r");f2=open("file2.txt","r");a=f1.readlines();b=f2.readlines()
if a==b:print("Identical")
else:
    for i in range(min(len(a),len(b))):
        if a[i]!=b[i]:
            print(i+1);break
f1.close();f2.close()






