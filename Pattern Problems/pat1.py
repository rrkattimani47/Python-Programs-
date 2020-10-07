"""Print the pattern as follows 
1
12
123
1234
12345
123456
1234567
12345678
123456789
12345678910 """


n=10
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i<=j:
            print(k,end='')
            k+=1
        else:
            print('',end='')
    print()
