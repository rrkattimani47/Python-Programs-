a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
a,b=b,a
print(a,b)

#or

x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))

x=x+y
y=x-y
x=x-y
print(x,y)
