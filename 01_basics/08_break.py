# Break Statement in Python

'''The break statement is used to immediately terminate (stop) a loop (for or while), even if the loop's condition is still True.

Once break is executed:

The loop ends immediately.
Control moves to the first statement after the loop.
Syntax
while condition:
    if condition_to_stop:
        break

or

for item in iterable:
    if condition_to_stop:
        break'''



# ===========================
# BREAK STATEMENT PRACTICE QUESTIONS
# (20 Questions | Easy → Advanced)
# ===========================

# 🟢 Level 1 – Basics

# 1. Print numbers from 1 to 10, but stop the loop when the number becomes 6.
'''for i in range(1,10):
    print(i)
    if i == 6:
        break'''
    

# 2. Print numbers from 20 to 1, but stop when the number becomes 12.
'''i = 20
while i >= 1:
    print (i)
    if i == 12:
        break
    i -= 1'''

# 3. Print numbers from 1 to 100, but stop after printing the first number divisible by 17.
'''i = 1
while i <= 100:
    print(i)
   
    if i % 17 == 0:
        break
    i += 1'''

# 4. Print all even numbers starting from 2, but stop when you reach 20.

'''i = 2
while i <= 50:
    print(i)
    if i == 20:
        break
    i += 2'''
        
        
# 5. Print the multiplication table of 7, but stop after the 5th multiple.
'''i = 1
while i <= 10:
    print(f"7 x {i} = {7 * i}")
    if i == 5:
        break
    i += 1'''

# ===========================
# 🟡 Level 2 – User Input
# ===========================

# 6. Keep asking the user to enter a word until they type "exit".
'''word = ""

while word != "exit":
    word = input("Enter a word: ")

    if word == "exit":
        break

    print("You entered:", word)

print("Program Ended!")'''

#M2
'''while True:
    sentence = input("Enter a sentence: ")

    if "exit" in sentence:
        print("Program Ended!")
        break'''

# 7. Keep asking the user for numbers and stop when they enter 0.

'''while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break
print("Program Ended.!")'''

# 8. Create a password checker. Keep asking for the password until the correct password is entered, then stop the loop.
'''correct_password = 987458
while True: 
    password = int(input("Enter a  six digit Password:"))
    if password == correct_password:
        print("The Password is correct!")
        break
    else:
        print("Incorrect Password. Try Again!")'''



# 9. Keep asking the user to enter positive numbers. Stop when they enter a negative number.
'''while True:
    num = int(input("Enter a positive number: "))

    if num < 0:
        print("Negative number entered. Program End!")
        break
    else:
        print("You entered:", num)'''

# 10. Ask the user to guess a secret number. Stop the loop when they guess correctly.
'''secret_num = 1122

while True:
    num = int(input("Enter a secret number:"))
    if num == secret_num:
        print("The Secret number is Correct!")
        break
    else:
        print("The Secret number is Incorrect!")'''

# ===========================
# 🟠 Level 3 – Searching
# ===========================

# 11. Find the first occurrence of 50 in the list.
# numbers = [12, 25, 37, 50, 60, 70]
# Print its index and stop searching.
'''numbers = [10, 20, 30, 50, 60, 50, 70]
for i in range(len(numbers)):
    if numbers[i] == 50:
        print("First occurrence of 50 is at index:",i)
        break'''

# 12. Find the first negative number in the list.
'''data = [15, 22, 30, -8, 12, -5]
# Stop after finding it.
for i in range(len(data)):
    if data[i] < 0:
        print("The First negative number is at index:",i)
        break'''


# 13. Find the first employee whose salary is greater than 50000.
# salary = [25000, 30000, 42000, 55000, 60000]
'''salary = [25000, 30000, 42000, 55000, 60000]

for i in range(len(salary)):
    if salary[i] > 50000:
        print("Index:", i)
        print("Salary:", salary[i])
        break'''

# 14. Find the first missing value (None) in the list.

'''data = [10, 20, None, 40, None]
for i in range(len(data)):
    if data[i] is None:
        print("The first missing value is at index:",i)
        break'''


# 15. Search for a given name in the list. If found, print "Found" and stop searching.

'''names = ["Ankit", "Rahul", "Priya", "Neha"]
name =input("Enter a Name:")

for i in range(len(names)):
    if names[i] ==  name:
        print("Found")
        print("Stop searching!")
        break'''


# ===========================
# 🔴 Level 4 – Data Analytics Style
# ===========================

# 16. Given daily sales:
'''sales = [1200, 1500, 1800, -1, 2200, 2500]
# Process the sales until -1 appears, then stop.

for i in range(len(sales)):
    
    if sales[i] == -1:
        break
    else:
        print(sales[i])'''


# 17. Read numbers from the user and keep calculating the sum. Stop when the user enters 999.

'''total = 0 
while True:
    num = int(input("Enter a number:"))
    if num == 999:
        break
    else:
        total += num
print("The sum is:",sum)'''

# 18. Given a list of temperatures:
temp = [28, 31, 34, 41, 39, 37]

# Stop processing as soon as the temperature exceeds 40°C.
'''for i in range(len(temp)):
    if temp[i] > 40:
        break
    # else:
    print(temp[i])'''


# 19. Given transaction amounts:

transactions = [500, 1200, 800, 10000, 700]

# Stop checking transactions when you find one greater than 5000 and print "Suspicious Transaction Found".
'''for i in range(len(transactions)):
    if transactions[i] > 5000:
        print("Suspicios Transaction Froud")
        break

    print(transactions[i])'''


# 20. Interview Challenge

numbers = [12, 25, 30, 45, 60, 75]
# Find the first number divisible by both 3 and 5, print it, and stop the loop immediately.
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        print("The number is:",numbers[i])
        print("Index:",i)
        break


'''for i in range(0,21):
    print(i)
    if i==11:
        break
   

print("\n")
for i in range(0,21):
    print(i)
    if i==18: 
        break

print("\n")

for i in range(1,11):
    print(i)
    if i==5:
        break'''