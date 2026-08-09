# PYTHON SET — 50 PRACTICE QUESTIONS
# Data Analytics + IPL Level
# ====================================

# LEVEL 1 — SET BASICS

# 1. Create a set containing the numbers 10, 20, 30, 40, 50 and print it.

# 2. Create a set from the list [10, 20, 20, 30, 30, 40] and remove duplicate values.

# 3. Create an empty set and verify its data type.

# 4. Create a set containing an integer, float, string, and Boolean value.

# 5. Given numbers = {10, 20, 30, 40}, check whether 30 exists using the in operator.

# 6. Given numbers = {10, 20, 30, 40}, check whether 50 does not exist using the not in operator.

# 7. Add 50 to the set {10, 20, 30, 40} using add().

# 8. Add the elements [50, 60, 70] to {10, 20, 30, 40} using update().

# 9. Remove 30 from {10, 20, 30, 40} using remove().

# 10. Remove 50 from {10, 20, 30, 40} using discard() without causing an error.


# LEVEL 2 — SET METHODS & OPERATIONS

# 11. Given {10, 20, 30, 40}, use pop() to remove an element and print the removed element.

# 12. Create a set {1, 2, 3, 4, 5} and remove all elements using clear().

# 13. Create a copy of {10, 20, 30} using copy() and prove that modifying the copy does not modify the original.

# 14. Given:
#     A = {1, 2, 3, 4}
#     B = {3, 4, 5, 6}

#     Find their union using union().

# 15. Find the union of A and B using the | operator.

# 16. Find the intersection of:
#     A = {1, 2, 3, 4}
#     B = {3, 4, 5, 6}

#     using intersection().

# 17. Find the intersection of two sets using the & operator.

# 18. Find the elements present in A but not in B using difference().

# 19. Find the elements present in B but not in A.

# 20. Find the symmetric difference between:
#     A = {1, 2, 3, 4}
#     B = {3, 4, 5, 6}


# LEVEL 3 — ADVANCED SET CONCEPTS

# 21. Perform symmetric difference using the ^ operator.

# 22. Use intersection_update() to keep only the common elements of two sets in the first set.

# 23. Use difference_update() to remove all elements of the second set from the first set.

# 24. Use symmetric_difference_update() and observe how the original set changes.

# 25. Check whether {1, 2} is a subset of {1, 2, 3, 4} using issubset().

# 26. Check whether {1, 2, 3, 4} is a superset of {1, 2} using issuperset().

# 27. Check whether two sets are disjoint using isdisjoint().

# 28. Determine whether {1, 2} is a proper subset of {1, 2, 3} using the < operator.

# 29. Determine whether {1, 2, 3} is a proper superset of {1, 2} using the > operator.

# 30. Create a set comprehension that generates the squares of numbers from 1 to 10.


# LEVEL 4 — SET PROBLEM SOLVING

# 31. Given:
#     numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]

#     Remove duplicates and keep only unique values.

# 32. Given two lists of student names, find students who appear in both lists.

# 33. Given two lists of customers, find customers who purchased in the first month but not in the second month.

# 34. Given two lists of employees, find employees who are present in either list but not both.

# 35. Given a list of product categories, find the number of unique categories.

# 36. Given the string "programming", find all unique characters using a set.

# 37. Given a sentence, find the number of unique words in it.

# 38. Given:
#     numbers = [10, 20, 20, 30, 40, 40, 50]

#     Find the unique numbers and calculate how many unique values exist.

# 39. Given two lists of numbers, find their common elements using sets.

# 40. Given:
#     A = {1, 2, 3, 4, 5}
#     B = {2, 4}
#     C = {4, 5, 6}

#     Find:
#     - A union B
#     - A intersection B
#     - A difference B
#     - A intersection C
#     - A union C
#     - A symmetric difference C


# LEVEL 5 — IPL / DATA ANALYTICS QUESTIONS

# 41. Given:
#     matches = [
#         ("CSK", "MI"),
#         ("RCB", "KKR"),
#         ("MI", "DC"),
#         ("CSK", "RCB"),
#         ("KKR", "DC")
#     ]

#     Find all unique teams that participated in the matches.

# 42. Given:
#     csk_opponents = {"MI", "RCB", "KKR", "GT"}

#     Check whether "MI" and "DC" played against CSK.

# 43. Given:
#     csk = {"MI", "RCB", "KKR", "GT"}
#     mi = {"CSK", "RCB", "KKR", "DC"}

#     Find the teams that both CSK and MI played against.

# 44. Given:
#     match1 = {"Virat", "Rohit", "Dhoni", "Jadeja"}
#     match2 = {"Rohit", "Hardik", "Dhoni", "Bumrah"}

#     Find all unique players who appeared in either match.

# 45. Using the same data, find players who appeared in both matches.

# 46. Using:
#     match1 = {"Virat", "Rohit", "Dhoni", "Jadeja"}
#     match2 = {"Rohit", "Hardik", "Dhoni", "Bumrah"}

#     Find players who appeared in match2 but did not appear in match1.

# 47. Given:
#     csk_venues = {"Chennai", "Mumbai", "Delhi", "Bangalore"}
#     mi_venues = {"Mumbai", "Delhi", "Kolkata", "Hyderabad"}

#     Find:
#     - Common venues
#     - Venues where only CSK played
#     - Venues where only MI played
#     - All unique venues

# 48. Given:
#     match1_players = {"Virat", "Faf", "Maxwell", "Siraj"}
#     match2_players = {"Virat", "Faf", "Siraj", "Rashid"}
#     match3_players = {"Virat", "Maxwell", "Rashid", "Gill"}

#     Find:
#     - Players who played in all three matches
#     - Players who played in match 1 and match 2
#     - Players who played only in match 3
#     - Total unique players across all three matches

# 49. Given:

#     season_2024 = {
#         "CSK", "MI", "RCB", "KKR", "SRH",
#         "RR", "DC", "PBKS", "GT", "LSG"
#     }

#     season_2025 = {
#         "CSK", "MI", "RCB", "KKR", "SRH",
#         "RR", "DC", "PBKS", "GT", "LSG"
#     }

#     Determine:
#     - Teams present in both seasons
#     - Teams only in 2024
#     - Teams only in 2025
#     - Total unique teams across both seasons
#     - Whether both seasons contain exactly the same teams

# 50. IPL DATA ANALYTICS CHALLENGE

#     Given:

#     team_A_players = {
#         "Virat", "Faf", "Maxwell", "Siraj", "Kohli"
#     }

#     team_B_players = {
#         "Rohit", "Hardik", "Bumrah", "Sky", "Tilak"
#     }

#     team_C_players = {
#         "Virat", "Gill", "Rashid", "Siraj", "Shami"
#     }

#     Write a program to find:

#     1. All unique players across the three teams.
#     2. Players common between Team A and Team B.
#     3. Players common between Team A and Team C.
#     4. Players common between Team B and Team C.
#     5. Players who belong to Team A but not Team C.
#     6. Players who belong to Team C but not Team A.
#     7. Players who are present in exactly one of the teams.
#     8. Total number of unique players.
#     9. Check whether Team A and Team B have any common players.
#     10. Check whether Team A is a subset of the combined Team B and Team C players.