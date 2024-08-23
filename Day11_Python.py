import statistics
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
# def check_season(month):
#     if month == "january" or month == "Febuery" or month == "March":
#         season = "summer"
#     elif month == "April" or month == "May" or month == "June":
#         season = "winter"
#     return season

# print(check_season(month="january"))

#6 Write a function called calculate_slope which return the slope of a linear equation
# def calculate_slope(x1,x2,y1,y2):
#     if y1 == x1:
#         return None
#     m = y2 - y1 / x2 - x1
#     return m

# print(calculate_slope(3,5,6,3))

#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def print_list(lst):
#     for n in lst:
#         print(n)

# print_list(lst=[23,4,21,23,55,32,32,11,22,32])

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# def reverse_list(lst):
#     reversed_array = []
#     for element in lst[::-1]:
#         reversed_array.append(element)
#     return reversed_array

# lst = [23,23,2,3,44,24,24,24,56,44,31]
# print(reverse_list(lst))

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# def capitalize_list_items(fruits_lst):
#     capitalize_list = []
#     for item in fruits_lst:
#         capitalize_list.append(item.upper())

#     return capitalize_list
# fruits_lst = ["mango","Orange","Watermellon","Apple","Pineapple"]

# print(capitalize_list_items(fruits_lst))

#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# def add_item(lst,item):
#     updated_list = lst.copy()
#     updated_list.append(item)
#     print(updated_list)

# lst = list(input("Fruits :").split())
# item = input("Enter item:")
# print(add_item(lst,item))

#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# def add_item(lst,item):
#     lst.append(item)
#     return lst

# def remove_item(lst,item):
#     lst.remove(item)
#     return lst
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# numbers = [2, 3, 7, 9]

# print(remove_item(numbers,7))

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# def sum_of_numbers(n):
#    return sum(range(1,n+1))

# print(sum_of_numbers(10))

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def sum_of_odds(n):
#     return sum(range(1,n+1,2))

# print(sum_of_odds(10))
#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def sum_of_even(n):
#     return sum(range(0,n+1,2))

# print(sum_of_even(10))

# ------------------------------------------EXERCISE 2

#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# def evens_and_odds(n):
#     even = 0
#     odd = 0
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print("Number of Even are:",even)
#     print("Number of Odds:",odd)

# evens_and_odds(100)

#2 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact

# print(factorial(3))

#3 Call your function is_empty, it takes a parameter and it checks if it is empty or not
# def is_empty(data):
#     return len(data) == 0

# print(is_empty([]))

#4 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# def calculate_mean(data):
#     return statistics.mean(data)
    

# def calculate_median(data):
#     return statistics.median(data)

# data = [3,2,3,4,2,3,4,2,1,4,4]

# print(calculate_mean(data))
# print(calculate_median(data))

# --------------------------------- EXERCISE 3
#1 Write a function called is_prime, which checks if a number is prime.

# def is_prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return "Not Primr"
#         else:
#             return "is Prime"

# print("the number is",is_prime(3))

#2 Write a functions which checks if all items are unique in the list.
# def is_unique(lst):
#     if len(lst) == len(set(lst)):
#         return True
#     else:
#         return False

# def is_unique(lst):
#     for i in range(len(lst)):
#         for j in range(i+1,len(lst)):
#             if lst[i] == lst[j]:
#                 return False
#     return True

# lst = [1,2,3,4,5,6,7,8,3]
# print(is_unique(lst))
    
#3 Write a function which checks if all the items of the list are of the same data type.
# def same_datatype(data):
#     for i in range(len(data)):
#         if type(data[0]) != type(data[i]):
#             return False
#     return True
    
# lst =[1,3,2,3,4,5,3,4,2]
# print(same_datatype(lst))

#4 Write a function which check if provided variable is a valid python variable
# def is_valid_variable(var_name):
#     # Use Python's built-in identifier check
#     return var_name.isidentifier()

# # Example usage:
# print(is_valid_variable("valid_name"))  # Output: True
# print(is_valid_variable("2invalid_name"))  # Output: False
# print(is_valid_variable("invalid-name"))  # Output: False
 