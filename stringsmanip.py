# Manipulating strings with python

# text = "Hallo dir!"

# print(text[0])

# white spaces are counted

# text = "Hallo dir!"

# print(text[5])

#Possile to print 2 caracters

# text = "Hallo dir!"

# print(text[0:2])

# counting the number of caracters we use

# text = "Hallo dir!"

# print(len(text))

# Substracting a part of our text using substring

# text = "Hallo dir!"
# substring = text[6:10]

# print(substring)

#Possibility to remove whitespaces ,andpreceding in our text using stripped function strip()
# text = "     Hallo dir!      "
# stripped = text.strip()

# print(stripped)
# Upper case and lower case

# a = "Hello, You!"
# b = "HALLO DIR!"
# print(a.upper())
# print(b.lower())

# Possibility to replacing a content inside a string

# a = "This is a snowy day"
# b = a.replace("snowy", "cloudy")

# print(b)

# Splitting a string into an array

# words = "apples,oranges,bananas"
# fruits = words.split(",")
# print(fruits)

# Finding a string within a string

# a = "This is a great day to learn about programming."
# b = a.find("great")
# c = a.find("Blue")

# print(b)
# print(c)

# Combining string functions/ Vérifier le non remplacement de "great" par "beautyful"

# a = "This is a great day to learn about programming."
# b = a.replace("great", "beautiful").upper().split(" ")

# print(b)
# print(a) 

# Finding array places

# message = "Hey you! How is the weather like outside the !"
# result = message.find("the")
# print(result)
# string = message.split(" ")
# for string in message:
#     print(result)

# Possible to found upper letter place?
# message = "Hey you! How is the weather like outside the !"
# result = message.find(string).split[:]
# print(result)
# string = message.split(" ")
# for string in message:
#     print(result)

# Possibility to found a string, its length, indexes of a list

# message = "hey you! How is the weather like outside the !"
# listOfIndexes = []
# messageLength = len(message)
# for index in range(messageLength):
#     if message.find('the', index) == index:
#         listOfIndexes.append(index)
        
# print(listOfIndexes)

# Manually solution

# message = "hey you! How is the weather like outside the !"
# result1 = message.find("the")
# result2 = message.find("the", 17)
# result3 = message.find("the", 24)

# indexes = [result1, result2, result3]

# print(indexes)

# Turning strings into array

# words = "Mangoes,Apples,Limes,Oranges"

# array = words.split(" ")

# print(array)

# Turning stings into array separated with coma

# words = "Mangoes,Apples,Limes,Oranges"

# array = words.split(",")

# print(array)

# Splitting with white spaces

# words = "Mangoes Apples Limes Oranges"

# array = words.split(",")

# for word in array:  
#         print(word)

# Escape sequences New line: \n Tab: \t
# \t
# a = "Hallo\tdir!"

# print(a)

#\n
# b ="Bonjourno\nSignorita!"
# print(b)

#\n befofe our string

# b ="\nBonjourno Signorita!"
# print(b)

# \n before out string combine to stip()

# b ="\nBonjourno Signorita!"
# print(b.strip())

# combining functions

# greet = " Hi dir "

# print(greet.strip().upper().replace("DIR", "KEMAL"))

# my_text = "Beautiful is better than ugly."
# "Explicit is better than implicit."
# "Simple is better than complex."
# "Complex is better than complicated."
# "Flat is better than nested."
# "Sparse is better than dense."
# "Readability counts."
# "Special cases aren't special enough to break the rules."
# "Although practicality beats purity."
# "Errors should never pass silently."
# "Unless explicitly silenced."
# "In the face of ambiguity, refuse the temptation to guess."
# "There should be one-- and preferably only one --obvious way to do it."
# "Although that way may not be obvious at first unless you're Dutch."
# "Now is better than never."
# "Although never is often better than *right* now."
# "If the implementation is hard to explain, it's a bad idea."
# "If the implementation is easy to explain, it may be a good idea."
# "Namespaces are one honking great idea -- let's do more of those!"