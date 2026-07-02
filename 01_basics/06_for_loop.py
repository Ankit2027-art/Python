# “A for loop in Python is used to repeat a block of code multiple times.
# It is mainly used for iterating over a sequence like a list, string, or range of numbers.”


'''for i in range(1,6): #RANGE FUNCTION GOES from 1 to 5
    print(i  )


 
#the range function goes fron first number to 2 nd number -1(2nd-1)

for i in range(1,11):
    print("5 X",i,"=",5*(i))

print(("\n"))


for i in range(1,11):
    print("10 x",i,"=",10*(i))


 

for i in range(1,11):
    print("5*",i,"=",i*5)'''

#Print num from 1 to 10
'''for i in range(1,11):
    print(i)'''
#print even num between 1 and 50
'''for i in range(1,51):
    if i % 2 ==0:
        print(i)'''
   
#muliplication of 5
'''for i in range(1,11):
    print("5 X",i,"=",i*5)'''

#sum of num 1to 100

'''total = 0
for i in range(1, 101):
    total += i

print("Sum of numbers from 1 to 100 is:", total)'''




# ++++++++++++++++++++BASICS+++++++++++++++++++++++++++

# Print numbers from 1 to N.
'''N=int(input("Enter a Value of N:"))
for i in range(1,N+1):
    print(i)'''

# Print N to 1.
'''N = int(input("Enter a value of N:"))
for i in range(N,0,-1):
    print(i)'''

# Print even numbers from 1 to N.
'''N = int(input("Enter a value of N:"))
print("The Even number between 1 to ",N,"is : ")
for i in range(1,N+1):
    if i % 2 == 0:
        print(i,end =" ")'''

# Print odd numbers from 1 to N.
'''N = int(input("Enter a value of N:"))
print("The Odd number between 1 to ",N,"is : ")
for i in range(1,N+1):
    if i % 2 != 0:
        print(i,end =" ")'''

# Print multiples of 5.
'''N = int(input("Enter a value of N:"))
print("The Multiplies of 5 between 1 to ",N,"is : ")
for i in range(1,N+1):
    if i % 5 == 0:
        print(i,end =" ")'''

# Print the multiplication table of a number.
'''num = int(input("Enter a number:"))
for i in range(1,11):
    print(num ,"X", i ,"=",num*i)'''

# Find the sum of numbers from 1 to N.
'''N = int(input("Enter a value of N:"))
sum = 0
for i in range(1,N+1):
    sum += i

print(sum)'''

# Find the factorial of a number.
'''num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial =", fact)'''




