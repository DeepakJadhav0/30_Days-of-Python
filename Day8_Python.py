# ----------------------------------- DICTIONARY - dict {} or {"key":"values"}

# Creating a Dictionary - {} is used for create dictionary it may contai = string ,list ,tuples, key&values
empty_dict = {}
dct = {"key1":"Value","key2":"Value2","key3":"value3"}
print(dct)

first_person = {'First Name':'Deepak',
'middle Name':'Mahadev',
'last Name':'jadhav',
'age':21,
'country':'Indai',
'is_married':True,
'skills':["React","Node","express","HTML","CSS","JAVASCRIPT","Python","mongodb"],
'address':{'street':'A/p Hasurchamopu','Tal':'Gadhinglaj','dict':'Kolhapur'}
}
print(first_person)

# Dictionary Length - len() is used to length 
print(len(first_person))

# Accessing Dictionary Items - by refering the key dict{['key']}
print(first_person['skills'])

# Adding Items to a Dictionary - dict['key'] = 'value' 
first_person['Job'] = 'Programmer ML'
print(first_person)

# Modifying Items in a Dictionary - we can just Overwrite on existing key value
first_person['First Name'] = 'Rohan'
print(first_person)

# Modifying Items in a Dictionary - in operator is used to check in dict 
is_check = 'skills' in first_person
print(is_check)

# Removing Key and Value Pairs from a Dictionary - pop(key) or popitem() for last item to remove 
first_person.pop('Job')
first_person.popitem()

# Changing Dictionary to a List of Items - .item() is used to change in tuple of list 
lst_first_person = first_person.items()
print(lst_first_person)

# Clearing a Dictionary - clear() is used 
# lst_first_person.clear()

# Deleting a Dictionary - del is used to delet 
# del first_person

# Copy a Dictionary - copy() is used to copy
dopy_first_person = first_person.copy()
print(dopy_first_person)

# Getting Dictionary Keys as a List - keys() is used to get list of keys 
print(first_person.keys())

# Getting Dictionary Values as a List - values() is used to get only values 
print(first_person.values())

# -------------------------------------------- EXERCISE 1

#1 Create an empty dictionary called dog
dog = {}

#2 Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'lucy','color':'brown','breed':'German shepad','legs':5,'age':10}
print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dict = {'first_name':'emily','last_name':'wick','Gender':'Female','is_married':False,'age':22,'skills':['react','angular','mongodb','mysql','c++'],'country':'India'}
print(student_dict)

#4 Get the length of the student dictionary 
print("length od dict is :",len(student_dict))

#5 Get the value of skills and check the data type, it should be a list
print(type(student_dict['skills']))

#6 Modify the skills values by adding one or two skills
student_dict['skills'].append('DSA')
print(student_dict['skills'])

#7 Get the dictionary keys as a list
print(student_dict.keys())

#8 Get the dictionary values as a list
print(student_dict.values())

#9 Change the dictionary to a list of tuples using items() method
lst_student_dict = student_dict.items()
print(lst_student_dict)

#10 Delete one of the items in the dictionary
student_dict.popitem()

#11 Delete one of the dictionaries
del student_dict