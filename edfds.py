# write a python to read 4 number from the user and find the greatest from the user

n=int(input("Enter the number: "))
n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
n3=int(input("Enter the number: "))
if (n>n1 and n>n2 and n>n3):
        print(n , " is the greatest")
elif (n1>n and n1>n2 and n1>n3):
        print(n1 , " is the greatest")
elif (n2>n1 and n2>n and n2>n3):
        print(n2 , " is the greatest")
else:
        print(n3 , " is the greatest")
    