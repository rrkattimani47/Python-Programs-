from array import *

arr=[]

n=int(input("how many values u want to enter:"))
for i in range(n):
    x=int(input("Enter value:"))
    arr.append(x)

print(arr)

key=int(input("Enter the key value: "))

count=0
for j in arr:
    if (j == key):
        print(count)
        break
        
    count+=1
