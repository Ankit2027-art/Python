# How to take input by user

# a=input("enter a value of a:")
a=int(input("enter a value of a:"))

# a=int(a)
b=input("enter value of b:")
b=int(b)

print(a+b)


c=int(input("enter a number"))
d=int(input("enter a number"))

print(c+d)

# How to take multiple input by user

a,b,c =map(int,input("Enter a value of a,b,c:",).split())
print(a)
print(b)
print(c)