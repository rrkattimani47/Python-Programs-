def fact(m,n):
    temp=[]
    for i in range(m,n+1):
        res=1
        for j in range(1,i+1):
            res*=j
        temp.append(res)
    print(temp)


a=int(input("Enter value a :"))
b=int(input("Enter value b : "))
fact(a,b)
