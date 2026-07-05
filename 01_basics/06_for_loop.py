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



# Print squares of numbers from 1 to N.
'''N = int(input("Enter the value of N:"))
squ = 0
print("The Square of numbers is:")
for i in range(1,N+1):
    squ = i * i
    print(squ,end=" ")'''


# Print cubes of numbers from 1 to N.
'''N = int(input("Enter the value of N:"))
print("The Square of numbers is:")
for i in range(1,N+1):
    # print(i * i * i,end=" ")
    print(i ** 3, end = " ")'''

#level - 2

# Count how many numbers are even between 1 and N.
'''N = int(input("Enter a value of N:"))
count = 0
for i in range(1,N+1):
    if i % 2 == 0:
        count += 1
print("The Even number between 1 to",N,"is :", count)'''

# Count how many numbers are divisible by 3 and 5.
'''N = int(input("Enter a value of N:"))
count = 0
for i in range(1,N+1):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print("The total number are divisible by 3 and 5 between 1 to",N,"is :", count)'''


# lopp with string

# Print each character of a given string using a for loop.
'''string = "HelloAnkit"
for ch in string:
    print(ch ,end =" ")'''
# M2
'''string = input("Enter a string")
for i in range(len(string)):
    print(string[i])'''


# Count the total number of characters in a string (without using len()).
'''string = input("Enter a string:")
count = 0
for ch in string:
    count = len(string)
print(count)'''

# Count the number of vowels (a, e, i, o, u) in a string.
'''string = input("Enter a string: ")
count = 0

for ch in string:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count += 1

print(count)'''

#m2
'''string = input("Enter a string:")
vowel ="aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowel:
        count += 1
print("Number of vowels:",count)'''
    
    

# Count the number of uppercase letters and lowercase letters in a string.
'''string = input("Enter a string:")
upper = 0
lower = 0
for ch in string:
    if ch in ch.upper():
        upper += 1
    elif ch in ch.lower():
        lower += 1
print("The total uppercase letter in string:",upper)
print("The total uppercase letter in string:",lower)'''

# Count the number of digits, alphabets, and special characters in a string.
'''string =input("Enter a  String:")
alphabets = 0
specialch = 0
digit = 0
for ch in string:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digit += 1
    else:
        specialch += 1
print("The total no ofalphabets in string:",alphabets)
print("The total no of digit in string:",digit)
print("The total no of special character in string:",specialch)'''


# Reverse a string using a for loop (without using slicing [::-1]).
'''string = input("Enter a String:")
rev = ""
for ch in string:
    rev = ch + rev
print("Reverse String:",rev)'''

# Count the frequency of each character in a string.
string = input("Enter a String:")
freq = {}
for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(" Character Frequent:")
for ch in freq:
    print(ch,":", freq[ch])

    
# Remove all vowels from a string using a for loop.
'''s = input("Enter a String:")
result = " "
vowels ="aeiouAEIOU"
for ch in s:
    if ch not in vowels:
        result += ch
print("String:",result)'''

# Find the first non-repeating character in a string.

string = input("Enter a string:")
freq = {}
result = ""
for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

found = False
for ch  in freq:
    if freq[ch] == 1:
        print("First non-repeating character is:",ch)
        found = True
        break
if not found:
    print("No non-repeating character found.")
        

# Check whether two strings are anagrams using a for loop.

'''s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    found = True

    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            found = False
            break

    if found:
        print("Anagram")
    else:
        print("Not Anagram")'''






    



