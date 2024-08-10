# --------------------------------- SET - {"item1","item2"} {} are used in set

# Creating a Set - set() or {} used
# st = set() or
st = {"item","item1","item2","item3"}

# Getting Set's Length - len() is used
print(len(st))

# Checking an Item - in opertator is used 
print("item" in st)

# Adding Items to a Set - add() is used for single add and update([]) is used for many 
st.add("item4")
print(st)

st.update(["item5","item6","item7","item8"])
print(st)

# Removing Items from a Set - remove("item_name") or pop() for Random are used 
st.remove("item")
print(st)

st.pop()
print(st)

# Clearing Items in a Set - clear() is Used 
# st.clear()
print(st)

# converting List to Set - set()(removes duplicates) and list()(can be ordered) are used 
lst = ["num1","num2","num3","num4","num5"]
st_list = set(lst)
print(st_list)

lst_st = list(st_list)
print(lst_st)

# Joining Sets - union() or update() are used
full_st = st.union(st_list)
print(full_st)

st.update(st_list)
print(st)

# Finding Intersection Items - set.intersection() is used 
st1 = {"num2","num8","num1","num5","num7"}
print(st_list.intersection(st1))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))

# Checking Subset and Super Set - issubset() or issuperset() are used 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1))
print(st1.issuperset(st2))

# Checking the Difference Between Two Sets - set1.Difference(set1) is used set1/set2
print(st1.difference(st2))

# Finding Symmetric Difference Between Two Sets - set.symmetric_difference() is used to get rather than common 
print(st1.symmetric_difference(st2))

# Joining Sets - if tow set are no commen they are called using isdisjoin()
print(st1.isdisjoint(st2))

# ------------------------------------------- EXERCISE 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1 Find the length of the set it_companies
print("length of it_companies is :",len(it_companies))

#2 Add 'Twitter' to it_companies
it_companies.add("twitter")
print(it_companies)

#3 Insert multiple IT companies at once to the set it_companies
it_companies.update(["TCS","Tech Mahindra","Infosys","Conqiate"])
print(it_companies)

#4 Remove one of the companies from the set it_companies
it_companies.pop()

#5 What is the difference between remove and discard
# when we use remove() is item is not exists it giver error and discard() does'nt

# ---------------------------------- EXERCISE 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1 Join A and B
C = A.union(B)
print(C)

#2 Find A intersection B
print(A.intersection(B))

#3 Is A subset of B
print(A.issubset(B))

#4 Are A and B disjoint sets
print(A.isdisjoint(B))

#5 Join A with B and B with A
# A.update(B)
# B.update(A)
# print(A)
# print(B)

#6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#7 Delete the sets completely
del A
del B

# ----------------------------------------------EXERCISE 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
st_age = set(age)
print(st_age)

#2 Explain the difference between the following data types: string, list, tuple and set
# string - sring are collect of characters represented usnig ("")
# list - list are collection of datatypes represented using ["item","item1"]
# tuple - tuple are unmodifiable collect of similar datatypes ("item","item1")
# set - is Unordred and unindexed colllection represented using {"item1","item2"}

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
print(sentence.split())

st_sentence = set(sentence.split())
print(st_sentence)