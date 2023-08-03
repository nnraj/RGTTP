"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

# INSERT YOUR CODE HERE

animal: str = "cow"
item: str = "moon"

print("The {} jumped over the {}!".format(animal, item))


# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

# INSERT YOUR CODE HERE

panic_stmt1: str = "Don't"
panic_stmt2: str = "Panic!"

print("{0} {1}".format(panic_stmt1, panic_stmt2))


# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

# INSERT YOUR CODE HERE

name: str = "Messi"
quality: str = "great"

print(" {who} is really {what}".format(who=name, what=quality))
