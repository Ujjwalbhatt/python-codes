# write a python to read 4 number from the user and find the greatest from the user
a,b,c,d=map(int,input("Enter the four number: ").split())

big=a
if (b>big):
        big=b
if (c>big):
        big=c
if (d>big):
        big=d
print("the highest number is: ", big)
        
