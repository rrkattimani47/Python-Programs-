av=10
x=int(input("How many candies you want:\n"))
i=1
count=0

while i<=x:
    if i>av:
        
        print("Out of stock")
        break
    count+=1
    print(count,"Candy")
    
    i+=1

print("Thank you, visit again")
