"""This program converts celsius to fahrenheit"""
Celsius = 20
Fahrenheit = (Celsius * 9/5) + 32
# The above formula is the calculation used to convert celsius into fahrenheit.
print (Celsius)
print (Fahrenheit)
#This prints both variables into the terminal
"""Changing the variable on celsius changes fahrenheit due to it being dependent on celsius for the calculation."""
String = ("This is a string")
Integer = 2
Float = 3.14
Boolean = True
print (String)
print (type(String))
print (f"This {Integer} is an integer it is a whole number data type.")
print (type(Integer))
print (f"This {Float} is a float which is a decimal data type")
print (type(Float))
print (f"This {Boolean} is a Boolean cause it can either be true or false")
print (type(Boolean))
Name = ("Logan")
Course = ("Computer science")
Program_Language = ("Python")
p = ("My name is ") + Name
print (p)
print (f"Hi my name is {Name} my favourite course is {Course}")
txt = "Hi my name is {Fname} and I LOVE {Fcourse}".format(Fname = "Logan", Fcourse = "Computer science")
print (txt)
Age = int(input("What is your age in years?"))
if Age < 18:
 print ("You are a minor")
else: print ("You are an adult")