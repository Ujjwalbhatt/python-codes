# Armstrong number using python
sum=0
t=0
n=int(input("Enter the number: "))
temp=n
k = len(str(n)) # To determine the number of digits in an integer

while n>0:
    t=n%10
    sum=sum+t**k
    n=n//10
if (temp==sum):
    print("Number is armstrong!")
else:
    print("Number is not armstrong!")