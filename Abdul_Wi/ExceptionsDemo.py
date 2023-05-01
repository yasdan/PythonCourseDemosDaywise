#import sys
# dictionary containing longitude and latitude of places
persons = {("Vijayawada", "Andhrapradesh"):"Abdul Yesdani",
		("Hyderabad", "Telangana"):"Rajendar"}
print(persons)
# Traversing dictionary with multi-keys and creating
# different lists from it
city = []
state = []
person = []
for i in persons:
	city.append(i[0])
	state.append(i[1])
	person.append(persons[i[0], i[1]])
print(person)
print(city)
print(state)

# Python code to illustrate
# working of try()
# def divide(x, y):
# 	try:
# 		result = x / y
# 		print("The quotient is :", result)
# 	except ZeroDivisionError:
# 		print("Devision by Zero error ")

# divide(3, -1)

# try:
#     num=int(input("Enter any positive number: "))
#     if num < 0:
#         raise  Exception("Not a positive number")
# except Exception as valer:
#     print(valer)
# print(num)



# grades =input("enter grades, separated by commas: ").split(",")
# try:
#     grades = [int(grade) for grade in grades]
# except ValueError:
#     print("The grades you entered were in an invalid format.")
# print(grades)

# class FormulaError(Exception):
#     pass
# def parse_input(user_input):
#   input_list = user_input.split()
#   if len(input_list) != 3:
#     raise FormulaError('Input must be consist of three elements')
#   n1, oprtr, n2 = input_list
#   try:
#     n1 = float(n1)
#     n2 = float(n2)
#   except ValueError:
#     raise FormulaError('The first and third input value must be numbers')
#   return n1, oprtr, n2

# def calculate(n1, op, n2):
#
#   if op == '+':
#     return n1 + n2
#   if op == '-':
#     return n1 - n2
#   if op == '*':
#     return n1 * n2
#   if op == '/':
#     return n1 / n2
#   raise FormulaError(f' {op} is not a valid operator')


# while True:
#   user_input = input('>>> ')
#   if user_input == 'quit':
#     break
#   n1, op, n2 = parse_input(user_input)
#   result = calculate(n1, op, n2)
#   print(result)