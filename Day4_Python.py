# --------------------------- STRINGS
# Creating a String
str1 = "Iten_name"

# String Concatenation - + operator is used to concatention
str2 = "object_name"
str3 = str1 + str2
print(str3)

# Escape Sequences in Strings
# \n is used for new line
# \t is used for add tabs
# \\ adds Backslash

print("This is A Escape Sequal \n")
print("This is another escape \t sequal")
print("this is a blackslash \\")

# Python Strings as Sequences of Characters - unpacking
language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)

# Accessing Characters in Strings by Index - accesed using index string_name[index]
print(language[1])

# Slicing Python Strings - string slicing has also same process string_name[strat:end:skip]
print(language[0:3])

# #1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = "Thirty "
str2 = "Days "
str3 = "Of "
str4 = "Python"

sentence = str1 + str2 + str3 + str4
print(sentence)

 #2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str1 = "Coding "
str2 = "For "
str3 = "All"

sentence = str1 + str2 + str3
print(sentence)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding for all"

#4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
print("length of string is " , len(company))

#6 Change all the characters to uppercase letters using upper() method.
upp_char = company.upper()
print(upp_char)

#7 Change all the characters to lowercase letters using lower() method.
low_case = company.lower()
print(low_case)

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.swapcase())
print(company.title())

#9 Cut(slice) out the first word of Coding For All string.
word = company.split()
print(word[0])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
Word = 'Coding'

contain_word = Word in company
print(contain_word)

#11 Replace the word coding in the string 'Coding For All' to Python.
rep = company.replace("Coding" , "python")
print(rep)

#12 Change Python for Everyone to Python for All using the replace method or other methods.
print(rep.replace("all","Everyone"))

#13 Split the string 'Coding For All' using space as the separator (split()).
print(company.split(" "))

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
sen = "Facebook,Google,Mivrosoft,Apple,Oracle,Amazon"
print(sen.split(","))

#15 What is the character at index 0 in the string Coding For All.
print(company[0])

#16 What is the last index of the string Coding For All.
print(company[-1])

#17 What is the last index of the string Coding For All.
print(company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
word1 = company.split()

#20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
# print(company.index('F'))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence1 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence1.index('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence1  .rindex('because'))

# ------------------------- PROJECT ------------------------------
# Write a Python program that calculates how much each person should pay when a group of people decides to split a bill and leave a tip. The program should:

# Prompt the user to enter the total bill amount.
# Prompt the user to enter the percentage of tip they would like to give (10, 20, or 30).
# Prompt the user to enter the number of people among whom the bill will be split.
# Calculate the total tip amount based on the percentage provided.
# Calculate how much each person should pay by dividing the total tip amount by the number of people.


print("Welcome To Tip Calculator ")
total_bill = int(input("Enter Total Bill amount:"))
per = int(input("Enter The Percentage of tip from bill like 10,20 or 30 :"))
no_people = int(input("Enter The Number of People bill to be spilt :"))

total_tip = total_bill * per / 100
tip = total_tip / no_people
print(f"Total bill Each Should Pay is :{tip}")