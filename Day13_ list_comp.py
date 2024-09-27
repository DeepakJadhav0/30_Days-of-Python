# ---------------------------------- List Comprehension

# [i for i in iterable if expression]

# language = 'python'
# # lst = list(language)
# # print(lst)

# lst = [i for i in language]
# print(lst)

# number = [i*i for i in range(11)]
# print(number)

# odd_numbers = [i for i in range(11) if i % 3 == 0]
# print(odd_numbers)

# tuples = [(i, i*i) for i in range(11)]
# print(tuples)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [i for row in list_of_lists for i in row]
print(flat)

# ---------------------------------- EXERCISE 1
#1 Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative = [i for i in numbers if i < 0]
positve = [ i for i in numbers if i >= 0]
print(positve)

#2 Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dem = [i for rows in list_of_lists for row in rows for i in row]
print(one_dem)

#3 Using list comprehension create the following list of tuples:

tuple_list = [(i,1,i,i**2,i**3,i**4,i**5,i**6) for i in range(11)]
print(tuple_list)

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

#4 Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [[country.upper(), country[:3].upper(), capital.upper()] for [[country, capital]] in countries]
print(result)

#5 Change the following list to a list of dictionaries:
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

new_result = [{"country":country.upper(),"city":city.upper() }for[[country,city]] in countries]
print(new_result)

#6 Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names = [first_name +" "+ last_name for [(first_name,last_name)] in names]
print(new_names)

# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']