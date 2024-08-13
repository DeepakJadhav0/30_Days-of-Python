# ------------------------------------------ Conditionals - if ,elif ,else

# if condition:
#     if the condition is true thab this statement is exicuted)

a = 20
if a > 10:
    print("Hellow World")


# if condition:
#     is the above is true this statement is executed)
# else :
#     is none of above is executed this statement is executed)

if a > 21:
    print("Statement 1 is executed")
else:
    print("Statement 2 is executed")

# if condition1:
#     if condition 1 is true this statementis executed
# elif condition2:
#     if condtion 1 is not true check for cndition 2 is it is true this statement is executed
# else:
#     if anyof above is true this is executed

if a > 30:
    print("statement 1 is executed")
elif a < 30:
    print("this statement 2 is executed")
else:
    print("statement 3 is executed")

# Short Hand - if statement is fitted in single line 
# code if condition else code 

print("A is positive") if a == 20 else print("none is true")

# Nested Conditions - if inside if
# if condition:
#     code
#     if condition:
#         code


if a > 10:
    if a > 20:
        print("a is bigger")
    

# ------------------------------------------ EXERCISE 1

# #1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# age = int(input("Enter Your Age :"))
# if age > 18:
#     print("You are Old enough to drive")
# else:
#     print(f"You still have to wait {18 - age} years")

# 2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# my_age = 22
# your_age = int(input("Enter Your Age :"))
# age_diff = my_age - your_age
# if my_age > your_age:

#     print(f" I am {my_age - your_age} years older than You")

# #3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# a = int(input("Enter a :"))
# b = int(input("Enter b :"))

# if a > b:
#     print("a is greater than b")
# elif a == b:
#     print('a nd b are equal')
# else:
#     print("b is greater than a")

# ------------------------------------- EXERCISE 2

#1 Write a code which gives grade to students according to theirs scores:

# marks = int(input("Enter Your score :"))
# if marks >= 80:
#     print("A Grade")
# elif marks >= 70:
#     print("B Grade")
# elif marks >= 60:
#     print("C Grade")
# elif marks >= 50:
#     print("D Grade")
# elif marks <= 50:
#     print("F Grade")
# else:
#     print("invalid inputn")

#2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

# month = input("Enter Month :")
# if month == 'September' or month == 'October' or month == 'November':
#     print('Season is Autumn')
# elif month == 'December' or month == 'January' or month == 'February':
#     print("Season is Winter")
# elif month == 'March' or month == 'April' or month == 'May':
#     print("Season is Spring")
# elif month == 'June' or month == 'July' or month == 'August':
#     print("Season is Summer")
# else:
#     print("invalid input")

#3 The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

# fruits = ['banana', 'orange', 'mango', 'lemon']
# in_list = input("Enter Fruit :")
# if in_list in fruits:
#     print('That fruit is alreasy exists in list')
#     print(fruits)
# else:
#     fruits.append(in_list)
#     print("successfully add in list")
#     print(fruits)


# --------------------------------- EXERCISE 3

#1 Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name':'Deepak',
    'last_name':"Jadhav",
    'age': 21,
    'gender':'male',
    'country':'india',
    'marial_status':False,
    'skills':['react','monogdb','node','javascript','python'],
    'address':{
        'village':'Hasurchampu',
        'pin': 426501
    }
}
print(person)

#1 Check if the person dictionary has skills key, if so print out the middle skill in the skills list

if 'skills' in person:
    print(person['skills'][len(person['skills']) // 2])
else:
    print("Enter skills")

#2 Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills'in person:
    if 'python' in person['skills']:
        print("Is a Python developer")

#3 the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person['marial_status'] == True:
    print(f"{person['first_name'],person['last_name']} Lives in {person['country']}, He is Married")
elif person['marial_status'] == False:
    print(f"{person['first_name']} {person['last_name']} Lives in {person['country']}, He is UnMarried")