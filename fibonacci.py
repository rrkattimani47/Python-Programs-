def fib(n):
    a=0
    b=1
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        if(c<=n):
            print(c)


n=int(input("Enter val"))
fib(n)
