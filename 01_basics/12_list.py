# ==========================
# PYTHON LISTS - QUICK REVISION
# ==========================

# 1. What is a List?
# ------------------
# • Ordered collection of items.
# • Mutable (can be changed).
# • Allows duplicate values.
# • Can store different data types.

# Example:
# a = [10, 20, 30]
# b = ["Python", 100, True, 3.5]

# --------------------------------------------------

# 2. Creating Lists
# -----------------
# a = []
# a = list()
# a = [1, 2, 3]
# a = ["Apple", "Banana"]
# a = [[1,2],[3,4]]

# --------------------------------------------------

# 3. Indexing
# -----------
# Positive:
# a[0]
# a[1]

# Negative:
# a[-1]
# a[-2]

# --------------------------------------------------

# 4. Slicing
# ----------
# a[start:end:step]

# a[1:4]
# a[:3]
# a[2:]
# a[::-1]

# --------------------------------------------------

# 5. Updating List
# ----------------
# a[1] = 100

# --------------------------------------------------

# 6. Adding Elements
# ------------------

# append()
# Adds one element.

# a.append(10)

# insert()
# Adds element at a specific index.

# a.insert(1,50)

# extend()
# Adds multiple elements.

# a.extend([4,5,6])

# Difference

# append([4,5])
# → [1,2,3,[4,5]]

# extend([4,5])
# → [1,2,3,4,5]

# --------------------------------------------------

# 7. Removing Elements
# --------------------

# remove(value)
# a.remove(10)

# pop()
# a.pop()

# pop(index)
# a.pop(2)

# del
# del a[1]

# clear()
# a.clear()

# --------------------------------------------------

# 8. Built-in Functions
# ---------------------

# len(a)
# sum(a)
# max(a)
# min(a)
# sorted(a)
# list(reversed(a))

# --------------------------------------------------

# 9. List Methods
# ---------------

# append()
# insert()
# extend()
# remove()
# pop()
# clear()
# index()
# count()
# sort()
# reverse()
# copy()

# --------------------------------------------------

# 10. Sorting
# -----------

# Ascending
# a.sort()

# Descending
# a.sort(reverse=True)

# New Sorted List
# sorted(a)

# --------------------------------------------------

# 11. Reverse
# -----------

# a.reverse()

# a[::-1]

# --------------------------------------------------

# 12. Membership Operators
# ------------------------

# 10 in a

# 20 not in a

# --------------------------------------------------

# 13. Operators
# -------------

# Concatenation
# a+b

# Repetition
# a*3

# --------------------------------------------------

# 14. Loop Through List
# ---------------------

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# --------------------------------------------------

# 15. List Comprehension
# ----------------------

# [x for x in range(10)]

# [x*x for x in range(5)]

# [x for x in range(20) if x%2==0]

# --------------------------------------------------

# 16. Nested List
# ---------------

# matrix=[[1,2],[3,4]]

# matrix[1][0]

# --------------------------------------------------

# 17. Copy List
# -------------

# b=a.copy()

# b=a[:]

# --------------------------------------------------

# 18. Common Errors
# -----------------

# IndexError
# a[100]

# ValueError
# a.remove(100)

# TypeError
# sum(["A","B"])

# --------------------------------------------------

# 19. Important Differences
# -------------------------

# append() vs extend()

# append()
# • One element
# • Can add list as single element

# extend()
# • Multiple elements
# • Adds each item separately

# -------------------------

# sort() vs sorted()

# sort()
# • Changes original list

# sorted()
# • Returns new sorted list

# -------------------------

# remove() vs pop() vs del

# remove()
# • Removes by value

# pop()
# • Removes by index
# • Returns removed item

# del
# • Deletes by index or slice

# --------------------------------------------------

# 20. Time Complexity
# -------------------

# Indexing      O(1)
# Append        O(1)
# Insert        O(n)
# Remove        O(n)
# Search        O(n)
# Sort          O(n log n)

# --------------------------------------------------

# 21. Interview Questions
# -----------------------

# ✓ What is a list?
# ✓ Why is a list mutable?
# ✓ Difference between list and tuple?
# ✓ append() vs extend()
# ✓ sort() vs sorted()
# ✓ remove() vs pop() vs del
# ✓ What is list comprehension?
# ✓ How to reverse a list?
# ✓ How to remove duplicates?
# ✓ How to find second largest element?
# ✓ How to merge two lists?
# ✓ How to flatten a nested list?

# --------------------------------------------------


# ==========================
# TOP 20 PYTHON LIST QUESTIONS
# (Data Analytics Level)
# ==========================
list = [ 10,50,70,80,90,10,20,25]


# 1. Write a program to find the largest element in a list without using max().
'''largest = list[0] 
for i in list:
    if i > largest:
        largest = i
print(largest)'''

# 2. Write a program to find the smallest element in a list without using min().

'''smallest = list[0] 
for i in list:
    if i < smallest:
        smallest = i
print(smallest)'''

# 3. Write a function to calculate the sum of all elements in a list without using sum().
'''sum = 0
for ele in list:
    sum += ele
print(sum)'''

# 4. Write a function to calculate the average of all numbers in a list.
total = 0
'''for ele in list:
    total +=ele
Average = total / len(list)
print(Average)'''


# 5. Write a program to count how many even and odd numbers are present in a list.

# 6. Write a function to remove duplicate elements from a list while keeping the original order.
'''new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)'''
    


# 7. Write a program to find the second largest element in a list.
'''largest = list[0]
sec_largest = list[0]
for num in list:
    if num > largest:
        sec_largest = largest
        largest = num
    elif num > sec_largest and num != largest:
        sec_largest = num

print(sec_largest)'''


# 8. Write a function to reverse a list without using reverse() or slicing ([::-1]).
'''list = [10,50,70,80,90,10,20,25]
new_list = []
for i in range(len(list) -1,-1,-1):
    new_list.append(list[i])

print(new_list)'''


# 9. Write a function to check whether a given element exists in a list without using the in operator.

'''def cheak_element(list, element):
    count = 0
    for num in list:
        if element == num :
            count += 1
    if count > 0:
            print("The Element Exists")
    else:
        print("The Element Not Exists")


list = [10,50,70,80,90,10,20,25]
element = int(input("Eneter a Number:"))

cheak_element(list, element)'''

# 10. Write a function to count the frequency of each element in a list.
'''def Frequency(list):
    frq = {}
    for num in list:
        if num in frq:
            frq[num] += 1
        else:
            frq[num] = 1
    print(frq)
    
list = [10,50,70,80,90,10,20,25]
Frequency(list)'''


# 11. Write a function to merge two lists and remove duplicate values.
'''def Merge(list1,list2):
    new_list= []
    for num in list1 + list2:
        if num not in new_list:
            new_list.append(num)
        
    print(new_list)

list1 = [10,20,30,40,50]
list2 = [40,50,60,70,80]
Merge(list1,list2)'''

# 12. Write a program to separate positive and negative numbers into two different lists.
'''def Seprate(numbers):
    Postive_num = []
    Negative_num = []
    for num in numbers:
        if num >= 0:
            Postive_num.append(num)
        else:
            Negative_num.append(num)
    print("Postive Numbers",Postive_num)
    print("Negative Numbers",Negative_num)

numbers = [10, -5, 20, -15, 0, 30, -8, 45, -25, 60, -1, 75]
Seprate(numbers)'''


# 13. Write a function to find all prime numbers present in a list.
# def Prime_num(numbers):
#     prime = []

#     for num in numbers:

#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime  =  False
#             break
            
#     prime.a(num)    

# numbers = [2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 29]
# Prime_num(numbers)



# 14. Write a function to return only the even numbers from a list.
'''def Even_num(numbers):
    Even_num = []
    for num in numbers:
        if num % 2 == 0:
            Even_num.append(num)
    print(Even_num) 


numbers = [2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 29]  
Even_num(numbers) '''

# 15. Write a function to sort a list in ascending order without using sort() or sorted().

def sort_list(numbers):

    for i in range(len(numbers)):
        for j in range(i +1,len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i],numbers[j] = numbers[j],numbers[i]

    return numbers

numbers = [10,50,70,80,90,10,20,25]
print(sort_list(numbers))



# 16. Write a function to find the common elements between two lists.

# 17. Write a function to find the missing number from a list containing numbers from 1 to n.

# 18. Given a list of students' marks, return:
#     - Total Marks
#     - Average Marks
#     - Highest Marks
#     - Lowest Marks
#     - Number of students who scored above the average

# 19. Given a list of employee salaries, calculate:
#     - Highest Salary
#     - Lowest Salary
#     - Average Salary
#     - Total Salary Expense
#     - Number of employees earning more than ₹50,000

# 20. Given a sales list:
#     [1200, 1500, 900, 1800, 2000, 1100, 1700]

#     Write functions to:
#     - Calculate Total Sales
#     - Calculate Average Sales
#     - Find Highest Sale
#     - Find Lowest Sale
#     - Count sales greater than ₹1500
#     - Return all sales between ₹1000 and ₹1800
