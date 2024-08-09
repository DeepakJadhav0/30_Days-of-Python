# ------------------- tuples - tuples() unchangeable
# Creating a Tuple - () are used to create tuples
fruits = ("mango","Orange","apple","Pineapple","Guava","Watermellon") 
print(fruits)

# Tuple length - Using Len()
print(len(fruits))

# Accessing Tuple Items - ising Tuple_name[index] 
print(fruits[1])

# Slicing tuples - slice tuple in sub-tuple using tuple_name[start:end]
print(fruits[::-1])

# Changing Tuples to Lists - to make change in tuple we must convert it into list 
List_fruit = list(fruits)
print(List_fruit)

# Checking an Item in a Tuple - in operator is used to check 
is_check = "mango" in fruits
print(is_check)

# Joining Tuples -  we use + operator to join two tuples 
num1 = (1,2,3,4,5,6)
num2 = (7,8,9,10,11,12)
num3 = num1 + num2
print(num3)

# ------------------------------------------------------ EXERCISE 1

#1 Create an empty tuple
numbers = ()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("john" , "smith" , "virat", "willims", "luck")
sister = ("ava" , "emily", "swift", "erik")

#3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sister
print(siblings)

#4 How many siblings do you have?
print("Total Siblings are ", len(siblings))

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Johhn","Maria")
family_members = siblings + parents
print(family_members)
# ------------------------------------------------------EXERCISE 2

#1 Unpack siblings and parents from family_members
*siblings , father , mother = family_members
print(siblings)
print(parents)

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits_product = ("apple","mango","Orange","Kivi")
vegetables_product = ("tomatoo","Potato","bringle","Corn")
animal_products = ("eggs","leather","meat")

food_stuff_tp = fruits_product + vegetables_product + animal_products
print(food_stuff_tp)

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = len(food_stuff_lt) // 2
print(food_stuff_lt[middle_item])

#5 Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

#6 Delete the food_staff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
is_Estonia = "Estonia" in nordic_countries
print(is_Estonia)

# Check if 'Iceland' is a nordic country
is_Iceland = "Iceland" in nordic_countries
print(is_Iceland)