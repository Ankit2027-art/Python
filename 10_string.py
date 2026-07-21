# What is a String?

'''A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).'''

# A string can contain:

'''Letters
Numbers
Symbols
Spaces
Special characters'''

# In Python, a string's data type is str.


#creating Strings
name="ankit"
name1='ankit'
name2='''ankit  is a,
good
 boy'''
message = """
Hello
Welcome
to Python
"""
'''print(message)
print(name)
print(name1)
print(name2)

print(name[0])'''


#Accesing Character

'''name = "Ankit"

print(name[0])
print(name[1])
print(name[4])

#negative indexing
name = "Ankit"

print(name[-1])
print(name[-2])'''

# string Slicing

# sytex---string[start : end]

'''name = "DataAnalytics"

print(name[0:4])
name = "Python"

print(name[0:3])
print(name[2:6])
print(name[:4])
print(name[3:])
print(name[:])'''


# String Immutability

'''Strings cannot be changed after they are created.
❌ Wrong
name = "Ankit"
name[0] = "R" '''


#String Concatenation

    # Joining strings using +.
'''first = "Data"
second = "Analytics"

print(first + " " + second)'''

#String Repetition.
print("Python " * 3)


#Membership Oprators
name = "Python"

print("P" in name)
print("z" in name)


# METHODS of String
# 1.upper()
'''text = "python"
print(text.upper())'''

# 2.Lower()
'''text = "PYTHON"
print(text.lower())'''

# 3.title()
'''text = "data analytics"

print(text.title())'''

# 4.capitalize()
'''text = "python"
print(text.capitalize())'''

# 5.strip()
"""Removes spaces from both ends."""
'''text = "   Python   "

print(text.strip())'''

# 6.Replace()
'''text = "I like Java"

print(text.replace("Java", "Python"))'''

# 7.find()
"""Returns the index of the first occurrence."""
'''text = "Python"

print(text.find("t"))'''

# 8.count()
'''text = "banana"

print(text.count("a"))'''

# 9.startswith()
'''text = "Python"

print(text.startswith("Py"))'''

# 10.endswith()
'''text = "Python"

print(text.endswith("on"))'''

#11.split()
"""text = "Python,Java,C++"

print(text.split(","))"""

#12.join()

'''languages = ["Python", "SQL", "Excel"]

print(" | ".join(languages))'''

# 13.Escape Characters:
print("I'm learning Python")
print('I\'m learning Python')

    #new line
print("Hello\nWorld")



#Comparison
print("Python" == "Python")
print("Python" == "python")


#loop trough string
text = "Python"
i = 0
while i < len(text):
    print(text[i])
    i += 1



print("PRACTICE QUESTIONS")
# =========================
# PYTHON STRING PRACTICE QUESTIONS
# (Basic → Advanced)
# =========================

# 🟢 Level 1: Basic (1–10)

# 1. Create a string containing your full name and print it.
'''name = "Amit Singh"
print(name)'''

# 2. Create a multiline string using triple quotes and print it.
'''message = """
Hello Everyone,
Welcome to Python Programming.
Have a Great Day!
"""

print(message)'''

# 3. Create a string "Python" and print its data type.
'''string = "Python"
print(type(string))'''


# 4. Print the first character of "DataAnalytics".
'''string = "DataAnalytics"
print(string[0])'''

# 5. Print the last character of "Programming" using negative indexing.
'''string = "Programming"
print(string[-1])'''

# 6. Print the third character of "Machine".
'''string = "Machine"
print(string[2])'''

# 7. Print all characters of "Python" using positive indexing.

'''string = "Python"

print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])'''



# 8. Print all characters of "Python" using negative indexing.
'''string = "Python"

for i in range(-6, 0):
    print(string[i])'''

# 9. Check whether "SQL" is a string.
'''print(type("SQL"))'''

# 10. Create two strings "Hello" and "World" and print:
#     Hello World
#     using concatenation.
'''a = "Hello"
b = "World"
print( a +" "+ b)'''

# =========================

# 🟡 Level 2: String Slicing (11–15)

# 11. Print the first 5 characters of "DataAnalytics".
'''string = "DataAnalytics"
print(string[:5])'''
# 12. Print the last 4 characters of "PythonProgramming".

# 13. Print every second character of "Analytics".

# 14. Reverse the string "Python" using slicing.

# 15. Print every third character of "DataScience".

# =========================

# 🟡 Level 3: String Immutability & Operators (16–20)

# 16. Try changing the first letter of "Python" to "J". What error do you get?

# 17. Repeat the string "Python " five times.

# 18. Check whether "Data" exists inside "DataAnalytics".
'''string = "DataAnalytics"
print("Data" in string)'''

# 19. Check whether "Java" exists inside "Python".

# 20. Write a program that asks the user for a word and checks whether the letter "a" exists in it.
'''word = input("Enter a word: ")
if "a" in word:
    print("Letter 'a' found in the word.")
else:
    print("Letter 'a' not found in the word.")'''

# =========================

# 🟠 Level 4: String Methods (21–25)

# 21. Convert "python programming" into uppercase.
'''string ="python programming"
print(string.upper())'''

# 22. Convert "PYTHON" into lowercase.

# 23. Convert "data analytics with python" into title case.

# 24. Capitalize the first letter of "machine learning".

# 25. Remove extra spaces from:
'''space = "     Python     "
print(space.strip())'''


# =========================

# 🔴 Level 5: Important Methods (26–30)

# 26. Replace "Java" with "Python" in:
'''string = "I love Java"
print(string.replace("Java","Python"))'''


# 27. Find the first occurrence of "a" in:
string = "DataAnalytics"
print(string.find("a"))

# 28. Count how many times "an" appears in:
string = "banana"
print(string.count("an"))

# 29. Check whether "Python" starts with "Py" and ends with "on".
string = "Python"
print(string.startswith("Py") and string.endswith("on"))

# 30. Split the following string into a list:
#     "Python,SQL,Excel,Power BI"
#     Then join it again using " | " as the separator.
string = "Python,SQL,Excel,Power BI"

data = string.split(",")
print(data)

result = " | ".join(data)
print(result)
# =========================
# ⭐ BONUS INTERVIEW QUESTIONS
# =========================

# 31. Reverse a string without using slicing.

# 32. Count the total number of vowels in a string.

# 33. Count the total number of consonants in a string.

# 34. Check whether a string is a palindrome.

# 35. Remove all spaces from a string.

# 36. Find all duplicate characters in a string.

# 37. Find the most frequent character in a string.

# 38. Count uppercase letters, lowercase letters, digits, spaces, and special characters.

# 39. Check whether two strings are anagrams.

# 40. Reverse the order of words in a sentence.
#     Example:
#     Input: "I Love Python"
#     Output: "Python Love I"

# 41. Find the length of a string without using len().

# 42. Count the occurrence of each character in a string.

# 43. Print only the unique characters from a string.

# 44. Find the first non-repeating character in a string.

# 45. Remove duplicate characters from a string.

# 46. Replace all spaces with underscores (_).

# 47. Check whether a string contains only alphabets.

# 48. Check whether a string contains only digits.

# 49. Find the longest word in a sentence.

# 50. Ask the user to enter a sentence and display:
#     - Number of words
#     - Number of characters
#     - Number of vowels
#     - Number of consonants