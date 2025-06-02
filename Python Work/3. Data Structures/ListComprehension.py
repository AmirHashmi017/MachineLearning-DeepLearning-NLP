#List containing square of all numbers form 1 to 10
squares=[i**2 for i in range(1,11,1)]
print(squares)

#List Containing all Even Numbers from 1 to 10
evens=[i for i in range(1,11,1) if i%2==0]
print(evens)

# List containing suare of numbers if they are ven and simple numbers if they are odd form 1 to 10
list=[i**2 if i%2==0 else i for i in range(1,10,1)]
print(list)

#List conating all pairs of list1 and list2
list1=[1,2,3,4]
list2=['a','b','c']
pairs=[[i,j] for i in range(0,4,1) for j in range(0,3,1)]
print(pairs)

#List Containg all prime numbers from 2 to 10
primes=[i for i in range(2,20,1) if all(i%j!=0 for j in range(2,i,1))]
print(primes)
# all() function is used to check if all iterables are true
# any() function is used to check if any iterable is true

# calling function through list comprehension
words=["Amir","Ashir",'ALi']
lengths=[len(word) for word in words]
print(lengths)
