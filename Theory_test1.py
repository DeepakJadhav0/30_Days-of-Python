# 03_Day_Operators

# What is the difference between the == operator and the is operator in Python?
# == is used for to check is equal value and is used to check the memory locations are same or not

# How does the // operator differ from the / operator in Python?
# / is a floating division and // is int division
print(10//5)
print(10/5)

# What is the result of the expression 5 ** 2 and how does the ** operator work?
# ** is used to power of number
print(5**2) # 5^2

# Explain how the & (bitwise AND) operator differs from the and (logical AND) operator.
# & is bitwaise addition in binary and is used to logical comparision

# What is the purpose of the % (modulus) operator in Python?
# % is used as remainder in Python
print(5 % 2)

# How do you use the << and >> operators for bitwise shifting?
# SHiftes the binary number

# What does the not operator do, and how does it differ from !=?
# not operator is used to change true in flase and false is true and != is used to comaprasion operator
print(not True)

# How would you use the or operator in a conditional expression?
# or is a logical operator where used in two conditions if any one is true the statetement is true 

# What is the result of the expression 10 < 5 < 15 in Python?
print(10>5<15)

# Explain the use of the += operator and give an example.
# += is used to add previus value of same veriable maily used in loops it means addition itself

# 04_Day_Strings

# How can you concatenate two strings in Python?
# + is used to concatenate two string
print('Deepak'+' '+'Jadhav')

# What method would you use to check if a string contains a particular substring?
# in operator is used to check is substring present in string 
name = "Python is Great"
is_preset = "Python" in name

print(is_preset)

# How do you convert a string to a list of characters?
str1 = "india"
lst_str = list(str1)
print(lst_str)

# What is the result of using the strip() method on a string?
# strip() removes the charatcter given () from biggining and ending 
print(name.strip("Pta"))

# How do you format a string with variables in Python?
# There are several ways .format and f{} string
print("I am from {} and i love {}" .format(str1,name))
print(f"I am From {str1} and i love {name}")

# Explain the use of the join() method in string manipulation.
# caharater.join(in) add charachter given before every char in in 
print(' '.join(name))

# How can you find the length of a string?
# len() is usd for length of given string
print(len(name))

# How can you check if all characters in a string are digits?
# str.isalnum() is used to check all are string

# What does the split() method do, and how can it be used?
# .split() is used to split string into list
print(name.split(" "))

# ------------------------------------ 5_Day_Lists

# How do you add an item to the end of a list in Python?
# append() is used to insert elemnets in last of list 
lst = [10,20,30,40]
lst.append(20)
print(lst)

# What method would you use to remove the first occurrence of a value from a list?
# remove() is used to remove from Last
lst.remove(20)
print(lst)

# How can you access the last element of a list?
# usind -1 index 
print(lst[-1])

# What does the pop() method do, and how can it be used?
# pop()is used to remove last elemet in list 
lst.pop()
print(lst)

# How can you sort a list in ascending order?
# using sort() function a list can be sorted
lst2 = [30,40,10,28,30,22]
lst2.sort()
print(lst2)

# How do you reverse the order of elements in a list?
# usnig reverse() a ist can be reversed
lst.reverse()
print(lst)

# What is the difference between remove() and del statements when modifying lists?
# remove() is used to remove first occurane=ce of element and del is used to delet remove entire list 

# How can you check if a list is empty?
lst3 = []
is_empty = len(lst3) == 0
print(is_empty)

# How do you merge two lists into a single list?
# extend() function is used to extend or add another list 
lst.extend(lst2)
print(lst)

# ---------------------------------- 06_Day_Tuples
tpl = (10,20,30,40,50,60,70)
tpl2 = (80,90,100,110)

# How do tuples differ from lists in Python?
# tuples are unmutabe they can not be changed once added and are sortef duplicates are removed 

# What happens if you try to change an element of a tuple?
# we can not change elements in tuples

# How can you concatenate two tuples in Python?
# + is used to concenate tuples 
print(tpl + tpl2)

# What is the result of using the count() method on a tuple?
# used to count the number of occurance fo specific number in tuples
print(tpl.count(70))

# How do you access a specific element in a tuple?
# using index the elements in tuples can be accessed
print(tpl[0])

# Can you nest tuples within other tuples? Provide an example.
# yes we can 
nested_tuples = (
    (10,20,30),
    (30,40,50),
    (60,70,80)
)

print(nested_tuples[0])
print(nested_tuples[0][2])

# How do you unpack a tuple into separate variables?
a,b,*c = tpl2
print(a,b,*c)

# What is the purpose of using tuples instead of lists in Python?
# less memonry and unmutable , removes duolicate used the fixed small sixe data 

# How do you convert a list into a tuple?
# ny simply usnig list the tuples can be changed in lists
tpl_lst = list(tpl)
print(tpl_lst)

# What is the result of using the index() method on a tuple?
# index is used to get index of specific element in tuples 
print(tpl.index(20))

# --------------------------------------- 07_Day_Sets
st = {10,20,30,40,50,60,70}
st2 = {40,50,60,70}
st3 = {80,90,100,110}

# What is a set in Python and how is it different from a list?
# set is unordered, changeable , set operations line intersection and union 

# How do you perform a union operation on two sets?
# union() is used to perform union get all elements from both sets
is_union = st.union(st3)
print(is_union)

# What method would you use to remove a specific element from a set?
# .remove(specific elemt) is used to remove specific element from set 
st.remove(20)
print(st)

# How can you find the intersection of two sets?
# .intersection() is used oto get intersected elemetns from sets 
print(st.intersection(st2))

# What is the purpose of the difference() method in sets?
# .difference is used to know elemnets not in other 
diff_set = st.difference(st2)
print(diff_set)

# How can you add multiple elements to a set at once?
add_st = {100,110,120}
st.update(add_st)
print(st)

# What does the discard() method do, and how is it different from remove()?
# if discard is failes there is no error occurs in program not like remove 

# How do you check if one set is a subset of another?
# st.issubset() is used to chrck if the set is subset of other subset
print(st2.issubset(st))

# Explain how the symmetric_difference() method works.
# it returns bit elemts from both sets except elements present on both side 
print(st.symmetric_difference(st2))

# How can you create an empty set in Python?
set_name = {} or set()

# --------------------------------------- Dictionaries

# How do you define a dictionary in Python, and what are its key characteristics?
# dictonary is a built-in data structure in python which store values in keyand value pair 
# key is like poointer to specific value 

# Given the dictionary my_dict = {'a': 1, 'b': 2, 'c': 3}, how would you access the value associated with the key 'b'?
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['b'])
my_dict['b'] = 200
print(my_dict)

# If you want to check whether the key 'name' exists in the dictionary user_info = {'name': 'John', 'age': 30}, what would the code look like?
user_info = {'name': 'John', 'age': 30}
print('name' in user_info)

# Explain the difference between my_dict.get('key') and directly accessing my_dict['key']. What are the advantages of using get()?
# .get() arise eror if item is not found

# How can you add a new key-value pair to an existing dictionary?
my_dict['d'] = 20
print(my_dict)

my_dict = {'x': 10, 'y': 20, 'z': 30}
my_dict.pop('y')
print(my_dict)

# How do you iterate through both the keys and values of a dictionary at the same time?
for key, value in my_dict.items():
    print(f"{key} : {value}")

print(my_dict.items())

# What is dictionary comprehension, and how would you use it to create a dictionary with keys as numbers from 1 to 5 and their values as the square of the keys?
squares = {x: x**2 for x in range(1,6)}
print(squares)

# What method would you use to return all the key-value pairs of a dictionary as a list of tuples?
print(my_dict.keys())

# If my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}, how would you access the second element in the list associated with key 'a'?
my_dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6]}
print(my_dict1['a'][1])

# ------------------------------------ Conditions 

# What is the purpose of conditional statements in Python?
# conditions are used to get conditions before output in python 

# How do you write a basic if statement in Python?
# if (Condition):
    # statement 

a = 20
if a > 30:
    print("a is more than 10")

# What is the difference between if, elif, and else statements?
# if condition:
#     statement1
#     elif condition:
#         statement2 
#         else condition:
#             statement 3

# if condition works first even if is instilled elif is executed and if both are false else is executed 

# Explain what happens if none of the conditions in an if-elif-else chain is true.
# is none of condition are true else os executed  

# How would you write a conditional to check if a number is both greater than 10 and less than 20?
if a > 10:
    print("a is Greater tha 20")
elif a < 30:
    print("a is smaller than 10")

x = 5
if x > 10:
    print("Greater")
else:
    print("Smaller") # smaller

# How can you use nested if statements, and when might this be useful?
# if condition:
#     statement1
#     if condition:
#         statement2
# else:
#     statement3
#  it is use full in complex decisions like leaf year or notn 

# What is the difference between using == and is in conditionals?
# ==  is used to check equality of vslue stord in both datatypes and is is usd to check if the both are has same mation emory loac

# Write a conditional statement that checks if a number is even or odd.
# num = int(input())
# if num % 2 == 0:
#     print('even')
# elif num % 2 == 1:
#     print('odd')
# else:
#     print("invalid input")

# What is the shorthand for writing if-else statements in a single line, and how is it used?
number = 5
result = "pass" if number > 2 else "fail"
print(result)

# ------------------------------ loops

# What is the difference between a for loop and a while loop in Python?
# Use a for loop when you have a specific collection or number of iterations in mind.
# Use a while loop when you need to loop based on a condition that may not have a predefined end.

# How do you loop through all elements in a list using a for loop?
# for element in data_type is used to through all the elemnets in list

# What is an infinite loop, and how can you avoid it when writing a while loop?
# infinite loops means a loop which executes infinitly to avoid it writing in while make sure that the condition will false after interval of time 

count =0
while count < 10:
    count += 1
    if count == 5:
        continue
    print(count)
    