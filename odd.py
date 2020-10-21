#The program takes the upper and lower limit and prints all odd numbers within a given range.

l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))

for i in range(l,u):
    if(i%2!=0):
        print(i)
