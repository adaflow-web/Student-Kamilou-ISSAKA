result = 3 + 7 * 7
# print(result)

bananas = 4
mangoes = 7
fruits = bananas + mangoes
# print(fruits)

pears = 201
ananas = 41

# print(pears)


message = ("Hello everyone!")
# print(message)


message = "Hello, my name is Kémal. ""Today is a nice day! ""I'd like to enjoy it with you."
# print(message)

greetings = "Hello"
nom = "Florence"
message = greetings + nom
# print(message)

greetings = "Hello"
nom = "Florence"
space = " "
message = greetings + space + nom
# print(message)

greetings = "Hello "
nom = "Florence"
message = greetings + nom
# print(message)

# # Calculator addNumbers

# def add_numbers(number_one, number_two):
#     result = number_one + number_two
#     number_one = (10, 11.6, 5)
#     number_two = (2, 7.1, -7)
#     print(result)

    
# add_numbers()
# add_numbers()
# add_numbers()

# Return Value

def add(number_one, number_two):
    result = number_one + number_two
    return result
total = add(10,2)
# print(total)

# Another example

def greet(name, weather):
    message = "Hi " + name + ". It is a " + weather + " day."
    # return message

greetings = greet("Sasha", "rainy")
# print(greetings)

greetings = greet("Carl", "sunny")
# print(greetings)

# Answer of practice on return Value

def add(number_one, number_two):
    result = number_one + number_two
    # return result

def substract(number_one, number_two):
    result = number_one - number_two
    # return result

def multiply(number_one, number_two, number_three):
    result =number_one*number_two*number_three
    # return result

total = add(47,12)
# print(total)

total = substract(9,11)
# print(total)

total = multiply(13,4,32)
# print(total)

# Upgrade my tempreture converter CONVERTER FUNCTION

def temp_converter(celsius):
    return (celsius * (9/5)) + 32

result = temp_converter(-3)
# print(result)

# print(temp_converter(0.9))
# print(temp_converter(-10.9))
# print(temp_converter(16))
# print(temp_converter(0))

# Problem with mixing types

# a_number = 7
# a_string = "Hello"

# result = a_number + a_string
# print(result)

# # To resolve such problem we try to concatenate and be precise
# # the error still continue
# a_number = "7"
# a_string = "Hello"

# result = a_number + a_string
# print(result)

# # ERROR AGAIN

# number_one = 2
# number_two = 7
# result = number_one + number_two

# a_string = result + a_string

# message = result + a_string
# print(message)

# USE STRING FUNCTION TO CONVERT ANY NUMBER 

number_one = 2
number_two = 7
result = number_one + number_two

a_string = "Hello"

message = str(result) + a_string
# print(message)

# CONVERT A STRING VALUE INTO INTERGER

apples = "5"
bananas = 1

result = int(apples) + bananas
# print(result)

# SOME OTHER EXAMPLES

apples = 0
bananas = 5
fruits = bananas and + apples
message = "I eat per day " + str(fruits) + " apples."

# print(message)

# THE INPUT() FUNCTION

# print("Please enter your name:")

# name = input()

# print("Your name is " + name)

# #REWRITING OF OUR ALL PROGRAMM

# name = input("Please enter your name: ")
# print("Your name is " + name)

#ALL INPUTS ARE STRINGS

x = input("Enter a number: ")
y = input("Enter a second number: ")
result = x + y
message = "The result of " + x + " plus " + y + " is " + result

# print(message)

# CONCATENATE by converting TWO NUMBER

apples = "3"
oranges = "7"

result = apples + oranges
# print(result)

# CONVERT STRING INTO NUMBER

apples = "3"
oranges = 2

result = int(apples) + oranges
# print(result)

# CONVERT TWO NUMBERS INTO STRINGS

apples = "3"
oranges = "2"

result = str(apples) + str(oranges)
# print(result)

# CONVERT TWO NUMBERS INTO STRINGS

apples = "3"
oranges = "2"

result = int(apples) + int(oranges)
# print(result)

# COMPLETE SENTENCE WITH THE STR AND INT FUNCTION

apples = 3
oranges = 5
fruits = apples + oranges

message = "There are " + str(fruits) + " fruits in the basket."

# print(message)


#ADD FUNCTION

# def add(a, b):
#     message = "The result is "
#     c = a + b
#     return message + c

# print(add(6, 7))

# CONCATENATE TO FIX THE ERROR

def add(a, b):
    message = "The result is "
    c = a + b
    # return message + str(c)

print(add(6, 7))

# FRIENDLY CONVERTER (Celsius * 9/5) + 32 =farenheit

# def converter(celsius):
#     return ((celsius * 975) + 32)

# print("-7.9 degrees celsius are ") + str(converter(-7.9) + " degrees farenheit")


# TO FIX ERROR TYPE

# def converter(celsius):
#     return ((celsius * 9/5) + 32)

# print("18.5 degrees celcius are " + str(converter(18.5)) + " degrees farenheit")

# def converter(celsius):
#     return (celsius * 9/5) + 32

# celsius = input("Enter your value in Celsius: ")
# farenheit = converter(int(celsius))
# print(celsius +  " degrees Celsius are " + str(farenheit) + " degrees Farenheit.")

# SPEAK PYTHON

# def chfToGND(chf) : 
#     # return int(chf) * 780.34

# chf = input("Enter your value in chf: ")
# gnd = chfToGND(chf)
# # print(chf + " chf are " + str(chf) + " GND$")

# print(chfToGND(2000))

# THE AND SYNTAX WITH PY

# weather = "sunny"
# temperature = "warm"

# if weather == "sunny" and temperature == "warm":
#     # print("Take sunglasses and a T-shirt")
    
# THE CHANGING OF ONE VALUE IN THE SAME LOGIQUE

# weather = "sunny"
# temperature = "cold"

# if weather == "sunny" and temperature == "warm":
#     print("Take sunglasses and a T-shirt")

# TRYING LOOP WHICH DISPLAY Number: 1, Number: 2,...using int or float to concatenate

# for x in range(8):
#     print("Number: " + int(x)) / this code run an error TypeError: can only concatenate str (not "int") to str

# for x in range(8):
#     print("Number: " + float(x))