for i in range(1,101):
    if i%3==0 or i%5==0: #not divisible by 3 or 5 like 9,25
        continue

    if i%3==0 and i%5==0: #not divisible by both like 15
        continue
    
    print(i)

print("LOL")
