# “If-else is a decision-making statement in Python.??

    # It is used to execute different blocks of code based on a condition.
    # If the condition is true, the if block executes; otherwise, the else block executes.”


'''age =int(input("enter your age:"))
if(age>18):
    print("you can drive")
    print("thank you")
elif(age == 18):
    print("Lets schedule an interview")
else:
    print("you can't drive")
    print("thank you")'''



#1-even odd
'''a=int(input("enter a numer:"))
if(a%2==0):
    print("number is even")
else:
    print("number is odd")'''

print("\n")

#2-largest of two number
'''b=int(input("enter a first number:"))
c=int(input("enter a second number"))
if(b>c):
    print("first num is greater then sec")
else:
    print("sec num is greater then first num")'''

#3-age group cheaker
'''age=int((input("enter a age:")))
if(age<13):
    print("child")
elif(13<=age<20): #WE CAN USE TWO OPERATORS ASIDE
    print("Teenager")
else:
    print("Adult")'''

#4-postive negative zero cheak
'''a=int(input("enter a number:"))
if(a>0):
    print("number is postive")
elif(a==0):
    print("number is zero")
else:
    print("number is negative")'''

# pass or fail
'''num=int(input("enter a number:"))
if(num>=35):
    print("passed")
else:
    print("failed")'''



'''marks=int(input("Enter a marks of students:"))
if marks>=90:
    print("Ex")
elif marks>=90:
    print("A")
elif marks>=80:
    print("B")

elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("F")'''


'''a = int(input("enter the number a: "))
b=int(input("enter the number b:"))

if (a>b):
    print("a is greater than b")

elif(a==b):
    print("a is equal to b")

else:
    print("b is greater than a")

print("commmands end")'''



# THIS IS FOR STRING INPUT NOT FOR INDIVIDUAL CHAR

'''a=(input("enter the word:"))
b="Ankit"
if a==b:
    print("you are elligible")

else:
    print("you are not")'''
    


#ADV LEVEL PRACTICE QUESTIONS.


#Vovel Consonent Cheak Program.
'''ch=input("enter a charecter:")
if len(ch) == 1 and ch.isalpha():
    if ch in "AEIOUaeiou":
        print("Char is vovel")
    else:
        print("Char is consonent")
elif not ch.isalpha():
    print("Enter a alphabet ,not an integer or Symbol.")
else:
    print("Please enter a Single Alphabet")'''



#Check whether a number is a multiple of 3 and 7.
'''num =int(input("Enter a number:"))
if (num % 3 == 0) & (num % 7 == 0):
    print(num,".is multiple of both 3 and 7")
elif (num % 3 == 0):
    print(num,".is Multiple of 3")
elif (num % 7 == 0):
    print(num,".is Multiple of 7")
else:
    print(num,"is not a multiple of 3 nor 7")'''

# Check whether a triangle is equilateral, isosceles, or scalene.
'''a,b,c = map(int,input("Enter a sides of triangle with Space:").split())
if (a != b) and (b != c) and (c != a):
    print("The triangle is Scalence Triangle:")
elif(a == b == c):
    print("The Trianle is Equilateral")
else:
    print("The Trianle is  Isosceles")'''

# Find whether a character is:Alphabet,Digit,Special character.
'''character = input("Enter a Character:")
if character.isalpha():
    print(character,",is  a Alphabed")
elif character.isdigit():
    print(character,",is a Digit")
else:
    print(character,".is a Special Character")'''


# Check whether a number is a 3-digit number.
'''num = int(input("Enter a Digit:"))
if (num >=100) and (num <=999):
    print("The number is a 3-digit number.")
else:
    print("The number is  not a 3-digit number.")'''
# Or
num = int(input("Enter a Digit:"))
'''if 100 <= abs(num) <= 999:
#or
if len(str(abs(num))) == 3:
    print("The number is a 3-digit number.")
else:
    print("The number is  not a 3-digit number.")'''

# Find the second largest among three numbers.

# Check whether a number lies between 100 and 500.
# Determine if a student passes or fails based on marks in 3 subjects.
# Find the greatest among four numbers.


