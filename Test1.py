# --------------------------------------Easy Questions
# Write a program that prints "Hello, Python!".
print('"Hellow, Python!".')
# Create a variable that stores your age and print it using a print() function.
age = 20
print("Age is",age)
# Write a program that adds two floating-point numbers and prints the result.
a = 1.233
b = 45.343
print("addition is ",(a + b))
# Write a program to check if a number is divisible by 5.
# num = int(input("NUmber:"))
# check_if = (num // 5 == 0)
# print(check_if)
# Create a list of 3 strings and print the second item.
str1 = ["Deepak","Mahadev","Jadhav"]
print(str1[(len(str1)//2)])
# Write a program that creates a tuple with three elements and prints all the elements.
tuples1 = ("mango","banana","orange")
print(tuples1)
# Create a set from a list of numbers and remove an element from the set.
number = [1,2,3,4,5,6,7]
set_number = set(number)
set_number.remove(3)
print(set_number)
# Write a program that adds a new key-value pair to a dictionary and prints the updated dictionary.
person = {
    'name':'Deepak',
    'city':'Kolhapur',
    'cillage':'Hasurchampu'
}
person["country"] = "India"
print(person)
# Write a program that checks if a number is positive, negative, or zero using an if-else statement.
# num1 = int(input("Number:"))
# if num1 > 0:
#     print("positive")
# elif num1 < 0:
#     print("Negative")
# elif num1 == o:
#     print("0")
# else:
#     print("invalid output")
# Write a program that uses a for loop to print numbers from 1 to 5.
for i in range(1,6):
    print(i)

# ---------------------------------------Medium Questions
# Write a program that calculates the area of a circle using a user-provided radius.
# radius = int(input("Enter Radius of Circle:"))
# pi = 3.14
# print("Radius of Circle is :",(pi*(radius**2)))

# Write a program that takes a user's input for name and age, then prints a greeting message.
# name = input("Enter Name:")
# age = int(input("Enter Your age"))

# print(f"Good morning! {name} , and you are of {age} right ?")

# Write a program that multiplies two numbers and prints the result only if it's greater than 100.
# num2 = int(input("Enter num1:"))
# num3 = int(input("Enter num2:"))
# if (num2 * num3)>100:
#     print(f"multiple of {num2} and {num3} is",(num2 * num3))
# else:
#     print("Multiple of Two number is not more than 100")
# Write a program that counts the number of vowels in a given string.
# vowels = ["a","e","i","o","u"]
# count = []
# str2 = input("Enter string:")
# for letter in str2:
#     if letter in vowels:
#         count.append(letter)

# print(f"There are {len(count)} vowels in {str2}")
# Write a program that appends a new item to a list, then sorts the list in ascending order.
# lst1 = [1,3,4,2,7,5,4,3]
# num2 = int(input("Num :"))
# lst1.append(num2)
# print(lst1)
# lst1.sort()
# print(lst1)
# Write a program that unpacks a tuple into individual variables and prints them.
# tuples1 = (2,3,1,3,4,3,4,5,6)

# for i in tuples1:
#     print(i)
# Write a program that finds the union of two sets.
set1 = {3,4,5,2,5,2}
set2 = {1,6,4,3,8,1}
set1.union(set2)
print(set1)
# Write a program that takes input from the user for keys and values, creates a dictionary, and prints it.
dict2 = {
    'name':'Deepak',
    'last_name':'Jadhav',
    'city':'Gadhinglaj'
}
dict2['village'] = 'Hasurchampu'
print(dict2)
# Write a program that checks if a number is a prime number using conditional statements.
num3 = int(input("Enter Numnber :"))

if num3 <= 1:
    print(f"{num3} is Not a Prime Number")
else:
    is_prime = True
    for i in range(2,num3):
        if num3 % i == 0:
            is_prime = False
    
if is_prime:
    print("prime")
else:
    print("not Prime")
# Write a program that uses a while loop to print the first 10 numbers in reverse order (from 10 to 1).
num4 = 10
while num4 > 0:
    print(num4,end=" ")
    num4 -= 1

#-------------------------------------- Hard Questions
# Write a program that takes a user's birth year and calculates their current age.
# Write a program that checks if a given string is a palindrome (reads the same forward and backward).
# Write a program that finds the largest number among three given numbers using logical operators.
# Write a program that takes a sentence from the user and prints each word on a new line.
# Write a program that removes all occurrences of a specific element from a list.
# Write a program that concatenates two tuples and then slices the concatenated tuple.
# Write a program that creates two sets and checks if they have any common elements.
# Write a program that stores students' names and their scores in a dictionary, then calculates the class average.
# Write a program that checks if a number is even or odd using both a for loop and an if-else statement.
# Write a program that prints the first n Fibonacci numbers, where n is provided by the user.
