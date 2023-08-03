"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

name: str = "pluto"
age: int = 20
# example using placeholder
print("{} is {} years old".format(name, age))

# example using f string
#   print(f"{name} is {age} years old")

# example using positional arguments
#   print("{0} is {1} years old".format(name,age))

# example using name - keyword argument
#   print("{person} is {years} years old".format(person=name, years=age))

# example using list for storing variables
#   name_list: list = ["Mercury", "Venus"]
#   age: int = 30
# prints all elements of list
#   print("{person} is {years} years old".format(person=name_list,years=age))

# print individual elements with the help of index
#   print("{person[1]} is {years} years old".format(person=name_list,years=age))

# example using dictionary  for storing variables, when accessing the 
#   dictionay inside the print statement by using the key. 

#   planets_dict: dict = {"Earth": 40, "Mars": 50}
#   print("Earth is {name[Earth]} years old".format(name=planets_dict))
#   print("Mars is {name[Mars]} years old".format(name=planets_dict))

# example using unpacking dictionary using `**` inside format method, 
#   when using these 2 wildcards, it unpacks the dictionary into 
#   individual variables like `Jupiter = 40` and `Saturn = 50`
#   large_planets_dict: dict = {"Jupiter": 60, "Saturn": 75}
#   print("Jupiter is {Jupiter} years old".format(**large_planets_dict))

# example using unpacking list using `*` here we use single wildcard for list
#   large_planets_list: list = ["Jupiter", "Saturn"]
#   large_planets_age: int = 75
#   print("{} is {} years old".format(large_planets_list[0],large_planets_age))
#   print("{} is {} years old".format(large_planets_list[1],large_planets_age))
#   print("{} is {} years old".format(*large_planets_list))
#   o/p --> Jupiter is Saturn years old


# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.


my_dict: dict = {13: "Queens", 15: "Stein", 16: "Train"}

print("RHOSP version 13's upstream code"
  "name is {name[13]:<25}! output is aligned left with 25 padding"
      .format(name=my_dict))

print("RHOSP version 15's upstream code"
"name is {name[15]:>25}! output is aligned right with 25 padding"
      .format(name=my_dict))

print("RHOSP version 16's upstream code"
"name is {name[16]:^25}! output is aligned center with 25 padding"
      .format(name=my_dict))


# 3. Show different representations of an integer.


number: int  = 42

# representing as it is
print("The answer to everything is {}".format(number))

# representing with explicit sign
print("The answer to everything is {:+}".format(number))

# representing with padded preceeding`0` 
print("The answer to everything is {:03}".format(number))

# representing with positive sign for padded positive number  preceeding `0`
print("The answer to everything is {:=+04}".format(number))

# representing wiith negative sign
#   number: int  = -42
#   print("The answer to everything is {:-}".format(number))

# 4. Format a floating-point number with fixed precision.

# INSERT YOUR CODE HERE

# printing float numbers with fixed precision
pi: float = 3.14159265
sentence: str = f'Value of Pi is {pi:.3f}'
print(sentence)
