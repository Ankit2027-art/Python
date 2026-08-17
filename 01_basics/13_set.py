# PYTHON SET — 50 PRACTICE QUESTIONS
# Data Analytics + IPL Level
# ====================================

# LEVEL 1 — SET BASICS

# 1. Create a set containing the numbers 10, 20, 30, 40, 50 and print it.
'''a = {10, 20, 30, 40, 50}
print(a)'''

# 2. Create a set from the list [10, 20, 20, 30, 30, 40] and remove duplicate values.
'''list =[10, 20, 20, 30, 30, 40]
print(set(list))'''

# 3. Create an empty set and verify its data type.
'''empty = set()
print(type(empty))'''

# 4. Create a set containing an integer, float, string, and Boolean value.
'''set = {50,"ankit",52.5,True}
print(set)'''

# 5. Given numbers = {10, 20, 30, 40}, check whether 30 exists using the in operator.
numbers = {10, 20, 30, 40}

'''if 30 in numbers:
    print("Exist")
else:
    print("Not Exists")  '''



# 6. Given numbers = {10, 20, 30, 40}, check whether 50 does not exist using the not in operator.
'''if 50 not in numbers:
    print("Not Exist")
else:
    print("Exixt")'''

# 7. Add 50 to the set {10, 20, 30, 40} using add().
'''numbers.add(50)
print(numbers)'''

# 8. Add the elements [50, 60, 70] to {10, 20, 30, 40} using update().
'''numbers.update([50, 60, 70])
print(numbers)'''


# 9. Remove 30 from {10, 20, 30, 40} using remove().
'''numbers.remove(30)
print(numbers)'''

# 10. Remove 50 from {10, 20, 30, 40} using discard() without causing an error.
'''a ={10, 20, 30, 40} 
a.discard(50)
print(a)'''

# LEVEL 2 — SET METHODS & OPERATIONS

# 11. Given {10, 20, 30, 40}, use pop() to remove an element and print the removed element.

a = {10, 20, 30, 40}
'''aa= a.pop()
print(a)'''

# 12. Create a set {1, 2, 3, 4, 5} and remove all elements using clear().
'''clear = a.clear()
print(clear)'''


# 13. Create a copy of {10, 20, 30} using copy() and prove that modifying the copy does not modify the original.
'''b = a.copy()
print(b)'''

# 14. Given:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#     Find their union using union().
'''union =(A | B)
print(union)'''

# 15. Find the union of A and B using the | operator.

# 16. Find the intersection of:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#     using intersection().
'''print(A.intersection(B))'''

# 17. Find the intersection of two sets using the & operator.
'''print(A & B)'''

# 18. Find the elements present in A but not in B using difference().
'''print(A -B)'''

# 19. Find the elements present in B but not in A.

# 20. Find the symmetric difference between:
'''A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A ^ B)'''

# LEVEL 3 — ADVANCED SET CONCEPTS

# 21. Perform symmetric difference using the ^ operator.
'''print(A.symmetric_difference(B))
print( A ^ B)'''

# 22. Use intersection_update() to keep only the common elements of two sets in the first set.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
'''A.intersection_update(B)
print(A)'''

# 23. Use difference_update() to remove all elements of the second set from the first set.
'''A.intersection_update(B)
print(B)'''

# 24. Use symmetric_difference_update() and observe how the original set changes.
'''A.symmetric_difference_update(B)
print(B)'''

# 25. Check whether {1, 2} is a subset of {1, 2, 3, 4} 
a = {1,2}
b = {1, 2, 3, 4} 
'''print(a.issubset(b))
print(a <= b)'''

# 26. Check whether {1, 2, 3, 4} is a superset of {1, 2} 
'''print(b.issuperset(a))'''

# 27. Check whether two sets are disjoint.
'''print(a.isdisjoint(b))'''


# 28. Determine whether {1, 2} is a proper subset of {1, 2, 3} 

# 29. Determine whether {1, 2, 3} is a proper superset of {1, 2} 

# 30. Create a set comprehension that generates the squares of numbers from 1 to 10.
'''sq = {x * x for x in range(1,10)}
print(sq)'''

# LEVEL 4 — SET PROBLEM SOLVING

# 31. Given:
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]

#     Remove duplicates and keep only unique values.
'''set = set(numbers)
print(set)'''

# 32. Given two lists of student names, find students who appear in both lists.
'''list1 = ["Rahul", "Aman", "Priya", "Sneha"]
list2 = ["Priya", "Sneha", "Rohit", "Aman"]
common = set(list1) & set(list2)
print(common)'''

# 33. Given two lists of customers, find customers who purchased in the first month but not in the second month.
'''First_month = ["Aman", "Rahul", "Priya", "Sneha", "Vikas"]

sec_month = ["Priya", "Rohit", "Aman", "Neha", "Sneha"]
diff = set(First_month) - set(sec_month)
print(diff)'''


# 34. Given two lists of employees, find employees who are present in either list but not both.
'''customers1 = ["Aman", "Rahul", "Priya", "Sneha", "Vikas"]

customers2 = ["Priya", "Rohit", "Aman", "Neha", "Sneha"]
aa =  (set(customers1) ^ set(customers2))
print(aa)'''

# 35. Given a list of product categories, find the number of unique categories.
'''categories = ["Electronics", "Clothing", "Grocery", "Electronics", "Books", "Clothing", "Toys", "Grocery"]
uniqe = set(categories)
print(uniqe)'''

# 36. Given the string "programming", find all unique characters using a set.
'''string = "programming"
print(set(string))'''

# 37. Given a sentence, find the number of unique words in it.
'''sentence = "Python is easy to learn and Python is powerful"
list =sentence.split()
print(set(list))'''

# 38. Given:
numbers = [10, 20, 20, 30, 40, 40, 50]

#     Find the unique numbers and calculate how many unique values exist.
'''print(set(numbers))
print(len(set(numbers)))'''

# 39. Given two lists of numbers, find their common elements using sets.
'''A = {1, 2, 3, 4, 5}
B = {2, 4}
print(A & B)'''

# 40. Given:
A = {1, 2, 3, 4, 5}
B = {2, 4}
C = {4, 5, 6}   

#     Find:
'''#     - A union B
print("Union",A | B)
#     - A intersection B
print("Intersection:", A & B)
#     - A difference B
print("Diffrence:",A-B)
#     - A intersection C
print("Diffrence:",A-C)
#     - A union C
print("Union:",A | B)
#     - A symmetric difference C
print("Symmentric Diff:",A ^ C)'''


# LEVEL 5 — IPL / DATA ANALYTICS QUESTIONS

# 41. Given:
matches = [
        ("CSK", "MI"),
        ("RCB", "KKR"),
        ("MI", "DC"),
        ("CSK", "RCB"),
        ("KKR", "DC")
    ]

#     Find all unique teams that participated in the matches.
'''list = []
for team1, team2 in matches:
    if team1 not in list:
        list.append(team1)
    if team2 not in list:
        list.append(team2)
    
print(set(list))'''

# 42. Given:
csk_opponents = {"MI", "RCB", "KKR", "GT"}

#     Check whether "MI" and "DC" played against CSK.
'''if "MI" in csk_opponents and "DC" in csk_opponents:
    print("Yes, both played against CSK")
else:
    print("Not both played against CSK")'''

# 43. Given:
'''csk = {"MI", "RCB", "KKR", "GT"}
mi = {"CSK", "RCB", "KKR", "DC"}

#     Find the teams that both CSK and MI played against.
print(csk & mi)'''

# 44. Given:
match1 = {"Virat", "Rohit", "Dhoni", "Jadeja"}
match2 = {"Rohit", "Hardik", "Dhoni", "Bumrah"}

#     Find all unique players who appeared in either match.
'''print(match1 | match2)'''

# 45. Using the same data, find players who appeared in both matches.
'''print(match1 & match2)'''
# 46. Using:
match1 = {"Virat", "Rohit", "Dhoni", "Jadeja"}
match2 = {"Rohit", "Hardik", "Dhoni", "Bumrah"}

#     Find players who appeared in match2 but did not appear in match1.
'''print(match2 - match1)'''
# 47. Given:
'''csk_venues = {"Chennai", "Mumbai", "Delhi", "Bangalore"}
mi_venues = {"Mumbai", "Delhi", "Kolkata", "Hyderabad"}

#     Find:
#     - Common venues
print(csk_venues & mi_venues)
#     - Venues where only CSK played
print(csk_venues - mi_venues)
#     - Venues where only MI played
print(mi_venues - csk_venues)
#     - All unique venues
print(csk_venues ^ mi_venues)'''

# 48. Given:
match1_players = {"Virat", "Faf", "Maxwell", "Siraj"}
match2_players = {"Virat", "Faf", "Siraj", "Rashid"}
match3_players = {"Virat", "Maxwell", "Rashid", "Gill"}

#     Find:
'''#     - Players who played in all three matches
print(match1_players & match2_players & match3_players)
#     - Players who played in match 1 and match 2
print(match1_players & match2_players)
#     - Players who played only in match 3
print(match3_players - (match1_players | match2_players))
#     - Total unique players across all three matches
print(match1_players | match2_players | match3_players)'''
# 49. Given:

season_2024 = {
        "CSK", "MI", "RCB", "KKR", "SRH",
        "RR", "DC", "PBKS",  "LSG"
    }

season_2025 = {
        "CSK", "MI", "RCB", "KKR", "SRH",
        "RR", "DC", "PBKS", "GT"
    }

#     Determine:
'''#     - Teams present in both seasons
print(season_2024 & season_2025)
#     - Teams only in 2024
print(season_2024 - season_2025)
#     - Teams only in 2025
print(season_2025 - season_2024)
#     - Total unique teams across both seasons
print(season_2025 | season_2024)
#     - Whether both seasons contain exactly the same teams
print(season_2025 == season_2024)'''

# 50. IPL DATA ANALYTICS CHALLENGE

#     Given:

'''team_A_players = {
        "Virat", "Faf", "Maxwell", "Siraj", "Kohli"
    }

team_B_players = {
        "Rohit", "Hardik", "Bumrah", "Sky", "Tilak"
    }

team_C_players = {
        "Virat", "Gill", "Rashid", "Siraj", "Shami"
    }

#     Write a program to find:

#     1. All unique players across the three teams.
print(team_A_players | team_B_players | team_C_players)
#     2. Players common between Team A and Team C.
print(team_A_players  & team_C_players)

#     4. Players common between Team B and Team C.
print(team_B_players  & team_C_players)
#     5. Players who belong to Team A but not Team C.
print(team_A_players - team_C_players)
#     6. Players who belong to Team C but not Team A.
print(team_C_players - team_A_players)
#     7. Players who are present in exactly one of the teams.
print((team_A_players ^ team_B_players) ^ team_C_players)
#     8. Total number of unique players.
print(team_A_players  | team_B_players | team_C_players)
#     9. Check whether Team A and Team B have any common players.
print(team_A_players  & team_B_players)
#     10. Check whether Team A is a subset of the combined Team B and Team C players.
print(team_A_players.isubset(team_B_players | team_C_players))'''
