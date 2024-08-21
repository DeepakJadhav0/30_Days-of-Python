# --------------------------------------------FUNCTIONS
# Defining a Function - function is defined using def keyword
# Declaring and Calling a Function
# def function_name():
#     code
#     code

# function_name() here function is called

# Function without Parameters - function_name() only
# def Student_name():
#     first_name = "Deepak"
#     last_name = "Jadhav"
#     full_name = first_name + " " + last_name
#     print(full_name)

# Student_name()

# def add_two_num():
#     num = 12
#     num1 = 22
#     sum = num + num1
#     print(sum)

# add_two_num()

# Function Returning a Value - Part 1
# def Student_name():
#     first_name = "Deepak"
#     last_name = "Jadhav"
#     full_name = first_name + " " + last_name
#     return full_name

# print(Student_name())

# def add_two_num():
#     num = 12
#     num1 = 22
#     sum = num + num1
#     return sum

# Function with Parameters 
# def greeting(name):
#     meaage = name + "Nice To meet You"
#     return meaage
# print(greeting('Deepak'))

# def Area_circle(radius):
#     PI = 3.14
#     area = PI * radius ** 2
#     return area

# radius = int(input("ENter RAdisu of circle "))
# print(Area_circle(radius))

# two Parameters 
# def sum_if_two(num1,num2):
#     sum = num1 + num2
#     return sum

# num1 = int(input("Enter num 1:"))
# num2 = int(input("Enter num 2:"))

# print(f"sum of {num1} and {num2} is {sum_if_two(num1,num2)}")

# def age_calculator(current,birth):
#     age = current - birth
#     return age

# current = int(input("enter current Year :"))
# birth = int(input("Enter Your Birth Year :"))

# print(f"Your Current age is {age_calculator(current,birth)}")

# Passing Arguments with Key and Value
# def full_name(first_name,last_name):
#     f_name = first_name +" "+ last_name
#     return f_name

# print(f"Welcome {full_name(first_name='Deepak',last_name='JAdhav')} to Learning Python")

# ----------------------------------- EXERCISE 1
#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def add_two_numbers(num1,num2):
#     sum = num1 + num2
#     return sum

# print("Sum of numbers is ",add_two_numbers(20,30))

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle(r):
#     area = 3.14*r*r
#     return area

# print("Area of Circle is :",(area_of_circle(15)))

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# def add_all_nums(*nums):
#     sum = 0
#     for num in nums:
#         if num == type(sum):
#             print("Invalid input")
#         sum = sum + num
    
#     return sum

# print(add_all_nums(20,30,32,23))

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit
# def convert_celcius_to_Fahrenhite(celcius):
#     fahrenheit = (celcius * 9/5) + 32
#     return fahrenheit

# celcius = int(input("Enter Temp in Celcius :"))
# print(f"{celcius} in fahermite is {convert_celcius_to_Fahrenhite(celcius)}")

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month == "january" or month == "Febuery" or month == "March":
        season = "summer"
    elif month == "April" or month == "May" or month == "June":
        season = "winter"
    return season

print(check_season(month="january"))