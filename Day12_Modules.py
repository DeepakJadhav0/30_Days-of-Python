# ---------------------------- Modules
# What is a Module - module is set of code which are imported from another file

# Creating a Module
# mymodule.py
# def full_name(first_name,last_name):
#     full = (first_name + ' ' + last_name)
#     return full

# importing a Module - import keyword is used for importing from another file
# import moduletest

# print(moduletest.full_name('deepak','jadhav'))

# Import Functions from a Module - from keyword is used for import specific function
# from moduletest import full_name,gravity,person,sum_of_numbers
# print(sum_of_numbers(34,44))
# print(full_name('harry','macqueen'))
# mass = 100
# weight = mass * gravity
# print(weight)
# print(person['country'])

# Import Functions from a Module and Renaming -  we can rename using as 
# from moduletest import sum_of_numbers as total,person as p,gravity as g

# print(total(10,20))
# print(g)
# print(p['city'])

# mport Built-in Modules
# OS Module

import os
# create a dicractory
# os.mkdir('test_sub')

# changing file path
# os.chdir('test_sub')

# getting currnt workin g dicractory\
# os.getcwd()

# removing directory
# os.rmdir('test_sub')

# Statistics Module
# import statistics
# ages = [12,32,4,23,43,23,12,42,53,23,12,33]

# print(statistics.mean(ages))
# print(statistics.median(ages))
# print(statistics.mode(ages))

# Math Module
# import math
# print(math.pi)           # 3.141592653589793, pi constant
# print(math.sqrt(2))      # 1.4142135623730951, square root
# print(math.pow(2, 3))    # 8.0, exponential function
# print(math.floor(9.81))  # 9, rounding to the lowest
# print(math.ceil(9.81))   # 10, rounding to the highest
# print(math.log10(100))

# ------------------------------------ EXERCISE 1
#1 Writ a function which generates a six digit/character random_user_id
import random
import string

# def random_user_id():
#     character = string.ascii_letters + string.digits
#     user_id =''.join(random.choice(character) for _ in range(size))

#     # for i  in range(size):
#     #     user_id += random.choice(character)

#     return user_id

# size = 10
# print(random_user_id())

#2nModify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user(times,limit):
    character = string.ascii_letters + string.digits
    user_id_gens = []

    for i in range(times):
        user_id_gen = ''
        for _ in range(limit):
            user_id_gen += random.choice(character)


    return user_id_gen

print(user_id_gen_by_user(times=12,limit=5))