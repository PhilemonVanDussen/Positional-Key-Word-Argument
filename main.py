# PJ VanDussen
# 11/13/2024
# Practice: Positional & Keyword Arguments in Python


# POSITIONAL ARGUMENTS
# Start by writing the code to create the three functions outlined below
# You'll use only positional arguments in the first three functions
# Test your code and correct any errors

# Greet The User
# Write a function that takes two parameters -- first name and age
# Use an f-string to welcome the user by first name and to display his/her age

# def hello(fname, age):
#     print(f'Hello {fname}, you are {age} years old')
# hello('John', 13)
    
# Area of a Rectangle
# Write a function to calculate the area (in square feet) of a rectangle
# Your two parameters will be length and width
# The print statement in the function should display the length, width and area (in square feet) of your rectangle

# def rect_area(length, width):
#     area = length * width
#     print(f'The length of the rectangle is {length}sq ft. and the width is {width}sq. ft and the area is {area}')
# rect_area(2,3)
# rect_area(12, 13)
    
# Sum of Numbers
# Write a function that finds the sum of three numbers
# Your three parameters will be num1, num2, and num3
# The print statement in the function should display the sum of the three numbers

# def sum_num(num1, num2, num3):
#     sum = num1 + num2 + num3
#     print(f'The sum of the 3 numbers is {sum}')
# sum_num(3, 2, 1)


# KEYWORD ARGUMENTS
# Create the three functions outlined below
# In these last three functions, you'll use only keyword arguments 
# Test your code and correct any errors

# Greet By Title
# Write a function that greets the user by title, first name and last name
# Examples of titles include: Mr., Ms., Mrs. and Dr.
# When calling your function, change the order of your keyword arguments so that they don't match the order of your function parameters

# def greeting(title, fname, lname):
#     print(f'Hello {title} {fname} {lname}, how are you ')
# greeting(title = 'Mrs', lname = 'Mooner', fname= 'Lylah' )

# Describe Your Pet
# Write a function that says what type of pet you have and what your pet's name is
# Your function parameters will be pet_type and pet_name

# def pet_fun(pet_type, pet_name):
#     print(f'Your pet is a {pet_type} and their name is {pet_name}')
# pet_fun('dog', 'coche')

# Updated Function
# Choose any ONE of the first three functions from this project and rewrite it below using keyword arguments

def pet_fun(pet_type, pet_name):
    print(f'Your pet is a {pet_type} and their name is {pet_name}')
pet_fun(pet_type = 'cat', pet_name = 'Joe')