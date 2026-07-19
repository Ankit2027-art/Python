# What is a While Loop?
'''A while loop is used to repeat a block of code as long as a condition is True.
-It checks the condition before every iteration.
-If the condition becomes False, the loop stops.'''

# Syntax
#      --while condition:
#     # Code to execute


'''i=1
while i<6:
    print(i)
    i=i+1

print("\n")

i=2
while i<18:
    print(i)
    i=i+2'''

# ==========================================
# 🟢 LEVEL 1: BASICS (1–10)
# ==========================================

# 1. Print numbers from 1 to 10 using a while loop.
'''i = 1
while i <= 10:
    print(i)
    i += 1'''

# 2. Print numbers from 10 to 1 in reverse order.
'''i = 10
while i >= 1:
    print(i)
    i -= 1'''

# 3. Print all even numbers from 1 to 50.
'''i = 1
print("The all even numbers from 1 to 50:")
while i <= 50:
    if i % 2 == 0:
        print(i,end=" ")
    i += 1'''

# 4. Print all odd numbers from 1 to 50.
'''i = 1
print("The all odd numbers from 1 to 50:")
while i <= 50:
    if i % 2 != 0:
        print(i,end=" ")
    i += 1'''


# 5. Print the multiplication table of a given number using a while loop.
'''num = int(input("Enter a number:"))
i = 1
while i <= 10:
    print(i,"X",num,"=",i*num)
    i += 1'''


# 6. Find the sum of numbers from 1 to N.
'''N = int(input("Enter a number:"))
sum = 0
i = 1
while i <= N:
    sum += i
    i += 1
print("The sum of 1 to ",N,"is:",sum)'''


# 7. Find the factorial of a number using a while loop.

'''N = int(input("Enter a number:"))
fact = 1
i = 1
while i <= N:
    fact *= i
    i += 1
print("The Factorial is:",fact)'''

# 9. Print all numbers divisible by both 3 and 5 between 1 and 100.
'''i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1'''

# 10. Print the square of numbers from 1 to 20.
'''i = 1
print("The square of numbers from 1 to 20.")
while i <= 20:
        print(i ** 2,end = " ")
        i += 1'''

# ==========================================
# 🟡 LEVEL 2: LOGIC BUILDING (11–20)
# ==========================================

# 11. Reverse a given number using a while loop.
'''num = int(input("Enter a number:"))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("The reverse of number is:",rev)'''

# 12. Count the number of digits in a given number.
'''digit = int(input("Enter a digit:"))
count = 0
while digit > 0:
    num = digit % 10
    count = count + 1
    digit = digit // 10
print("Total digits:",count)'''

# 13. Find the sum of digits of a number.
'''digit = int(input("Enter a digit:"))
sum = 0
while digit > 0:
    num = digit % 10
    sum = sum + num
    digit = digit // 10
print("The sum of digits:",sum)'''


# 14. Find the product of digits of a number.
'''digit = int(input("Enter a digit:"))
product = 1
while digit > 0:
    num = digit % 10
    product = product * num
    digit = digit // 10
print("The product of digits:",product)'''

# 15. Check whether a number is a palindrome.
'''num = int(input("Enter a number:"))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("The number is Palindrome")
else:
    print("The number is  not a Palindrome")'''


# 16. Check whether a number is an Armstrong number.

'''num = int(input("Enter a number:"))
temp = num
result = 0

count = 0
while temp >= 0:
    count += 1
    temp //= 10 

temp = num
while temp > 0:
    digit = temp % 10
    result = result + count
    temp = temp // 10
if result == num:
    print("The number is Armstrong")
else:
    print("The number is  not a Armstrong")'''


# 17. Check whether a number is a Strong number.
'''num = int(input("Enter a number:"))
temp = num
result = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    while digit > 0:
        fact *= digit
        digit -= 1

    result += fact

    temp = temp // 10
if result == num:
    print("The number is Strong number:")
else:
    print("The number is  Not Strong number:")'''

    


# 18. Find the largest digit in a number.
'''num = int(input("Enter a number:"))
temp = num
largest = 0

while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp = temp // 10
print("The largest digit in number is:",largest)'''



# 19. Find the smallest digit in a number.
'''num = int(input("Enter a number:"))
temp = num
Smallest = 9

while temp > 0:
    digit = temp % 10

    if digit < Smallest:
        Smallest = digit

    temp = temp // 10
print("The Smallest digit in number is:", Smallest)'''

# 20. Print the Fibonacci series up to N terms using a while loop.
'''N = int(input("Enter a value of N:"))
a = 0
b = 1
count = 0
while count <= N:
    print(a, end =" ")

    c = a + b
    a = b
    b = c

    count += 1'''



# ==========================================
# 🔵 LEVEL 3: INTERVIEW LEVEL (21–30)
# ==========================================

# 21. Check whether a number is a Prime number.

'''num = int(input("Enter a number:"))
temp = 1
count = 0
while temp <= num:
    if num % temp == 0:
        count += 1
    temp += 1

if count == 2:   
    print("The number is prime:")
else: 
    print("The number is not prime:")'''

    

# 22. Print all Prime numbers between 1 and N.

'''N = int(input("Enter the value of N: "))

i = 2
while i <= N:
    count = 0
    temp = 1

    while temp <= i:
        if i % temp == 0:
            count += 1
        temp += 1

    if count == 2:
        print(i,end=" ") 
    i += 1'''

# 23. Count the total Prime numbers between 1 and N.
'''N = int(input("Enter the value of N: "))

i = 2
total = 0
while i <= N:
    count = 0
    temp = 1
    
    while temp <= i:
        if i % temp == 0:
            count += 1
        temp += 1

    if count == 2:
        total += 1
    i += 1
print("The total Prime num between 1 to",N,":",total)'''

# 24. Find the HCF (GCD) of two numbers.

# 25. Find the LCM of two numbers.

# 26. Check whether a number is a Perfect number.

# 27. Check whether a number is a Harshad (Niven) number.

# 28. Convert a decimal number to binary using a while loop.

# 29. Print the reverse multiplication table of a given number.
'''num = int(input("Enter a number:"))
i = 10
while i >= 1:
    print(i,"X",num,"=",i * num)
    i -= 1'''


# 30. Create a Number Guessing Game using a while loop.
'''secret_number = 25
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        print("Total Attempts:", attempts)
        break
    elif guess < secret_number:
        print("Too Low! Try Again.")
    else:
        print("Too High! Try Again.")'''
