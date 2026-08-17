# DICTIONARY IN PYTHON

# 1. Definition:
# A dictionary is a mutable collection that stores data in key-value pairs.

# 2. Syntax:
# dictionary_name = {
#     key1: value1,
#     key2: value2
# }

# Example:
# student = {
#     "name": "Ankit",
#     "age": 19,
#     "course": "BCA"
# }

# 3. Key-Value Pair:
# Each item consists of:
# Key → used to identify/access the data.
# Value → actual data associated with the key.

# Example:
# "name" → Key
# "Ankit" → Value

# 4. Keys:
# - Keys must be unique.
# - Keys must be hashable.
# - Common key types: string, integer, tuple.

# Example:
# d = {
#     "name": "Ankit",
#     "age": 19
# }

# 5. Values:
# Values can be of any data type.

# Example:
# d = {
#     "name": "Ankit",
#     "marks": 85,
#     "skills": ["Python", "SQL"]
# }

# 6. Mutable:
# Dictionary contents can be changed after creation.

# Example:
# d = {"name": "Ankit"}

# d["name"] = "Rahul"

# 7. Accessing Values:

# d = {"name": "Ankit", "age": 19}

# d["name"]       → "Ankit"
# d["age"]        → 19

# 8. Adding a New Item:

# d["city"] = "Lucknow"

# 9. Updating an Item:

# d["age"] = 20

# 10. Deleting an Item:

# del d["age"]

# 11. Important Dictionary Methods:

# keys()      → Returns all keys.
# values()    → Returns all values.
# items()     → Returns key-value pairs.
# get()       → Safely accesses a value.
# update()    → Adds or updates multiple items.
# pop()       → Removes an item using its key.
# popitem()   → Removes the last inserted item.
# clear()     → Removes all items.

# 12. Example:

# student = {
#     "name": "Ankit",
#     "age": 19,
#     "course": "BCA"
# }

# student.keys()
# student.values()
# student.items()

# 13. Checking a Key:

# "name" in student       → True
# "city" in student       → False

# 14. Looping Through Dictionary:

# for key, value in student.items():
#     print(key, value)

# 15. Nested Dictionary:
# A dictionary can contain another dictionary.

# Example:

# students = {
#     "student1": {
#         "name": "Ankit",
#         "age": 19
#     }
# }

# 16. Why use Dictionary?
# - Fast access using keys.
# - Useful for structured data.
# - Used frequently in APIs, JSON, databases and data analysis.


# --------------- Beginner (1–15) ---------------

# 1. Create a dictionary of 5 students and their marks.
students = {
    "Ankit": 85,
    "Rahul": 92,
    "Aman": 78,
    "Priya": 88,
    "Neha": 95
}

'''print(students)'''

# 2. Print all keys of a dictionary.
'''print(students.keys())'''


# 3. Print all values of a dictionary.
'''print(students.values())'''

# 4. Print all key-value pairs.

# 5. Access the value of a given key.
'''name = input("enter a Name:")
print(students[name])'''

# 6. Check whether a given key exists.
'''name = input("Enter a name:")

count = 0
for key in students:
    if name ==  key:
        count += 1
if count > 0:
    print("Exist")
else:
    print("Not Exist")'''


# 7. Check whether a given value exists.
'''num = int(input("Enter a number:"))
count = 0
for value in students.values():
    if value == num:
        count += 1
if count > 0:
    print("Exist")
else:
    print("Not Exist")'''

#or
'''num = int(input("Enter a number: "))

if num in students.values():
    print("Exist")
else:
    print("Not Exist")'''

# 8. Add a new key-value pair.
'''students.update({"Yash":99})
print(students)'''

# 9. Update the value of an existing key.
'''students.update({"Ankit":100})
print(students)'''

# 10. Delete a key from a dictionary.
'''del students["Neha"]
print(students)'''

# 11. Find the length of a dictionary without using len().
'''lengths = 0
for key in students:
    lengths+=1
print(lengths)'''

# 12. Iterate through all keys.
'''for key in students:
    print(key)'''


# 13. Iterate through all values.
'''for value in students.values():
    print(value)'''

# 14. Iterate through all key-value pairs.
'''for k,v in students.items():
    print(k,v)'''

# 15. Copy one dictionary into another.
'''new_dic = students.copy()
print(new_dic)'''

# ------------- Intermediate (16–30) -------------

# 16. Count the frequency of each element in a list.
'''numbers = [10, 20, 10, 30, 20, 10]
dic = {}
for num in numbers:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
print(dic)'''

# 17. Count the frequency of each character in a string.

'''text = "banana"
frq = {}
for i in text:
    if i in frq:
        frq[i] += 1
    else:
        frq[i] =1
print(frq)'''
    

# 18. Count the frequency of each word in a sentence.
'''text = sentence = "apple banana apple mango banana apple"

word = text.split()
frq = {}
for i in word:
    if i in frq:
        frq[i] += 1
    else:
        frq[i] =1
print(frq)'''

# 19. Find the key having the maximum value.
'''maximum = max(students.values())

for key , value in students.items():
    if value == maximum:
        print(key)'''


# 20. Find the key having the minimum value.
'''min = min(students.values())

for key , value in students.items():
    if value == min:
        print(key)'''


# 21. Calculate the sum of all dictionary values.
'''sum = 0
for value in students.values():
    sum += value
print("Total",sum)'''

# 22. Calculate the average of all dictionary values.
'''avg = sum / len(students.keys())
print(avg)'''

# 23. Merge two dictionaries without using update().
'''dict1 = {
    "Ankit": 85,
    "Rahul": 92,
    "Aman": 78
}

dict2 = {
    "Priya": 88,
    "Neha": 95,
    "Rohan": 81
}
new_dic = {}
for key ,value in dict1.items():
    new_dic[key] = value

for key , value in dict2.items():
    new_dic[key] = value
print(new_dic)'''

# 24. Create a dictionary from two lists (keys and values).
'''keys = ["Virat", "Gill", "Rohit", "Dhoni", "KL Rahul"]

values = [741, 890, 417, 161, 520]
dict = {}
for i in range(len(keys)):
    dict[keys[i]] = values[i]
print(dict)'''


# 25. Swap keys and values (invert dictionary).
'''dict2 = {
    "Priya": 88,
    "Neha": 95,
    "Rohan": 81
}
new ={}
for key,value in dict2.items():
    new[value] =key
print(new)'''

# 26. Remove duplicate values from a dictionary.
'''dict = {
    "Priya": 88,
    "Neha": 95,
    "Rohan": 81,
    "Amit" : 88
}
new ={}
seen =  []
for key,value in dict.items():
    if value not in seen:
        new[key] = value
        seen.append(value)
    
print(new)'''

# 27. Sort a dictionary by keys without using sorted().
'''dict = {
    "Priya": 88,
    "Neha": 11,
    "Rohan": 81,
    "Amit" : 20
}
list = []
for value in dict.keys():
    list.append(value)

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]

print(list)
new  ={}

for key in list:
    new[key] = dict[key]
print(new)'''
    


# 28. Sort a dictionary by values without using sorted().
'''stu = {
    "Priya": 88,
    "Neha": 11,
    "Rohan": 81,
    "Amit" : 20
}
list = []
for value in stu.values():

    list.append(value)

for i in range (len(list)):
    for j in range(i+1,len(list)):
        if list[i] >list [j]:
            list[i],list[j]=list[j],list[i]

new = {}
for value in list:
    for key,val in stu.items():
        if val == value:
            new[key] = val
print(new)'''

# 29. Find the second highest value in a dictionary.
'''stu = {
    "Priya": 60,
    "Neha": 90,
    "Rohan": 81,
    "Amit" : 20
}
list = []
for value in stu.values():

    list.append(value)

largest = list[0]
sec_largest = list[0]
for num in list:
    if num > largest:
        sec_largest = largest
        largest = num
    elif num > sec_largest and num != largest:
        sec_largest = num


print(sec_largest)

new ={}

for key,val in stu.items():
    if val == sec_largest:
        new[key] = val
print(new)



# print(new)'''

# 30. Return only the even values from a dictionary.
'''stud = {
    "Priya": 60,
    "Neha": 90,
    "Rohan": 81,
    "Amit" : 20
}
list = []
for num in stud.values():
    if num % 2 == 0:
        list.append(num)

new = {}
for value in list:
    for key,val in stud.items():
        if val == value:
            new[key] = val
print(new)''' 

    


# --------------- Advanced (31–40) ---------------

# 31. Return only the odd values from a dictionary.
'''stu = {
    "Priya": 60,
    "Neha": 90,
    "Rohan": 81,
    "Amit" : 20
}
list = []
for value in stu.values():
    if value % 2 != 0:
        list.append(value)
new = {}
for value in list: 
    for key,val in stu.items():
        if val == value:
            new[val] = value

print(new)'''

# 32. Return only the prime values from a dictionary.
'''stu = {
    "Priya": 2,
    "Neha": 5,
    "Rohan": 8,
    "Amit" : 10
}
list = []

for value in stu.values():
    list.append(value)

prime_numbers = []


for num in list:
    is_prime = True

    if num <= 1:
        is_prime = False

    else:
        for i in range(2,num):
           if num % i == 0:
                is_prime = False
                break

    if is_prime:
        prime_numbers.append(num)


print(prime_numbers)

new = {}
for value in prime_numbers: 
    for key,val in stu.items():
        if val == value:
            new[key] = val

print(new)'''

# 33. Create a nested dictionary of student details.
'''students = {
    "Ankit": {
        "Age": 20,
        "Marks": 90,
        "City": "Delhi"
    },

    "Rahul": {
        "Age": 21,
        "Marks": 85,
        "City": "Lucknow"
    },

    "Priya": {
        "Age": 19,
        "Marks": 95,
        "City": "Kanpur"
    }
}

print(students)'''

# 34. Search for a key entered by the user.
'''stu = {
    "Priya": 2,
    "Neha": 5,
    "Rohan": 8,
    "Amit" : 10
}
keyy =input("Enter a Key:")

found = False
for key,value in stu.items():
    if keyy == key:
        print("Found:",key,value)
        found = True
        break

if not found:
    print("Not Found")'''
    

# 35. Search for a value entered by the user.
'''value = int(input("Enter a Value:"))
stu = {
    "Priya": 2,
    "Neha": 5,
    "Rohan": 8,
    "Amit" : 10
}
count = 0
for val in stu.values():
    if val == value:
        count += 1
        
if count > 0:
    print("Key Found")
else:
    print("Not Found")'''
        


# 36. Count how many values are greater than 100.
'''stu = {
    "Priya": 2,
    "Neha": 500,
    "Rohan": 800,
    "Amit" : 10
}
count = 0
for value in stu.values():
    if value > 100:
        count += 1
print("The total value >100 is:",count)'''


# 37. Find duplicate values in a dictionary.
'''stu = {
    "Priya": 2,
    "Neha": 500,
    "Rohan": 800,
    "Amit" : 500
}
list = []
for value in stu.values():
    if value not in list:
        list.append(value)
    else:
        print(value)'''

# 38. Remove all keys having duplicate values.

'''stu = {
    "Priya": 2,
    "Neha": 500,
    "Rohan": 800,
    "Amit": 500
}

new = {}

for key, value in stu.items():
    if list(stu.values()).count(value) == 1:
        new[key] = value

print(new)'''
        

# 39. Flatten a nested dictionary.

# 40. Create a dictionary comprehension that stores the square of numbers from 1 to 20.

# ------------ IPL Data Analytics (41–50) ------------

# 41. Create a dictionary of IPL players and their total runs.bv
players = {
    "Virat":915,
    "Rohit":654,
    "suman":535,
    "Manish":654
}
print(players)


# 42. Find the Orange Cap winner.
'''list = []

for key, value in players.items():
    list.append(value)

highest =max(list)

for key,value in players.items():
    if value == highest:
        print("The Orange cap Winner is:",key)'''

# 43. Find the player with the lowest runs.
'''list = []

for key, value in players.items():
    list.append(value)
lowest = min(list)

for key,value in players.items():
    if value == lowest:
        print("The lowest run is:",key,value)'''

# 44. Find all players having more than 500 runs.
'''new = {}
for player,run in players.items():
        if run > 600:
            new[player] = run
print(new)'''

# 45. Calculate the average runs of all players.
'''count =len(players)
avg = sum(students.values()) / count
print(avg)'''

# 46. Create a nested dictionary:

players = {
    "Virat": {
        "Runs": 741,
        "Fours": 62,
        "Sixes": 38
    },
    "Rohit": {
        "Runs": 850,
        "Fours": 70,
        "Sixes": 45
    },
    "Rahul": {
        "Runs": 650,
        "Fours": 55,
        "Sixes": 30
    }
}

# Find:
# • Highest Runs
'''list = []
for player,details in players.items():
    list.append(details['Runs'])
    
highest = max(list)
for player,details in players.items():
    if details['Runs'] == highest:
        print("Highest Run =>",player,":",details['Runs'])'''

# • Highest Fours
'''fours = []
for player,details in players.items():
    fours.append(details['Fours'])

Highest = max(fours)

for player ,details in players.items():
    if details['Fours'] == Highest:
        print("The Highest Fours is =>",player,":",details['Fours'])'''


# • Highest Sixes
'''sixs = []
for player,details in players.items():
    sixs.append(details['Sixes'])

Highest = max(sixs)

for player ,details in players.items():
    if details['Sixes'] == Highest:
        print("The Highest Sixs is =>",player,":",details['Sixes'])'''

# 47. Given a dictionary of teams and points,
teams = {
    "India": 10,
    "Australia": 8,
    "England": 6,
    "Pakistan": 4
}
# find the team having maximum points.
'''list = []
for team, point in teams.items():
    list.append(point)
maxim = max(list)

for team, point in teams.items():
    if point == maxim:
        print("The team having maximum points.",team,point)'''
    

# 48. Given player → team dictionary,
players = {
    "Virat": "India",
    "Rohit": "India",
    "Babar": "Pakistan",
    "Smith": "Australia"
}
# count how many players belong to each team.
team_count = {}
for player,team in players.items():

    if team in team_count:
        team_count[team] += 1
    else:
        team_count[team] = 1
print(team_count)



# 49. Create a scoreboard.

# Example:

# {
# "Virat":80,
# "Gill":45,
# "Dhoni":22
# }

# Update runs after every over.

# 50. MINI IPL DATA ANALYTICS PROJECT

# Given:

# players = {
# "Virat":{"Runs":741,"SR":154,"Team":"RCB"},
# "Gill":{"Runs":890,"SR":158,"Team":"GT"},
# "Dhoni":{"Runs":161,"SR":220,"Team":"CSK"},
# "Rohit":{"Runs":417,"SR":146,"Team":"MI"},
# "KL Rahul":{"Runs":520,"SR":138,"Team":"LSG"}
# }

# Perform all operations:

# • Find Orange Cap winner.
# • Find highest strike rate.
# • Find lowest runs.
# • Find average runs.
# • Find players above 500 runs.
# • Count players team-wise.
# • Sort players by runs.
# • Search a player.
# • Update player statistics.
# • Delete a player.
# • Add a new player.
# • Display Top 3 players.


