# Functions in Python

'''A function is a block of reusable code that performs a specific task. Instead of writing the same code again and again, you write it once inside a function and call it whenever needed.'''


# Syntax
'''def function_name():
    # code'''

'''def greet():
    print("Hello, Welcome to Python!")

greet()'''

# Parts of a Function
'''def greet():
    print("Hello")

def   → Keyword used to define a function.
greet → Function name.
()    → Parentheses (parameters go here).
:     → Starts the function body.
Indented code → Function body.'''

# Function with Parameters

'''Parameters allow you to pass data into a function.

def greet(name):
    print("Hello", name)

greet("Ankit")'''


# Function with Multiple Parameters
'''def add(a, b):
    print(a + b)
add(10, 20)'''

#Function with return value
'''def add(a, b):
    return a + b
result = add(5, 10)
print(result)'''

# Real-Life Example 🎁
"""
Socho tum restaurant gaye.
Without return

Tum waiter se bole:
"Mera bill batao."
Waiter bolta hai:
"₹500"
Aur chala jata hai.
Tumne sun liya, lekin tumhare haath me bill nahi aaya.
Ye print() jaisa hai.
With return

Tum waiter se bole:
"Mera bill do."
Waiter tumhare haath me bill de deta hai.
Ab tum us bill ko:
Save kar sakte ho.
Kisi aur ko de sakte ho.
Calculate kar sakte ho.

Ye return hai."""


# Built-in Functions

'''Python already provides many functions.

print("Hello")

len("Python")

type(10)

max(10,20,30)

min(5,2,8)

sum([1,2,3])'''

# User-defined Function

'''Functions created by the programmer.'

def square(num):
    return num * num

print(square(5))'''


# Types of Functions
    # 1. No Parameter, No Return
'''def hello():
    print("Hello")
hello()'''

    #  2. Parameter, No Return
'''def greet(name):
    print("Hello",name)
greet("Nikhil")'''

    # 3.No Parameter Return
'''def number():
    return 100
print(number())'''
    #4. Parameter and Return
'''def multiply(a, b):
    return a * b

print(multiply(4,5))'''


# ++++++++++++EXAMPLE++++++++++++
# {Suppose you calculate the average of marks many times.}

# Without function
'''marks = [80, 90, 75]

print(sum(marks)/len(marks))'''

#With Function 
'''def average(data):
    return sum(data)/len(data)

marks = [80, 90, 75]
print(average(marks))'''




# Interview Questions
'''Q1. What is a function?

A reusable block of code that performs a specific task.

Q2. Difference between parameter and argument?
Parameter: Variable in the function definition.
Argument: Actual value passed to the function.

Example:

def greet(name):   # name → parameter
    print(name)

greet("Ankit")     # "Ankit" → argument'''

# Q3. Difference between print() and return?
# | `print()`           | `return`                    |
# | ------------------- | --------------------------- |
# | Displays output     | Sends value back            |
# | Doesn't store value | Can be stored in a variable |
# | Ends with display   | Ends the function execution |


# 1. Write a function that prints "Hello, Python!".
'''def greet():
    print("Hello, Python!")
greet()'''

# 2. Write a function that accepts a name as a parameter and prints:
#    Hello, <name>
'''def greet(name):
    print("Hello", name)
greet("Ankit")'''

# 3. Write a function to add two numbers.
'''def add(a,b):
    print(a + b)

add(6,5)'''
# OR
'''def add(a, b):
    return a + b
result = add(6, 5)
print(result)'''

# 4. Write a function to find the square of a number.
'''def Seq(num):
    print(num * num)
Seq(5)'''

# 5. Write a function to calculate the area of a rectangle.
'''def Area(length,width):
    print(length * width)
Area( 5, 9)'''

# 6. Write a function to check whether a number is even or odd.
'''def cheak(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
cheak(5)'''


# 7. Write a function to find the largest of three numbers.
'''def largest(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

largest(10, 25, 15)'''


# 8. Write a function that returns the factorial of a number.

# 9. Write a function to count the number of vowels in a string.

# 10. Write a function to calculate the average of a list of numbers.

# 11. Write a function to check whether a string is a palindrome.

# 12. Write a function to reverse a string.

# 13. Write a function to count the frequency of each character in a string.

# 14. Write a function to remove duplicate elements from a list.

# 15. Write a function to find the second largest number in a list.

# 16. Write a function to count how many times a specific word appears in a sentence.

# 17. Write a function that returns all even numbers from a list.

# 18. Write a function to find the maximum value in a list without using max().

# 19. Write a function to calculate the sum of all numbers in a list without using sum().

# 20. Write a function that accepts a list of marks and returns:
#     - Total Marks
#     - Average Marks
#     - Highest Marks
#     - Lowest Marks



