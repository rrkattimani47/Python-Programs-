"""Print the pattern as follows
*
**
***
****
*****
******
*******
********
*********
********** """
n=10
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i<=j:
            print("*",end='')
            k+=1
        else:
            print('',end='')
    print()
