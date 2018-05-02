x=int(input("Please enter the number: "))
for i in range(1,x+1):
    y=x%i
    if y==0:
       print (i)