# ----------------------------- list 

# How to Create a List
# List_name = [] here [] brackets are used for creating lists

# Accessing List Items Using Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)  

#similarly we can use Negative numbers for revert indexing

#Unpacking List Items
# we use variable for unpack the list 
fitem,sitem,titem, * rest = fruits
print(fitem)
print(sitem)
print(titem)
print(rest)

# Slicing Items from a List
# List-name[start:till]
print([fruits[1:3]])

# Modifying Lists
# we overwrite the ist to modify
fruits[1] = "Watermellon"
print(fruits)

# Checking Items in a List - in opertator is used to checking item in list
is_fruit = "mango" in fruits
print(is_fruit)

# Adding Items to a List - append() is used to insert at last and instert(index,item) is used to add any indexed place
fruits.append("strawberrary")
print(fruits)

fruits.insert(1,"custudapple")
print(fruits)

# emoving Items from a List - we can remove using list_name.remove("item_name")
fruits.remove("mango")
print(fruits)

# Removing Items Using Pop pop(index)
fruits.pop(3)
print(fruits)

# Clearing List Items clear() is used to clear string

# Copying a List copy() is used to copy 
fruits_copy = fruits.copy()
print(fruits_copy)

# Counting Items in a List - count() is used to count item repeated in list
print(fruits.count('mango'))

# Joining Lists - + or extend() are used to jion lists
num1 = [1,2,3]
num2 = [4,5,6]
num3 = num1 + num2
num1.extend(num2)
print(num3)
print(num1)

# Finding Index of an Item - is unsed to get index of item or items index
# print(fruits.index("mango"))

# Reversing a List - revers is used to reverce the list 

# Sorting List Items - sort() is used to sort in ascending and sort(reverse=true) for decending to ascinding
# num1.sort(reverse=True)
# print(num1)
print(sorted(num1,reverse=True))

#------------------------------------------------------------------- EXERCISE
#1 Declare an empty list
lst1 = [] 

#2 Declare a list with more than 5 items
lst1 = ['mango','apple','banana','orange','watermellon']
print(lst1)

#3 Find the length of your list
print("length of list is ;",len(lst1))

#4 Get the first item, the middle item and the last item of the list
first_item = lst1[0]
middle_item = len(lst1) // 2
last_item = lst1[-1]

print(first_item,lst1[middle_item],last_item)

#3 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type = ["Deepak", 21, 5.5, "Not MArried", 'a/p Hasurchampu']

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["facebook","Google","Microsoft","apple","IBM","Oracle","Amazon"]

#7 Print the list using print()
print(it_companies)

#8 Print the number of companies in the list
print(len(it_companies))

#9 Print the first, middle and last company
first_com = it_companies[0]
middle_com = len(it_companies) // 2
last_com = it_companies[-1]

print(first_com,it_companies[middle_com],last_com)

#10 Print the list after modifying one of the companies
it_companies[2] = "Flipkart"

#11 Add an IT company to it_companies
it_companies.append("Microsoft")
print(it_companies)

#12 Insert an IT company in the middle of the companies list
it_companies.insert(middle_com,"TCS")
print(it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!
upper_com = it_companies[2].upper
print(it_companies)

#14 Join the it_companies with a string '#;  '


#15 Check if a certain company exists in the it_companies list.
exist_in = "TCS" in it_companies
print(exist_in)

#16 Sort the list using sort() method
numbers = [2,4,3,6,7,8,1,0]
print(sorted(numbers))

#17 Reverse the list in descending order using reverse() method
numbers.reverse()
print(numbers)

#18 Slice out the first 3 companies from the list
print(it_companies[0:3])

#19 Slice out the last 3 companies from the list
print(it_companies[::-3])

#20 Slice out the middle IT company or companies from the list
print(it_companies[middle_com])

#21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#22 Remove the middle IT company or companies from the list
middle_c = len(it_companies) // 2
it_companies.pop(middle_c)
print(it_companies)

#23 Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#24 Remove all IT companies from the list
# it_companies.clear()
# print(it_companies)

#25 Destroy the IT companies list - del list_name is used 

#26Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# type 1 
full_stack = front_end + back_end
print(full_stack)

# type 2 id if have to add in single
# front_end.extend(back_end)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
insert_index = full_stack.index("Redux") + 1
full_stack.insert(insert_index,"Python")
full_stack.insert(insert_index + 1,"Sql")
print(full_stack)
