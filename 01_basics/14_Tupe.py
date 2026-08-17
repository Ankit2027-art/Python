# TUPLE IN PYTHON

# 1. Definition:
# A tuple is an ordered and immutable collection of elements in Python.

# 2. Syntax:
# tuple_name = (element1, element2, element3)

# Example:
# t = (10, 20, 30, 40)

# 3. Ordered:
# Tuples maintain the order of elements.
# Each element has an index starting from 0.

# Example:
# t = (10, 20, 30)
# t[0] → 10

# 4. Immutable:
# Once a tuple is created, its elements cannot be changed, added, or removed.

# Example:
# t = (10, 20, 30)
# t[0] = 50       # Error

# 5. Allows Duplicates:
# Tuples can contain duplicate values.

# Example:
# t = (10, 20, 10, 30)

# 6. Allows Different Data Types:
# A tuple can contain different types of values.

# Example:
# t = (10, "Python", 3.14, True)

# 7. Single Element Tuple:
# A comma is required for a single-element tuple.

# Example:
# t = (10,)

# Without comma:
# t = (10)        # This is an integer, not a tuple

# 8. Tuple Methods:
# Tuples mainly have two methods:

# count()  → Counts occurrences of an element.
# index()  → Returns the index of an element.

# Example:
# t = (10, 20, 10, 30)

# t.count(10)     → 2
# t.index(20)     → 1

# 9. Tuple Operations:
# Tuples support:
# - Indexing
# - Slicing
# - Concatenation (+)
# - Repetition (*)
# - Membership (in / not in)

# 10. Why use Tuple?
# - Data should not be modified.
# - Safer than mutable collections.
# - Can be used as dictionary keys if all elements are hashable.
# - Generally more memory-efficient than lists.

# Example:
# coordinates = (28.61, 77.20)
# =====================================
# PYTHON TUPLE PRACTICE QUESTIONS
# Beginner → Advanced → IPL Level
# =====================================

# --------------- Beginner (1–10) ---------------

# 1. Create a tuple containing the names of five IPL teams.

'''tup = ("RCB", "MI", "CSK", "KKR", "GT")
print(tup)'''

# 2. Print the first and last element of a tuple.
tup = ("RCB", "MI", "CSK", "KKR", "GT")
'''print("First Elemnt",tup[0])
print("Last Elemnt",tup[-1])'''

# 3. Print the third element of a tuple.

# 4. Find the length of a tuple without using the len() function.
'''count  = 0
for i in tup:
    count +=1
print(count)'''


# 5. Count how many times a given element appears in a tuple.
tup = (10, 20, 30, 20, 40, 20, 50)
'''num = int(input("Enter a NUmber:"))
print(tup.count(num))'''



''''num = int(input("Enter a NUmber:"))
count = 0
for i in tup:
    if i == num:
        count += 1
print(count)'''

# 6. Find the index of a given element in a tuple.
'''tup = (10,20,30,82,65,41,20)
num = int(input("Enter a Number:"))
print("Index:",tup.index(num))'''

# 7. Check whether a given element exists in a tuple.
tup = (10,20,30,82,65,41,20)
'''num = int(input("Enter a Number:"))
count = 0
for i in tup:
    if i == num:
        count += 1
if count>0:
    print("Exist")
else:
    print("Not Exists")'''



'''if tup.count(num)>0:
    print("Exist")
else:
    print("Not Exist")'''

# 8. Convert a tuple into a list.
'''list =list(tup)
print(list)'''

# 9. Convert a list into a tuple.


# 10. Iterate through a tuple and print each element.
f'''or i in tup:
    print(i)'''

# ------------- Intermediate (11–20) -------------

# 11. Find the largest element in a tuple.
tup = (10,20,30,82,65,41,20)
'''print(max(tup))'''

# 12. Find the smallest element in a tuple.
'''print(min(tup))'''

# 13. Find the sum of all elements in a tuple.
'''sum = 0
for num in tup:
    sum += num
print("Total",sum)'''

# 14. Find the average of all numeric elements in a tuple.

'''total = 0
for num in tup:
    total += num

avg = total / len(tup)
print("Average:",avg)'''

# 15. Count the even numbers in a tuple.
t = (5,2,4,7,8,9,4,3,5,4,2)

'''count = 0
for i in t:
    if i % 2 == 0:
        count += 1
print("Total Even num:",count)'''

# 16. Count the odd numbers in a tuple.

# 17. Return only the prime numbers from a tuple.
t = (2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 29)
'''for num in t:

    if num > 1:
        prime = True

        for i in range(2 , num):
            if num % i == 0:

               prime = False
        if prime:
            print(num)'''

#OR
'''for num in tup:
    count= 0
    if num > 1:
        for i in range(1, num +1):
            if num % i == 0:
                count += 1

    if count == 2:
        print(num)'''

 

# 18. Reverse a tuple without using slicing ([::-1]).

rev = tuple(reversed(t))
# 19. Find the second largest element in a tuple.
'''tt = (5,2,4,7,8,9,4,3,5,4,2)
largest = tt[0]
sec_largest = tt[0]
for num in tt:
    if num > largest:
        sec_largest =largest
        largest = num
    elif num > sec_largest and num != largest:
        sec_largest = num

print(sec_largest)'''

    
# 20. Merge two tuples without using the + operator.
'''t1 = (1,2,3,4)
t2 = (5,6,7,8)
new_tuple = ()
for num in t1:
    new_tuple += (num,)
for nu in t2:
    new_tuple += (nu,)
print(new_tuple)'''

# --------------- Advanced (21–25) ---------------

# 21. Remove duplicate elements from a tuple.
'''tt = (5,2,4,7,8,9,4,3,5,4,2)
new_tup = ()
for num in tt:
    if num not in new_tup:
        new_tup += (num,)
print(new_tup)'''

# 22. Find the frequency of every element in a tuple.
'''tt = (5,2,4,7,8,9,4,3,5,4,2)
frq = {}
for num in tt:
    if num in frq:
        frq[num] += 1
    else:
        frq[num] = 1

print(frq)'''

# 23. Check whether two tuples are equal.
'''t1 = (1,2,3,4)
t2 = (5,6,7,8)
if t1 == t2:
    print("Equal")
else:
    print("NotEqual")'''

# 24. Find all duplicate elements in a tuple.

'''tupp = (5,2,4,7,8,9,4,3,5,4,2)

printed = ()
for i in tupp:
    if tupp.count(i) > 1 and i not in printed:
        print(i)
        printed += (i,)'''

# 25. Sort a tuple in ascending order without using sorted().
''''tt = (5,2,4,7,8,9,4,3,5,4,2)
lst = list(tt)

for i in range(len(tt)):
    for j in range(i +1,len(tt)):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]

tup =tuple((lst))

print(tup)'''


# ----------- IPL Data Analytics (26–30) ----------

# 26. Given a tuple of player runs, find the Orange Cap winner.

# Example:
'''players = ("Virat", "Rohit", "Gill", "Dhoni", "KL Rahul")
runs = (930, 417, 890, 161, 573)
highest = max(runs)
index = runs.index(highest)

print("Orange Cap Winner:", players[index])
print("Runs:", highest)'''

# 27. Given two tuples:
# (players)
players = ("Virat", "Rohit", "Gill", "Dhoni", "KL Rahul")
runs = (930, 417, 890, 161, 573)

# Create a dictionary where player names are keys and runs are values.


# 28. Given a tuple of IPL teams:
teams = ("CSK", "MI", "RCB", "CSK", "GT", "MI", "CSK")

# Count how many times each team appears.
'''frq ={}
for team in teams:
    if team in frq:
        frq[team] += 1
    else:
        frq[team] = 1
print(frq) '''

# 29. Given a tuple containing match results:

# (
# ("CSK", "MI"),
# ("RCB", "GT"),
# ("CSK", "RCB"),
# ("MI", "GT")
# )
matches = (
    ("CSK", "MI"),
    ("RCB", "GT"),
    ("CSK", "RCB"),
    ("MI", "GT")
)

# Count how many matches each team played.
'''count ={}
for match in matches:
    for team in match:
        if team in count:
            count[team] += 1
        else:
            count[team] = 1

print(count)'''


# 30. Mini IPL Tuple Project

# Given:
players = ("Virat", "Gill", "Dhoni", "Rohit", "KL Rahul")
runs = (741, 890, 161, 417, 520)

# Perform the following:
# • Find the Orange Cap winner.
'''higest = max(runs)
winner = runs.index(higest)
print(winner)
print("Orange cap winner:",players[winner])
print("Runs:",higest)'''

# • Find the player with the lowest runs.
'''lowest = min(runs)
player = runs.index(lowest)
print("Lowest runs:",players[player])
print("Runs",lowest)'''

# • Calculate the average runs.
'''average = sum(runs) / len(runs)
print(average)'''

# • Find players with more than 500 runs.
'''for i in range(len(runs)):
    if runs[i] > 500:
        print(players[i],":",runs[i])'''