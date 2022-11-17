print("hello world")

#Printing Hello World Using a Variable
message = "hello world"
print(message)

#Concatenate two Python Strings to Print Hello World
word1 = "hello"
word2 = "world"
print(word1+" "+word2)

#Use the String format() Method to Print Hello World
word1 = "hello"
word2 = "world"
print("{} {}".format(word1, word2))

#Using Python f-strings to Print Hello World
word1 = "hello"
word2 = "world"
print("{word1} {word2}")

# Using a List and the String join() Method
words = ["hello","world"]
message = " ".join(words)
print(message)

#Using a List of Characters and the String join() Method
characters = ['H','e','l','l','o',' ','W','o','r','l','d']
message = "".join(characters)
print(message)

#new
#Using Dictionary Values to Print Hello World in Python
words = {1: "Hello", 2: "World"}
print(words.values())

#Using Python Dictionary Keys to Print Hello World
words = {"Hello": 1, "World": 2}
print(words.keys())

#with join method
message = " ".join(words.keys())
print(message)
