# Packing Tuple
tuple1= 10,3.4,"Amir",True
print(tuple1)

# Unpacking Tuples
num,pival,name,boolval=tuple1
print(num,pival,name,boolval)

# Unpacking Tuples with *
start,*middle,end=tuple1
print(start,middle,end)

# Tuple Applications
# Apllication 1: Returning Multiple values from function
def returntwovalues():
    return (3,4)

x,y=returntwovalues()
print(x,y)

# Application 2: Passing arguments as args* to a function The * in *numbers means:
# "Take any number of positional arguments..."
# "...and pack them into a single tuple named numbers."
def sumallnumbers(*numbers):
    return sum(numbers)

print(sumallnumbers(1,2,3,4,5))

# Application :03 Tuples are hashable, so they can be used as keys in dictionaries (lists can’t).
locations={('Lahore','Pakistan'):'hot',('Toronto','Canada'):'cold'}