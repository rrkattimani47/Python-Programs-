#Python Program to Accept Three Digits and Print all Possible Combinations from the Digits


x=int(input("Enter a value:"))
y=int(input("Enter a value:"))
z=int(input("Enter a value:"))
d=[]
d.append(x)
d.append(y)
d.append(z)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i!=j and j!=k and k!=i:
                print(d[i],d[j],d[k])
