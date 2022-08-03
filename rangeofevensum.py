# find the sum of even number in the give range p & q

p=int(input("Enter the starting range of list"))
q=int(input("Enter the end range of list"))
sum=0
i=0
for i in range(p,q+1):
        if(i%2==0):
            sum=sum+i
print("The sum of even number in the given range is: ",sum)
