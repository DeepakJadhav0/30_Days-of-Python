# # 1. Introduction to Python
# # Question: What will be the output of the following code and why?

# print(type(5/2)) # float single / is a floating point division
# print(type(5//2)) # int double // is intiger point division

# # 2. Variables and Built-in Functions
# # Question: What will be the value of the variable result after executing the following code? Explain your answer.

# x = 10
# y = x ** 2
# result = pow(x, 3) + max(y, x) - abs(-5) # pow = 10***3 = 1000 max = 100, abs = -5
# print(result)

# # 3. Operators
# # Question: Given two variables a = 10 and b = 15, write a Python program to swap their values without using a third variable. Explain the logic behind the solution.
# a = 10
# b = 15

# temp = a
# a = b
# b = temp

# print(a,b)

# # 5. Lists
# # Question: Given a list nums = [10, 15, 3, 7] and a target sum k = 17, write a Python function that returns whether any two numbers from the list add up to k. Explain your approach.
# list_nums = [10,15,3,7,3,2,4,5,1,12]
# max = 1
# for n in list_nums:
#     if n > max:
#         max = n

# print(max)

# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

#     # grades = []
#     # for grade in students:
#     #     grades.append(grade[1])
        
# grade = [grade[1] for grade in students]
          
# # unique_grade = list(set(grades))
# unique_grade = sorted(set(grade))
    
# second_lowest_grade = unique_grade[1]


# # # second_lowest_names = []
# # # for student in students:
# # #     if second_lowest_grade == student[1]:
# # #         second_lowest_names.append(student[0])

# second_lowest_names = [name[0] for name in students if second_lowest_grade == name[1]]
            
            
# second_lowest_names.sort()
            
# for name in second_lowest_names:
#     print(name)

# students_scores = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
# print(students_scores['Krishna'])
# total = []
# for score in students_scores['Krishna']:
#     total.append(score)


# avg = sum(total)//len(total)
# print(f"{avg:.2f}")

# stri = "python"
# new_str = (stri.swapcase)
# print(stri.swapcase())

# def swap_case(s):
#     return (s.swapcase())

# s = 'HackerRank.com presents "Pythonist 2"'
# print(swap_case(s))

# def split_and_join(line):
#     split_line = line.split(" ")
#     join_line = "-".join(split_line)
#     print(join_line)

# split_and_join(line="This is me deepak")

# def print_full_name(first, last):
#     print(f"hello {first} {last}! You Just delved into python")

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# def mutate_string(string, position, character):
#     lst_string = list(string)
#     lst_string[position] = character
#     str_lst_string = "".join(lst_string)
#     return str_lst_string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# def mutate_string(string, position, character):
#     lst_string = list(string)
#     lst_string[position] = character
#     new_str = ''.join(lst_string)
#     return 

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

print("WEl COME TO KBC")
money = 0
continu = True
while continu:
    print("Here is your first question for 10000:")
    print("What is Capital of India ?")
    print("A.mumba B.delhi C.nagpur D.Pune")
    ans = input("Enter your Option you selected :")
    if ans == "B":
        print("Congrulations You have won 10000")
        money = 10000
        print(f"You bakance is {money}")
    else:
        print("Booo! Try again")
        continu = False
    print("Would you like to countineu Y/N?")
    co = input()
    if co == 'Y':
        print("here is ypur second question for 25000 :")
        print("who is known as father of indai ?")
        print("A.M Ghandi B.s bose D.n Modi C.j Nehru")
        ans = input("Enter Your Option you've selected :")
        if ans == 'A':
            print('yesss you have won 25000')
            money = 25000
            print(f"Balance = {money}")
        else:
            print("boooo ! Wrong Answer Try again !")
            continu = False
    else:
        continu = False