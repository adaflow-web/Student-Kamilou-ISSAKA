# # print("Hello")

# # # Farenheit = (Celsius * (9/5))+ 32
# # Celsius = 32 
# # Farenheit = (Celsius * (9/5))+ 32
# # print(Farenheit)  

# # celsius = 15
# # Farenheit = (Celsius * (9/5)) + 32

# # print(Farenheit)

# # Celsius = -4
# # Farenheit = (Celsius) * (9/5) + 32

# # print(Farenheit)

# # # Reusability and Function

# # def say_hello():
# #     print("Hello!")
    
# # def say_hello():
# #     print("Hello!")
    
# # say_hello()
# # say_hello()
# # say_hello()

# # def say_hello():
# #     print("Hello!")
# #     print("How are you today?")
# #     print("It is nice meeting you!")
    
# # say_hello()
# # say_hello()

# # # Most colorsFunctions
# # def show_colors():
# #     print("Red is a color")
# #     print("Blue is a color")

# # show_colors()
# # show_colors()
# # show_colors()
# # show_colors()
# # show_colors()

# # # Students in formation
# # def count_students():
# #     girls = 5
# #     boys =2
# #     students = girls + boys
# #     print(students)
    
# # count_students()
# # count_students()
# # count_students() 
# # # Multiple Functions

# # def say_hello():
# #     print("Hello!")
    
# # def ask_question():
# #     print("How are you?")
    
# # def say_goodbye():
# #     nom = "Johny"
# #     message = "Googbye " + nom
# #     print(message)
    
# # say_hello()
# # ask_question()
# # say_goodbye() 

# # # Parameters 

# # nom1 = "Eva"
# # nom2 = "Khalida"
# # nom3 = "Angelika"
# # nom4 = "Maria"

# # greetings = "Hello! "

# # message = greetings + nom1
# # print(message)

# # message = greetings + nom2
# # print(message)

# # message = greetings + nom3
# # print(message)

# # message = greetings + nom4
# # print(message)

# # # Example of parameter

# # def say_hello(nom):
# #     nom1 = "Eva"
# #     nom2 = "Khalida"
# #     nom3 = "Angelika"
# #     nom4 = "Maria"
# #     print("Hello " + nom)
    
# # say_hello()

# # # Calculator addNumbers

# # def add_numbers(number_one, number_two):
# #     result = number_one + number_two
# #     number_one = (10, 11.6, 5)
# #     number_two = (2, 7.1, -7)
# #     print(result)

    
# # add_numbers()
# # add_numbers()
# # add_numbers()

# # Return Value

# # def add_numbers(number_one, number_two):
# #     result = number_one + number_two
# #     return result
# # total = add_numbers(10,2)
# # print(total)

# # MAKE MY TEMP CONVERTER WORK WITH USER INPUT

# # def temp_converter(celsius):
# #     msg_1 = " degrees Celsius are "
# #     msg_2 = " degrees Farenheit."
# #     result = (celsius * 9/5) + 32
# #     return str(celsius) + msg_1 + str(result) + msg_2

# # user_input = input("Enter a temperature in degrees Celsius: ")
# # Farenheit_result = temp_converter(float(user_input))

# # print(Farenheit_result)

# # # CHF to Gn$ CONVERTER

# def chf_converter(chf,exchange_rate):
#     gnd = chf * exchange_rate 
#     chf_converter = "Today, Gn$" + str(" Gn$") + " can buy CHF " + str(chf) + "."
#     return chf_converter

# user_input_1 = float(input("Enter the Gn$ amount: "))
# user_input_2 = float(input("Today's exchange rate: "))

# print(chf_converter(user_input_1,user_input_2))


# # CONVERTER ANOTHER WAY

# # def converter():
# #     celsius = input("1. Enter a temperature in degrees Celsius: ")
# #     farenheit = (float(celsius) * 9/5) + 32
# #     return celsius + " degrees celsius are " + str(farenheit) + " degrees Farenheit."

# # print(converter())

# # Make some FUNCTION REUSABLE

# # # def some_function(some_input):
# # #     return some_input

# # # entry = input("Enter something: ")
# # some_function(entry)

# # Booleans

# day = True
# night = False

# print(day)
# print(night)

# # The Equality sign in programming ==

# print(5 == 5)

# print(100 == 7)

# secret_number = 5
# guess = input("Enter a number between 1 and 10: ")
# print(secret_number == int(guess))

# # Not Equal sign !=

# print(7 != 6+1)

# ANSWER EXERCICE

# value = input("Enter your secret winner: ")
# secret_winner = "Argentine"
# if(secret_winner == value) :
#     print(True)
# else :
#     print(False)
    
# secret_word = "dog"
# guess = input("Human's best friend: ")
# print(secret_word == str(guess))

# IF THIS THEN WHAT

# secret_word = "Exploration"
# guess = input("Try to guess my favourite word: ")
# if secret_word == guess:
#     print("Congratulations! You've found the secret word!")
# if secret_word != guess:
#     print("Try again!")
    
    # Walkingthrough
    
# result = 10
# guess = input("What is the result of 7+3?")

# if result == int(guess):
#     print("Congratulations! You found the correct result.")
    
# print("The program terminated successfully.")

# EXAMPLE

# a = input("Please enter value for var 'a': ")
# b = input("Please enter value for var 'b': ")

# u = input("What is the result of "+a+"+"+b+"? ")

# if((int(a) + int(b))== int(u)) :
#     print("Yes! You are absolutely right!")
# else :
#     print("No! You are wrong")
#     print("Correct answer is " + str(int(a)+int(b)))
    
# TO CONCATENATE NUMBERS AND GET STRING

# print(str(5) + str(2))
#CONCATENATE NUMBERS TO GET ADD RESULT
# print(int(5) + int(2))

# print(float(5) + float(2))

# To continue

# a = 2
# b = 3
# result = 5
# user_input = input("Enter your answer: ")
# if result == int(user_input):
#     print("Congratulations! ")
# print(" Whatever the user's answer was, this line should always be displayed before the program exits.")

# The logic behind putting the if statement outside the function

# def tempConvert(celsius):
#     msg1 = " degrees C are equal to "
#     msg2 = " degrees F."
#     farenheit = 32 + (celsius * 9/5)
#     return str(celsius) + msg1 + str(farenheit) + msg2
#     if int(celsius) > 38.5:
#        return str(celsius) + msg1 + str(farenheit) + msg2 + "That's hot!!"
#     else:
#        return str(celsius) + msg1 + str(farenheit) + msg2
   
#    # RETURN "A String"
   
# def converter():
#     user_input = input("Enter the amount of CHF that you want the convert to €: ")
#     msg_2 = " CHF is "
#     result = float(user_input) * 0.98
#     message = user_input + msg_2 + str(result) + " €"

#     if float(user_input) < 0:
#         return "Enter a number between 0 and 100'000.-"

#     if float(user_input) == 100:
#         return "This is a lot of money!"

#     return message

# print(converter())
# print("The programme has successfully terminate.")

# upgrading my money converter with promotion

# def converter():
#     user_input = input("Enter the amount of CHF that you want the convert to €: ")
#     msg_2 = " CHF is "
# #     result = float(user_input) * 0.98
# # #     message = user_input + msg_2 + str(result) + " €"

# # #     if float(user_input) < 100:
# # #         return "Enter a number between 0 and 100'000.-"

# # #     if float(user_input) >= 100:
# # #         return "This is a lot of money!"

# # #     return message

# # # print(converter())
# # # print("Congratulation you get our Promotion!")

# # # UPGRADING MY CONVERTER AGAIN

# # def convert(cfa):
# #     if cfa > 100:
# #         print("You need to get autorisation!")
        
# #     msg1 = " You can pass "
# #     msg2 = " with CHF."
# #     result = cfa * 780
# #     return str(cfa) + msg1 + str(result) + msg2

# # print(convert(700))
# # print(convert(49))

# # Practice with else!

# # enter_number = 10
# # guess = input("Enter a number between 1 and 10: ")

# # if enter_number <= int(guess):
# #     print("You win!")
# # else:

# #     if enter_number >= int(guess):
# #         print("You lose!")

# # print("Try to play again!")

# # # SAME EXAMPLE WITH !=

# # guess = input()
# # print("Write a number between 1 and 10: ")

# # if float(guess) != 9:
# #     print("You lose!")
    
# # else:
# #     print("You win!")
    
# # print("Try to play again!")

# # SOMETHING SHORTCUT CODE

# # secret_number = 8
# # def secret(guess):
# #     if guess == secret_number:
# #         text =  "You win!"
# #     else :
# #         text =  "You lose!"
# #     return text + "\nTry to play again!"

# # guess = int(input("Provide a number between 1 and 10 : ")) 
# # print(secret(guess))   
        

# # UPGRADE MY SECRET WORD GAME

# # secret_word = "Exploration"
# # guess = input("Try to guess my favourite word: ")
# # if (secret_word == guess) :
# #     print("Congratulations!!!") 
# # else :
# #     print("Ooops! Try again!")
    
# # CHAINING STATEMENTS

# # weather = "sunny"

# # if weather == "raining":
# #     print("Take an umbrella.")

# # if weather == "sunny":
# #     print("Take sunglasses.")

# # if weather == "snowing":
# #     print("Take gloves.")
    
# # # SOME OTHERS

# # weather = "sunny"

# # if weather == "raining":
# #     print("Take an umbrella.")

# # if weather == "sunny":
# #     print("Take sunglasses.")

# # if weather == "snowing":
# #     print("Take gloves.")
# # else:
# #     print("Stay home.")
    
# # # ELIF 

# # weather = "sunny"

# # if weather == "raining":
# #     print("Take an umbrella.")
# # elif weather == "sunny":
# #     print("Take sunglasses.")
# # elif weather == "snowing":
# #     print("Take gloves.")
# # else:
# #     print("Stay home.")
    
# # # REMPLACING "SUNNY" TO SEE WHAT HAPPEN

# # weather = "Cloudy"

# # # if weather == "raining":
# # #     print("Take an umbrella.")
# # # elif weather == "sunny":
# # #     print("Take sunglasses.")
# # # elif weather == "snowing":
# # #     print("Take gloves.")
# # # else:
# # #     print("Stay home.") 
    
# # # EXERCICE: Practice with ELSE IF

# # user_input_a = float(input("Please enter the first number: "))
# # user_input_b = float(input("Please enter the second number: "))

# # result = user_input_a - user_input_b

# # if result > 10:
# #     print("The result is greater than 10.")
# # elif result < 10 and result > 0:
# #     print("The result is greater than 0 but not than 10.")
# # elif result == 0:
# #     print("The result is Zero.")
# # else:
# #     print("The  result is a negative number.")
    
# # print(" Try again!")

# # OTHER EXAMPLE

# result = 15

# if result > 15:
#     print("The result is greater than 15")
# elif result == 15:
#     print("The result is equal to 15")
# elif result > 10:
#     print("The result is greater than 10")
# else:
#     print("The result is smaller than 10")
    
    # THE AND SYNTAX WITH PY
    
# weather = "sunny"
# temperature = "warm"

# if weather == "sunny" and temperature == "warm":
#     # print("Take sunglasses and a T-shirt")
    
    
# CHANGING VALUE IN AND CONDITION

# weather = "sunny"
# temperature = "cold"

# if weather == "sunny" and temperature == "warm":
#     print("Take sunglasses and a T-shirt")

# USE ELSE WITH CHANGINGS
# weather = "sunny"
# temperature = "cold"

# if weather == "sunny" and temperature == "warm":
#     print("Take sunglasses and a T-shirt")
# else:
#     print("Try to adapt your dressing!")
    
# Using and in python

# def weather_function(weather, temperature):
#     if (weather == "raining" and temperature == "cold"):
#         return("Take an umbrella and a warm jacket")
#     elif (weather == "raining" and temperature =="warm"):
#         return("Take an umbrella and a t-shirt")
#     elif (weather == "sunny" and temperature =="cold"):
#         return("Take sunglasses and a warm jacket")
#     elif (weather == "sunny" and temperature =="warm"):
#         return("Take sunglasses and a t-shirt")
#     else:
#         return("Just stay home!")

# print(weather_function("sunny", "cold"))
# print(weather_function("sunny", "warm" ))
# print(weather_function("snowing", "cold"))

# SAYING OR WITH PYTHON

# a = 8
# b = 12

# if a > 10 or b > 10:
#     print("At least one of the two numbers is greater than 10!")
# else:
#     print("Both numbers are not greater than 10.")
  
  
#   USE AND IN PLACE OF OR

# a = 8
# b = 12

# if a > 10 and b > 10:
#     print("At least one of the two numbers is greater than 10!")
# else:
#     print("Both numbers are not greater than 10.")
    
#MAKE THE SYNTAX AND WORK WITH AND & OR
# prgrm_language = input("What language are you using?")

# if prgrm_language == "Python" or "JavaScript":
#     print("This is good Programming language")
# elif prgrm_language == "Python" and "JavaScript":
#     print("This is Thinking and Creating with Code!")
# else:
#     print("Nice to learn something new!")
    

# number = input("Guess the number: ")
# color = input("and now the color: ")

# if float(number) > 10 or color == "Blue":
#     print("Cool!")
# elif float(number) <= 10 and color == "Blue":
#     print("Cool!")
# else:
#     print("Play again")
    
# RETURN STATEMENT WITH PYTHON
# def play():
#     numberSecret = 7
#     colorSecret = "Blue"

#     number = input("Enter a number between 1 and 20: ")
#     color = input("Enter a color: ")

#     if int(number) == numberSecret and color == colorSecret:
#         print("You've found both the secret number and the secret color!")
#     elif int(number) == numberSecret or color == colorSecret:
#         print("You found at least one of the secrets!")
#     else:
#         print("You didn't find any of the secrets! Better luck next time!")
#     print("Try again!")
    
# play()

# ERRORS AND US : SYNTAX ERRORS

# Implement errorS

# result = (3 + 5) * 2
# print("The result is 16: " + str(result))

# result = 3 + 5 * 2
# print("The result is 16: " + str(result))

# FIX PYTHON ERRORS NOW

# def say_Hi(name, age):
#     message = "Your name is" + #"and you're " + #int(age) + " years old."
#     return message

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(say_Hi(name, age))

# We haven't to concatenate the parameter AGE, OUR FUNCTION WILL RUN AN ERROR the str("and you are" need space in the beginning to be well write.)

#It can be fix like that

# def say_Hi(name, age):
#     message = "Your name is" + " and you're " + age + " years old."
#     return message

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(say_Hi(name, age))

# GOOD SYNTAX AND CONVERT AN INPUT TO AN INT WITH INT(INPUT("...")) BY CASTING AN INPUT DIRECTLY

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# first_number = int(input("Enter a number: "))
# second_number = int(input("Enter another number: "))

# message = "The result of " + str(first_number) + " + " + str(second_number) + " is " + str(add(first_number, second_number))
# print(message)

# message = "The result of " + str(second_number) + " - " + str(first_number) + " is " + str(subtract(second_number, first_number))
# print(message)

# FIXING THE CODE

# print("Dou you like programming?")
# print("A. Ya")
# print("B. No")
# answer = input("Enter A or B: ")

# if answer == "A":
#     print("Awasome! Programing is really fun!")
# else:
#     answer == "B"
# print("Hang in there!  It's an acquired taste!")

# ERRORS HUNTER / IF WE DON'T CONVERT STR INTO INT VALUE AND WE DIDN'T CONCATENATE OUR RESULT WE'LL GET ERROS
# er.py", line 635, in <module>
#     message = "The result of " + first_number + " + 
# " + second_number + " is " + add(first_number, second_number)
#               ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~       
# TypeError: can only concatenate str (not "int") to str

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# first_number = input("Enter a number: ")
# second_number = input("Enter another number: ")

# message = "The result of " + first_number + " + " + second_number + " is " + add(first_number, second_number)
# print(message)

# message = "The result of " + second_number + " - " + first_number + " is " + subtract(second_number, first_number)
# print(message)

#THEN WE FIX IT BY THE FOLLOWING

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# first_number = int(input("Enter a number: "))
# second_number = int(input("Enter another number: "))

#  message = "The result of " + str(first_number) + " + " + str(second_number) + " is " + str(add(first_number, second_number))
#  print(message)

#  message = "The result of " + str(second_number) + " - " + str(first_number) + " is " + str(subtract(second_number, first_number))
#  print(message)

#  OR WE CAN ALSO FIX IT LIKE THAT

# def add(a, b):
#     return float(a) + float(b)
# def subtract(a, b):
#     return float(a) - float(b)
# first_number = input("Enter a number: ")
# second_number = input("Enter another number: ")
# message = "The result of " + first_number + " + " + second_number + " is " + str(add(first_number, second_number))
# print(message)
# message = "The result of " + first_number + " - " + second_number + " is " + str(subtract(first_number, second_number))
# print(message)

# def get_result(answer):
#     if answer == "a":
#         return "True"
#     else:
#         return "False"

# WRITE LOOPS IN PYTHON

# for x in range(10):
#     print("Hello World!,by Alan WALKER")
    
# SOME OTHER LOOPS

# for x in range(11):
#     print(x) 

#Exercise on loop which display Number: 0; Number: 1...

# for x in range(8):
#     print("Number: " + str(x))

#DO IT AGAIN

# for x in range(102):
#     print("Number: " + str(x))

# Exercise on STEP

# for i in range(7):
#     "current_step" == str(i + 1)
#     step_word = ""
#     if "current_step" == "1":
#         step_word = " step"
#     else:
#         step_word = " steps"
#         print("current_step" + step_word)

#OTHERS

# for i in range(5):
#     current_step = str (i + 1)
#     step_word = ""
#     if current_step == "1": 
#         step_word = " step"
#     else:
#         step_word = " steps"
#     print(" It's " + current_step + step_word)

# My first loop

# for a in range(11):
#     print(str(a) + " is a number")

# Test WHILE LOOP

# a = 0
# while a < 3:
#     print("Hello world!")
#     a = a + 2

# MY FIRST WHILE LOOP

# z = 3

# while z < 50:
#     print("Hello world!")
#     z = z + 1

#WHILE LOOP

# fruits = ["apples", "oranges", "kiwis"]
# loops = 0

# while loops < len(fruits):
#     print(fruits[loops])
#     loops = loops + 1

# ARRAY

# students = ["Maria", "Kelly", "Khalida", "Eva","Angelica", "Kémal"]

# for x in students:
#     print(x)

# OTHER ARRAW

# students = ["Maria", "Kelly", "Khalida", "Eva","Angelica", "Kémal"]

# for x in range(0):
#     print(students[0])
    
#OTHER ONE

# students = ["Maria", "Kelly", "Khalida", "Paulo", "Eva","Angelica", "Kémal"]

# for x in range(5):
#     print(students[x])

# Same OTHER 
# students = ["Maria", "Kelly", "Khalida", "Paulo", "Eva","Angelica", "Kémal", "Kokoé"]

# for x in range(7):
#     print(students[x])
# IF the list array growth and we print x in range of a number  < our list, some of the list won't be printed.

# students = ["Maria", "Kelly", "Khalida", "Eva","Angelica", "Kémal"]

# for student in students:
#     print(student)

#OTHER ARRAW AGAIN

# students = ["Maria", "Kelly", "Khalida", "Eva","Angelica", "Kémal"]

# for x in students:
#     print(x)

# FOR LOOP

# fruits = ["apples", "oranges", "kiwis"]
# for x in range (2):

#     print(fruits[x])
#     x = x + 1 

# LOOP THROUGH MY FAVORITE SONGS

# fun_songs = ["Sing me to sleep", 
#             "I fadded", 
#             "Unstoppable", 
#             "Falling love","Someone like you",]

# print("There are my favorite songs!")

# LOOP FOR

fun_songs = ["Sing me to sleep", 
            "I fadded", 
            "Unstoppable", 
            "Falling in love","Someone like you",]

print("There are my favorite songs!")

# for song in fun_songs:
#     print(song)
    
# print("And tell me yours!")

#FOR LOOP USING A FUNCTION , THE INDEX AND THE NAME MY INDEX

# def display_catalogue():
#     fun_songs = ["Sing me to sleep", 
#             "I fadded", 
#             "Unstoppable", 
#             "Falling in love","Someone like you",]
#     index = 0
#     for song in fun_songs:
#         print(str(index) + " - " + song)
#         index = index + 1

# display_catalogue()

# SAME FOR LOOP IN SHORT

# def display_catalogue():
#     fun_songs = ["Sing me to sleep", 
#             "I fadded", 
#             "Unstoppable", 
#             "Falling in love","Someone like you",]
#     for song in fun_songs:
#         print(str(fun_songs.index) + " - " + song) 


# display_catalogue()

# LOOP ON MY BEST FOODS

best_foods = ["Watché", 
            "Coliko", 
            "Akoumé", 
            "Touwoo","Abloo",]

print("Here are my favorite foods!")

for food in best_foods:
    print(food)
    
print("Tell me what are your favorite foods?")