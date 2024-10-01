# ------------------------------------ Exception Handling
# Exception handling is a process of handlisng errors 

# try:
#     when this code run without any errors
# except:
#     if error occurs in above code this code runs
# finally:
#     runs code 

# try:
#     print(10+20)
# except:
#     print("Somethinf is wrong")

# try:
#     name = input("Enter Your Name :")
#     birth_year = int(input("Enter Year of Birth :"))
#     years = 2024 - birth_year
#     print(f"Your name is {name} and your current age {years}")
# except TypeError:
#     print("there is a type error")
# except SyntaxError:
#     print("There is a Syntax error !")
# except ValueError:
#     print("there is a Value Error")
# except ZeroDivisionError:
#     print("there is a zerodivide error")

# try:
#     22 + '34'
# except Exception as e:
#     print(e)

# def sum_of(a,b,c,d,e,f):
#     return a+b+c+d+e+f

# tpl = (1,2,3,4,5,6)
# print(sum_of(*tpl))

# lst = [1,2,3,4,5,6]
# print(sum_of(*lst)) here * is used for list to destruct

# ** is used for dictonary

# def info(name,age,country):
#     return f"name is {name} and age is {age} and lives in {country}"

# dit = {"name":"deepak",'age':'21','country':'India'}
# print(info(**dit))

# def sum_of(*rest):
#     for i in rest:
#         print(i)

# print(sum_of(1,2,3))