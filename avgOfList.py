z=int(input("Enter the size:"))
a=[]
for i in range(0,z):
      ele=int(input("Enter the value:"))
      a.append(ele)
avg=sum(a)/z
print(round(avg,5))
