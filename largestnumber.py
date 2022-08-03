# largest number among the list
li=[]
n=int(input("Enter the range of list"))
max=0
i=0

for i in range(0,n):
    li.append(int(input("Enter the number")))
max=li[0]
for i in range(1,n):
    if(max<li[i]):
        max=li[i]
print(max)