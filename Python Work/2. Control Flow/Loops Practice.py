# Print all prime Numbers between 1 and 100 using nested for loops.
for i in range(2,101,1):
    isprime=True
    for j in range(2,i,1):
        if(i%j==0 and i!=j):
            isprime=False
            break
    if(isprime):
        print(i)