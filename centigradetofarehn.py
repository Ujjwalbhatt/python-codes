li=[]
n=int(input("Enter the range of list"))
f=0
i=0
c=0
for i in range(0,n):
    f=int(input("Enter the temperature"))
    li.append(f)
for i in range(0,n):
    c=int(((li[i]-32)*5)/9)
    print(c)