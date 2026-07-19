# What is continue?

'''The continue statement is used to skip the current iteration of a loop and move directly to the next iteration.'''

'''Unlike break, it does not stop the loop. It only skips the remaining code for the current iteration.'''

#  Start
#    │
#    ▼
# Check Condition
#    │
#    ▼
# Execute Loop
#    │
#    ▼
# continue?
#  ┌──────────┴──────────┐
#  │                     │
# Yes                   No
#  │                     │
#  ▼                     ▼
# Skip Remaining     Execute Remaining
# Statements         Statements
#  │
#  ▼
# Next Iteration   
#         

'''for i in range(1,20):
    if i==10:
        continue #continue the loop for the next iteration here itself
    print(i)
if i==12:
    pass
print("End of program")
print("\n")


for i in range(1,11):
    if i==5:
        continue
    print(i)

print("\n")

for i in range(1,21):
    if i% 2 == 0:
        continue
    print(i)'''

# =========================================
# CONTINUE STATEMENT PRACTICE QUESTIONS
# (15 Questions | Easy → Advanced)
# =========================================

# 🟢 Level 1 – Basics

# 1. Print numbers from 1 to 10, but skip the number 5 using continue.
'''i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1'''

# 2. Print numbers from 1 to 20, but skip all even numbers.
'''i = 1
while i <=20:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1'''

# 3. Print numbers from 1 to 20, but skip all numbers divisible by 3.
'''i = 1
while i <=20:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1'''

# 4. Print the multiplication table of 7, but skip the 5th multiple.
'''num = 7
i = 1
while i <=10:
    if i == 5:
        i += 1
        continue
    print(num,"X",i,"=",num * i)
    i += 1'''

# 5. Print numbers from 1 to 30 except 10, 15, and 20.
'''i = 1
while i <= 30:
    if i in (10,15,20):
        i += 1
        continue
    print(i)
    i += 1'''

# =========================================
# 🟡 Level 2 – User Input
# =========================================

# 6. Keep asking the user to enter 10 numbers. Skip negative numbers and print only positive numbers.

'''count = 1
while count <= 10:
    num = int(input("Enter a numbers:"))
    if num < 0:
        count += 1
        continue
    print("Postive Number:",num)
    count += 1'''

# 7. Ask the user to enter 10 marks. Skip invalid marks (less than 0 or greater than 100).
'''marks = []
count = 1
while count <= 10:
    num = int(input("Enter a marks:"))
    if num < 0 or num >- 100:
        count += 1
        continue
    marks.append(num)
    count += 1
print("Marks:",marks)'''

# 8. Read numbers until the user enters 0. Skip negative numbers while calculating the sum.
'''sum = 0

while True:
    num = int(input("Enter a number:"))
    if num == 0:
        break
    elif num < 0:
        continue
    sum += num
print("Total:",sum)'''

# 9. Keep asking the user for names. Skip blank inputs ("").
'''names = [ ]
while len(names) < 5:
    name = input("Enter name:")
    if name == "":
        continue
    names.append(name)
print("Names:",names)'''


# =========================================
# 🟠 Level 3 – Lists
# =========================================

# 10. Given:
'''numbers = [10, -5, 20, -8, 15, 30]
# Print only positive numbers.
i = 0
while  i < len(numbers):

    if numbers[i] < 0:
        i += 1
        continue

    print(numbers[i])  
    i += 1'''


# 11. Given:
'''data = [10, None, 20, None, 40, 50]
# Skip None values and print only valid data.
i = 0
while  i < len(data):

    if data[i] == None:
        i += 1
        continue

    print(data[i])  
    i += 1'''

# 12. Given:
'''sales = [1200, -1, 1500, 1800, -1, 2200]
# Skip invalid sales (-1) and calculate the total sales.
total = 0

i = 0
while  i < len(sales):

    if sales[i] < 0:
        i += 1
        continue
    total += sales[i]
    i += 1
print("Total:",total)'''


# =========================================
# 🔴 Level 4 – Interview / Data Analytics
# =========================================

# 13. Given employee salaries:
'''salary = [25000, 0, 35000, 42000, 0, 50000]

# Skip salaries equal to 0 and calculate the average salary.
total = 0
count = 0

i = 0 
while  i < len(salary):

    if salary[i] == 0:
        i += 1
        continue

    total += salary[i]
    count += 1
    i += 1

average = total / count
print("Average:",average)'''

# 14. Given customer ratings:
'''ratings = [5, 4, None, 3, None, 5, 2]

# Skip missing ratings and calculate the average rating.
total = 0
count = 0

i = 0 
while  i < len(ratings):

    if ratings[i] is None:
        i += 1
        continue

    total += ratings[i]
    count += 1
    i += 1

average = total / count
print("Average:",average)'''



# 15. Interview Challenge
'''numbers = [12, 15, -5, 0, 30, 45, -10, 60]

# Using only a while loop and continue:
# • Skip negative numbers.
# • Skip zeros.
# • Print only numbers divisible by 3.
# • Calculate their sum.
# • Count how many valid numbers were processed.
# • Calculate the average.
div = []
total = 0
count = 0

i = 0
while i < len(numbers):
    if numbers[i] <= 0:
        i += 1
        continue

    if numbers[i] % 3 != 0:
        i += 1
        continue

    div.append(numbers[i])
    total += numbers[i]
    count += 1

    i += 1
average = total / count

print("The numbers are div by 3 is:",div)
print(" the total valid numbers was processed is: ",count)
print("Total sum:",total)
print("Average",average)'''
