# In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:
from functools import reduce
from countries import countries

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

# Function as parameter 
# def sum_numbers(nums):
#     return sum(nums)

# def higher_order_function(f,lst):
#     summation = f(lst)
#     return summation

# print(higher_order_function(sum_numbers,[1,2,3,4,5]))

# Function as Return value
# def square(x):
#     return x**2

# def cube(x):
#     return x**3

# def absulute(x):
#     if x > 0:
#         return x
#     else:
#         return  -(x)

# def higher_order_function(type):
#     if type == "square":
#         return square
#     elif type == "cube":
#         return cube
#     elif type == "abolute":
#         return absulute
    
# result = higher_order_function('square')
# print(result(3))
# result = higher_order_function('cube')
# print(result(10))
# result = higher_order_function('abolute')
# print(result(-10))

# def greeting():
#     return "Python is best language of all"

# def upper_case(greeting):
#     def wrapper():
#         func = greeting()
#         upper_func = func.upper()
#         return upper_func
#     return wrapper

# new = upper_case(greeting)
# print(new())

# ------------------- MAP 
# map(function,itration)

# names = ['Deepak','mahadev','jadhav']

# def change_to_upper(name):
#     return name.upper()

# names_in_upper = map(change_to_upper,names)
# print(list(names_in_upper))

# def square(x):
#     return x**2

# lst = [1,2,3,4,5]
# squred_list = map(square,lst)
# print(list(squred_list))

# lst = ['1','2','3','4']
# numder_int = map(int,lst)
# print(list(numder_int))

# ----------------- filter
# it basicalyy get the true boolen itrations 
# filter(function,itrations)

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# numbers = [1,2,3,4,5,6,7,8,9]
# only_even = filter(is_even,numbers)
# print(list(only_even))

# names = ['Asabeneh', 'Lidaaaya', 'Ermias', 'Abraham']
# def is_long_name(name):
#     if len(name)>7:
#         return True
#     return False

# long_names = filter(is_long_name,names)
# print(list(long_names))

# ------------------------------ EXERCISE 1

countriesy = ['Estonia', 'Finland', 'ESweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1 Explain the difference between map, filter, and reduce.
# map() is used to aplly given function to every itration given 
# filter() is used to fileter the itration according to conditions 
# reduce() is used to reduce itration and to aggration 

# numbers = [1,2,3,4,5,6,7]
# result = reduce(lambda x: x**2 ,numbers)
# print(result)

#2 Use for loop to print each country in the countries list.
# for i in countries:
#     print(i)

#3 Use for to print each name in the names list.
# for i in names:
#     print(i)

#4 Use for to print each number in the numbers list.
# for i in numbers:
#     print(i)

# --------------------------- EXERCISE 2

#1 Use map to create a new list by changing each country to uppercase in the countries list
# def upper_case(country):
#     return country.upper()

# upper_case_country = map(upper_case,countries)
# print(list(upper_case_country))

#2 Use map to create a new list by changing each number to its square in the numbers list
# def square(num):
#     return num**2

# square_numbers = map(square,numbers)
# print(list(square_numbers))

#3 Use map to change each name to uppercase in the names list
# def upper_case(name):
#     return name.upper()

# names_upper = map(upper_case,names)
# print(list(names_upper))

#4 Use filter to filter out countries containing 'land'.
# def is_land(country):
#     if 'land' in country:
#         return True
#     return False

# filtered_countries = filter(is_land,countries)
# print(list(filtered_countries))

# 5 Use filter to filter out countries having exactly six characters.
# def six_char(country):
#     if len(country) == 6:
#         return True
#     return False

# six_chararcters = filter(six_char,countries)
# print(list(six_chararcters))

#6 Use filter to filter out countries containing six letters and more in the country list.
# def more_thansix(country):
#     if len(country) > 6:
#         return True
#     return False

# more_than_six = filter(more_thansix,countries)
# print(list(more_than_six))

#7 Use filter to filter out countries starting with an 'E'
# def starting_E(country):
#     return country.startswith('E')

# starting_withE = filter(starting_E,countries)
# print(list(starting_withE))

#8 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# mixed_list = [1, "apple", 3.14, "banana", True, "cherry", 42]

# def is_string(element):
#     if type(element) is str:
#         return True
#     return False

# str_list = filter(is_string,mixed_list)
# print(list(str_list))

#9 Use reduce to sum all the numbers in the numbers list.
# def sum_is(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total

# print(sum_is(numbers))

#10 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# def country_land(country):
#     if 'land' in country:
#         return True
#     return False

# country_with_land = filter(country_land,countries)
# print(list(country_with_land))

def country_ia(country):
    if 'island' in country:
        return True
    return False

country_with_ia = filter(country_ia,countries)
print(list(countries))

def country_island(country):
    if 'island' in country:
        return True
    return False

country_with_island = filter(country_island,countries)
print(list(country_with_island))
# def country_stan()