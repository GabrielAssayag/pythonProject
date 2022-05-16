# print('Pizza')
# print("It's really good")

################# Variable
# name = "Gabriel"
# last = "Assayag"
# full_name = name +" "+ last
# age = 21
# age += 1
#
# print(type(name))
# print("Hello " + full_name)
#
# print("your age is: " + str(age))

# height = 250.5
# print(type(height))
# print(height)
#
# print("your height is:" + str(height)+"cm")

# human = True
# print(human)
# print(type(human))
# print("Are you human? " + str(human))


#################  Multiple assignment - multiple var at the same time in one line of code
# name = "Gabi"
# age = 35
# attractive = True

# name, age, attractive = "Gabi", 21, True
#
# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30
# Spongebob = Patrick = Sandy = Squidward = 30
#
# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

################# String Methods

# name = "Gabi"
# print(len(name))
# print(name.find("b"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.replace("bi","vriel"))
# print(name*3)

################## type casting = convert the data type of a value to another data type

# x, y, z = 1, 2.0, "3"
#
# x = float(x)
# y = float(int(y))
# z = float(int(z))
#
# print("X is " + str(x))
# print("Y is " + str(y))
# print("Z is " + str(z))

################## User Input

# name = input("What is your name?")
# age = int(input("how old are you?"))
# height = float(input("how tall are you?"))
#
# print("Hello " + str(name))
# print("you are " + str(age) + " years old")
# print("you are " + str(height) + "cm tall")

################## Math Functions

# import math

# pi = 3.14
# x,y,z = 1,3,2
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(pi,y,x,z))
# print(min(pi,y,x,z))

################## String Slicing = create a substring by extracting elements from another string
################## indexing[] or slice()
################## [start:stop:step]
# name = "Gabriel Assayag"
# first_name = name[0:name.find(" ")]
# last_name = name[name.find("A"):]
# funky_name = name[::3]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wiki.com"
#
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])

################## if statement = a block of code that will execute if its  condition is true

# age = int(input("You! enter you age!"))
# if age <= 18:
#     print("you are less  or equel to 18")
# elif 50 > age > 18:
#     print("Adult")
# elif age >= 50:
#     print("old as fuck")
# else:
#     print("you haven't been born yet")

################## Logical operators  (and,or, not) = used to check if two or more conditional statement

# temp = int(input("what is the temp outside?"))
# if not(temp >= 0 and temp <= 30):
#     print("nice weather")
#     print("go outside!")
# elif not(temp < 0 or temp > 30):
#     print("stay home. its weird outside")

################## while loops - a statement that will execute its block of code as long as its true.

# while 1==1:
#     print("HA HA HA HA HA HA")

# name = ""
# name1 = None
# print(type(name1))
#
# while len(name) == 0:
#     name = input("Enter your name")
#
# print("Hello " + name)

################## for loop = a statment that will execute its a block of code a limited amount of times.
##################
################## while loop = unlimited
################## for loop = limited

# for i in range(10):
#     print(i + 1)

# for i in range(50,100 + 1,2):
#     print(i)

# for i in "Gabriel Assayag":
#     print(i)

# import time
#
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("End")

################## nested loops - the "inner loop" will finish all its iteration before
# finishing one iteration of the "outer loop"

# rows = int(input("rows"))
# column = int(input("column"))
# symbol = input("Enter Symbol to use")
#
# for i in range(rows):
#     for j in range(column):
#         print(symbol, end="")
#     print()

################## Loop control statement
### Break    = used to terminate the loop entirely
### continue = skips to the next iteration of the loop
### pass     = does nothing, acts as a placeholder

# while True:
#     name = input("Enter name:")
#     if name != "":
#         break

# phone_number = "050-1112-22333"
# display without "-"

# for i in phone_number:
#     if i =="-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)


################## Lists = used to store multiple items in the single variable.

# food = ["pizza", "Hamburger", "Hotdog", "Spaghetti"]
#
# food[0] = "Sushi"
# food.append("ice cream")
# food.remove("Hotdog")
# food.pop()
# food.insert(0,"Cake")
# food.sort()
# food.clear()
#
# # print(food[0:2])
#
# for x in food:
#     print(x)

################## 2D Lists = a list of lists

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "ham", "hotdog"]
# dessert = ["cake", "icecream"]
#
# food = [drinks,dinner,dessert]
# print(food[0])
# print(food[1][2])

################## tuple = collection which is ordered and unchangeable
#                           used to group together related data

# student = ("Gabi", 35,"Male")
#
# print(student.count("Gabi"))
# print(student.index("Male"))
#
# for x in student:
#     print(x)
#
# if "Gabi" in student:
#     print("Gabi is here!")

################## sets = collection which is unordered, unindexed. no duplicate values
# from turtle import bye
#
# utensils = {"fork", "Spoon", "Knife"}
# dishes = {"bowl", "plate","cup","Spoon", "Knife"}

# utensils.add("Napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

# print(utensils.difference(dishes))
# print(dishes.difference(utensils))

# print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)

################## dictionary = a changeable, unordered collection of unique key:value pairs
#                  Fast because they're using hashing, allow us to access a value quickly

# capitals = {'USA':'Washington','Israel': 'Jerusalem', 'India': 'New Delhi', 'Chine':'Beijing','Russia':'Moscow'}

# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys(),capitals.values())
# print(capitals.items())

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('Israel')
# capitals.clear()


# for key,value in capitals.items():
#     print(key, value)


################## index operator [] = gives access to a sequence's element (str,list,tuple)

# name = "gabi assayag"

# if(name[0].lower()):
#     name = name.capitalize()
# first_name = name[0:name.index(" ")].upper()
# last_name = name[name.index(" ")+1:].upper()
# last_character = name[-1]

# print(first_name, last_name, last_character)

################### function = a block of code which is executed only when it is called.
# hello = "Hello World!"
# name = "gab"
# numbers = str(12)
# def hello1(name,number):
# hello = "Hello World"
# print(hello + " " + name + number)
# print(hello)
# def hello(name):
# hello = "Hello World"
# print(hello + " " + name + "!")
# print(hello)
# hello(name)
# hello1(name,numbers)
# for x in Hello:
# hello("name")

################### return function = Functions send Python value/objects back to the caller.
#                   These values/objects are known as the function's return value

# def multiply(num1,num2):
#     return num1 * num2

# x = multiply(10,99)

# print(x)

################### Keyword arguments = arguments preceded by an identifier when we pass them to a function
#                   the order doesn't matter, unlike positional arguments'
#                   python knows the names of the arguments that our function receives

# def hello(first, middle, last):
#     print("hello " + first + " " + middle + " " + last)

# hello("Gabriel","Legend","Assayag")
# hello(last="Assayag",first="Gabriel",middle="Legend")

# ################### nested functions calls =
#                           function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

# num = input("Enter a positive")
# num = float(num)
# num = abs(num)
# num = round(num)

# print(num)
#### is the same as

# print(round(abs(float(input("Enter a positive")))))

#################### *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments

# def add(num1,num2):
#     sum = num1 + num2
#     return sum
#
# print(add(12,8))
#
# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
#
# print(add(12,8,1,2,3,5,6))

################### **kwargs = parameter that will pack all arguments into a dictionary
#                   useful so that a function can accept a varying amount of keywarod arguments
#
# def hello(**names):
#     print("Hello " + names['first'] + " " + names['last'])
#     print("Hello",end=" ")
#     for key,value in names.items():
#         print(value,end=" ")
#
#
# hello(title="Mister",first="Gabi",last="Assayag",middle="Legend")

################### str.format() = optional method that gives users
#                                   move control when displaying output

# number = 1000
#
# print("The number pie is {:.2f}".format(number))
# print("The number pie is {:,}".format(number))
# print("The number pie is {:b}".format(number))
# print("The number pie is {:o}".format(number))
# print("The number pie is {:X}".format(number))
# print("The number pie is {:E}".format(number))

# animal = "cow"
# item = "moon"
#
# # print("The " + animal+ " jumped over the " + item)
# # print("The {} jumped over the {}".format(animal,item))
# # print("The {0} jumped over the {1}".format(animal,item)) # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) # keyword argument
#
# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# name = "Gabi"
# print("Hello , my name is {}".format(name))
# print("Hello , my name is {name:10},nice to meet you".format(name=name))
# print("Hello , my name is {:<10},nice to meet you".format(name))
# print("Hello , my name is {:>10},nice to meet you".format(name))
# print("Hello , my name is {:^10},nice to meet you".format(name))


################### Random module
# import random
#
# myList = ['rock','paper','scissers']
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
# random.shuffle(cards)
# print(round(random.random()))
# print(random.randint(1,6))
# print(random.choice(myList))
# print(cards)


################### Exception handling = events detected during execution that interrupt the flow of a program

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#
# except ZeroDivisionError as e:
#     print(e)
#     # print("cannot divide number 0")
# except ValueError as e:
#     print(e)
#     # print("one or more of the following parameters isn't valid:" + str(numerator) + str(denominator))
# except Exception as e:
#     print(e)
#     print("Nope")
# else:
#     print(result)
# finally:
#     print("This is the End")

################### File detection

# import os
#
# path = "/var/log/scripts"
#
# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is a file.")
#     elif os.path.isdir(path):
#         print("That is directory")
# else:
#     print("That location doesnt exists")

################### reading a file
# try:
#     with open('C:\\Users\\gabriel.a\\Desktop\\Test.txt') as file:
#         print(file.read())
#
# except FileNotFoundError:
#     print("File not found")

################### write a file

# text = "Yoooooo\nThis is some text\nhave a good one."
# # text = "Overwritten"
#
# f = open('C:\\Users\\gabriel.a\\Desktop\\Test.txt','x')

# with open('C:\\Users\\gabriel.a\\Desktop\\Test.txt','w') as file:
#     file.write(text)
#     file.read()
#     file.close()
# file = open('C:\\Users\\gabriel.a\\Desktop\\Test.txt','r')
# print(file.read())

# with open('C:\\Users\\gabriel.a\\Desktop\\Test.txt','r') as file:
#     print(file.read())


################### copy a file
# copyfile() = copies content of a file
# copy() =     copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies metadata (file's creation and modification times)
# import shutil
# i = '21'
# shutil.copyfile('C:\\Users\\gabriel.a\\Desktop\\Test.txt','C:\\Users\\gabriel.a\\Desktop\\Test'+ i +'.txt') # src.dst

################### Move a file

# import os
#
# source = "C:\\Users\\gabriel.a\\PycharmProjects\\pythonProject\\venv\\Folder"
# destination = "C:\\Users\\gabriel.a\\Desktop\\MovingAFolder"
#
# try:
#     if os.path.exists(destination):
#         print("there is already a file there")
#     else:
#         os.replace(source,destination)
#         print("Moved")
# except FileNotFoundError:
#     print(source + " was not found")

################### module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

# import messages as m
# from messages import * # less recommend
# from messages import hello,bye
#
# help("modules")
#
# hello()
# bye()
# m.hello()
# m.bye()

################### rock,paper scissors game

# import random
#
# while True:
#     choices = ["rock","paper","scissors"]
#     computer = random.choice(choices)
#     player = None
#     while player not in choices:
#         player = input("rock paper or scissors?").lower()
#     if player == computer:
#         print("player: ", player)
#         print("computer: ", computer)
#         print("Tie!")
#     elif player == "rock":  # Rock
#         if computer == "paper":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("Computer wins")
#         if computer == "scissors":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("Player wins")
#     elif player == "paper":  # paper
#         if computer == "scissors":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("Computer wins")
#         if computer == "rock":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("Player wins")
#     elif player == "scissors":  # scissors
#         if computer == "rock":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("Computer wins")
#         if computer == "paper":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("Player wins")
#     play_again = input("Play again? (Y/n) ").lower()
#     if play_again !="y":
#         break
# print("Bye!")

################### Quiz game
# ----------------#
# def new_game():
#
#     guesses = []
#     corret_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("--------------")
#         print(key)
#         for i in options[question_num - 1]:
#             print(i)
#         guess = input("Enter (A, B, C or D)").upper()
#         guesses.append(guess)
#         print(questions.get(key),guess)
#         corret_guesses += check_answer(questions.get(key),guess)
#         question_num += 1
#
#     display_score(corret_guesses,guesses)
#
# #----------------#
# def check_answer(answer, guess):
#     if answer == guess:
#         print("Correct!")
#         return 1
#     else:
#         print("Wrong!")
#         return 0
# #----------------#
# def display_score(correct_guesses,guesses):
#     print("#----------------#")
#     print("Results!")
#     print("#----------------#")
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
#
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int((correct_guesses / len(questions))*100)
#     print("Your score is: " + str(score)+"%")
# #----------------#
# def play_again():
#     response = input("Play again? Y/n ").lower()
#     if response == "y":
#         return True
#     else:
#         return False
# #----------------#
# #------Dictionary names questions----------#
# questions = {
#     "Who created Python?: ": "A",
#     "What year was Python created?: ":"B",
#     "Python is tributed to which comedy group?: ":"C",
#     "Is the Earth round?: ":"A"
# }
#
# options = [["A. Guido van Rossum","B. Elon Musk","C. Bill Gates","D. Mark Zuckerburg"],
#            ["A. 1989","B. 1991","C. 2000","D. 2016"],
#            ["A. Lonly Island","B. Smosh","C. Monty Python","D. SNL"],
#            ["A. Yes","B. No","C. sometimes","D. What is Earth?"]]
#
# new_game()
#
# while play_again():
#     new_game()
#
# print("BYEEEEEE!!!!!")

################# P-OOP - Object Oriented Programming
# Objects that mimic real life objects
# attributes = is/has
# ex. name, age, height
# method = actions
# ex. eat, sleep, make Videos
# class - blueprint

# class Car:
#     #
#     # make = None
#     # model = None
#     # year = None
#     # color = None
#     #
#     def __init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def drive(self):
#         print("This "+self.model+" is driving")
#
#     def stop(self):
#         print("This "+self.make+" is stopped")
#
#
# car_1 = Car('Chevy',"Corvet",2021,"blue")
# car_2 = Car('Fort',"mosteng",2022,"red")
#
# # print(car_1.make)
# # print(car_1.model)
# # print(car_1.year)
# # print(car_1.color)
#
#
# car_1.drive()
# car_1.stop()

# ########################## Class variable
# class Car:
#
#     wheels = 4 # class variable
#
#     def __init__(self, make, model, year, color):
#         self.make = make    #instance variable
#         self.model = model  #instance variable
#         self.year = year    #instance variable
#         self.color = color  #instance variable

# car_1 = Car('Chevy',"Corvet",2021,"blue")
# car_2 = Car('Fort',"mosteng",2022,"red")
# car_2.wheels = 2
# print(car_1.wheels)
# print(car_2.wheels)
#

# print(Car.wheels)

# ########################## Inheritance

# class Animal:
#
#     alive = True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
# class Rabbit(Animal):
#     def run(self):
#         print("this rabbit is running")
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
# rabbit.run()
# fish.swim()
# hawk.fly()

# ########################## Multilevel Inheritance
# when a derived (child) class inherits another derived (child) class

# class Organism:
#
#     alive = True
#
# class Animal(Organism):
#
#     def eat(self):
#         print("This animal is eating")
#
# class Dog(Animal):
#
#     def bark(self):
#         print("This dog is barking!")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

# ########################## Multiple Inheritance
# when a child class is derived from more than one parent class.
#
# class Prey:
#
#     def flee(self):
#         print("This animal is fleeing")
#
# class Predator:
#
#     def hunt(self):
#         print("This animal is hunt")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Predator ,Prey):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()

# ########################## Method overriding
#

# class Animal():
#
#     def eat(self):
#         print("This animal is eating")
#
# class Rabbit(Animal):
#
#     def eat(self):
#         print("This Rabbit eating carrot")
#
# rabbit = Rabbit()
# rabbit.eat()

# ########################## Method chaining
# Calling multiple methods sequentially
# each call preforms an action on the same object and return self.

# class Car:
#
#     def turn_on(self):
#         print("You start the engine")
#         return self # return class name - Car
#
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brakes")
#         return self
#
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
#
# car = Car()
#
# #car.turn_on().drive()
#
# # car.brake().turn_on()
#
# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()


# ########################## super() function
# Function used to give access to the methods of a parent class
# returns a temporary object of a parent class when used

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def area(self):
#         return self.length * self.width
#
# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
#
#     def volume(self):
#         return self.length * self.width * self.height
#
# squere = Square(3,3)
# cube = Cube(3,3,3)
# print(cube.volume())
# print(squere.area())

# ########################## abstract classes
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     @abstractmethod  # "Telling the children - If you are going to inherit
#     # from me. Then you need to override this(go) abstract method.
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
#
# class Car(Vehicle):
#
#     def go(self):
#         print("You drive the car")
#
#     def stop(self):
#         print("Car Stopped")
#
#
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("You drive the motorcycle")
#
#     def stop(self):
#         print("motorcycle Stopped")
#
#
# # vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# # vehicle.go()
# # vehicle.stop()
# car.go()
# car.stop()
# motorcycle.go()
# motorcycle.stop()


# ########################## objects as arguments

# class Car:
#
#     color = None
#
# class Motorcycle:
#
#     color = None
#
# def change_color(vehicle,color):
#
#     vehicle.color = color
#
#
# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# bike1 = Motorcycle()
#
# change_color(car1,"red")
# change_color(car2,"blue")
# change_color(car3,"yellow")
# change_color(bike1,"black")
#
# print(car1.color)
# print(car2.color)
# print(car3.color)
# print(bike1.color)

# ########################## duck typing
#   Concept where the class of an object is less important than the methods
#   class type is not checked if minimum methods/attributes are present
#   "If it walks like a duck, and it quacks like a duck, then it must be a duck"

# class Duck:
#
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is talking")
#
#
# class Chicken:
#
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
#
# class Person:
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")
#
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)

# ########################## walrus operator


# ########################## dictionary comprehension = create dictionaries
# using an expression can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}

# cities_in_F = {'New York': 32, 'Boston': 75,'Los Angeles': 100, 'Chicago': 50}
#
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#
# print(cities_in_C)
#
# weather = {'New York': 'snowing', 'Boston': 'sunny','Los Angeles': 'sunny', 'Chicago': 'cloudy'}
# # sunny_weather = {key: value for (key,value) in weather.items() if value == 'sunny'}
#
# cities = {'New York': 32, 'Boston': 75,'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("Warm" if value >=40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

#################### GUI ####################
from tkinter import *

# widget = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

# window = Tk() # instantiate an instance of a window
# window.geometry("420x420") # measurement
# window.title("VC") # change window title
#
# icon = PhotoImage(file='voicentericon.png') # convort to photo image # changing icon
# window.iconphoto(True,icon)
# window.config(background="black") # "#000000"
#
#
# window.mainloop() # place window on computer screen. listens for events
#################### Labels ####################
# from tkinter import *
#
# # label = an area widget that holds text and / or an image within a window
#
# window = Tk()
# window.geometry("1420x1420")
# photo = PhotoImage(file="sharingan.png")
# label = Label(master=window,
#               text="Hello World!",
#               font=('Ariel',40,'bold'),
#               fg='#8b0000',
#               bg='black',
#               relief=SUNKEN,
#               bd=10,
#               padx=4,
#               pady=8,
#               image=photo,
#               compound="bottom")
# label.pack()
# # label.place(x=0,y=0)
# window.mainloop()

#################### Buttons ####################
# from tkinter import *
#
#
# count = 0
# # button = you click it , then it does stuff.
# def click():
#     global count
#     count += 1
#     print(count)
#     if count == 10:
#         exit()
#
#
# window = Tk()
# photo = PhotoImage(file="Like.PNG")
#
# button = Button(master=window,
#                 text="Click ME !",
#                 command=click,
#                 font=("Comic Sans",30),
#                 fg="#8c0000",
#                 bg="black",
#                 activeforeground="#8c0110",
#                 activebackground="black",
#                 image=photo,
#                 compound="center")
# button.pack()
#
# window.mainloop()
#
#
#################### Entrybox ####################
# from tkinter import *
# # entry widget = textbox that accepts a single line of user input
#
# def submit():
#     username = entry.get()
#     print(f"Hello {username}")
#     entry.config(state=DISABLED)
# def delete():
#     entry.delete(0,END)
#
# def backspace():
#     entry.delete(len(entry.get())-1 ,END)
# window = Tk()
#
# entry = Entry(window,
#               font=("Ariel",15),
#               fg="#00FF00",
#               bg="black",
#               show="*")
# # entry.insert(0,"Spongebob")
# entry.pack(side=LEFT)
#
# submit_button = Button(window,text="Submit",command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(window,text="Delete",command=delete)
# delete_button.pack(side=RIGHT)
#
# backspace_button = Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=RIGHT)
#
#
# window.mainloop()


#################### checkbox ####################
from tkinter import *
















