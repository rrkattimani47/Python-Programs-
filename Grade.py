#Python Program to Take in the Marks of 5 Subjects and Display the Grade

s1=int(input("Enter the marks of sub 1:"))
s2=int(input("Enter the marks of sub 2:"))
s3=int(input("Enter the marks of sub 3:"))
s4=int(input("Enter the marks of sub 4:"))
s5=int(input("Enter the marks of sub 5:"))


avg=(s1+s2+s3+s4+s5)/5
print("Your avg is : ",avg)

if (avg>90):
    print("Your grade is: S+")

elif(avg>=70 and avg<=80):
    print("Your grade is: A")
    
elif(avg>=60 and avg<70):
    print("Your grade is : B")

elif(avg>50 and avg<60):
    print("Your grade is : C")
elif(avg<40):
    print("Sorry you Failed")
