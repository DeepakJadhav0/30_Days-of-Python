# # ----------------------LOOPS - 1. While 2.For
# # While Loop - until condition is False
# # while condition:
# #     code

# a = 0
# while a < 5:
#     print("Hellow world")
#     a += 1

# # while condition:
# #     code
# # else:
# #     code 

# b = 0
# while b < 5:
#     print("yes!")
#     b += 1
# else:
#     print("Last time")

# # Break and Continue - Part 1 - Break and coutinue is used 
# # break is used if we want to stop the loop

# # while condition:
# #     code
# #     if condition:
# #         break

# c = 0
# while c < 5:
#     print(c)
#     c += 1
#     if c == 3:
#         break

# # continue is used to skip the and continue

# # while condition:
# #     code
# #     if condition:
# #         continue

# d = 0
# while d < 5:
#     if d == 2:
#         d += 1
#         continue
#     print(d)
#     d += 1

# # For Loop -  for is used 
# # for condition: till the condition is true loops repeats
# #     code

# # for loops with list
# num = [1,2,3,4,5,6]
# for number in num:
#     print(number)

# # for loop with string
# language = "Python"
# for letter in language:
#     print(letter)

# for i in range(len(language)):
#     print(language[i])


# ------------------------------------ EXERCISE 1

#1 Iterate 0 to 10 using for loop, do the same using while loop.
num1 = 0
for i in range(11):
    print(i)

while num1 < 11:
    print(num1)
    num1 += 1

#2 Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,0,-1):
    print(i)

num2 = 10
while num2 > 0:
    print(num2)
    num2 -= 1

#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(7):
    print("#"*i)

#4 Use nested loops to create the following:
for i in range(8):
    for j in range(8):
        print("#",end=' ')
    print()

#5 Print the following pattern:
for i in range(11):
    print(i,"x",i,'=' ,(i*i))

#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ["Python","NUmpy","Pandas","Django","Flask"]
for i in range(len(lst)):
    print(lst[i])

#7 Use for loop to iterate from 0 to 20 and print only even numbers
Even_lst = []
for i in range(0,20,2):
    Even_lst.append(i)

print(Even_lst)

odd_lst = []
for i in range(1,100,2):
    odd_lst.append(i)

print(odd_lst)

# ----------------------------------------- EXERCISE 2

#1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(101):
    sum += i

print("sum of 1 to 100 is ",sum)

#2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odd
sum_even = 0
sum_odd = 0
for i in range(0,100,2):
    sum_even += i

print("Sum of 1 to 100 odd numbe is :",sum_even)

for j in odd_lst:
    sum_odd += j

print(sum_odd)

# ------------------------------------- EXErCISE 3

#1 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana','orange','mango','lemon']
rev_fruits = []
for i in range(len(fruits)):
    rev_fruits.append(fruits.pop())

print(rev_fruits)