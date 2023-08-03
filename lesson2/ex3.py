"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

# INSERT YOUR CODE HERE

sample_list: list = ['Tom', 83, 'House cat']
print("{} is my favorite cartoon  character,"
      "he is {} years young and works as a {}!"
      .format(*sample_list))


# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

# INSERT YOUR CODE HERE

book_dict: dict = {'title': "Pale Blue Dot:" 
                    "A Vision of the Human Future in Space",
                   'author': "Carl Sagan", 
                   'publication_year': 1994}

print("The guidebook {title} by {author} was published in {publication_year}"
      .format(**book_dict))
# print("The guidebook {0} by {1} was published in {2}"
#      .format(book_dict['title'],book_dict["author"], book_dict["publication_year"]))


# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

# INSERT YOUR CODE HERE

space_ship: dict = {'name': "The Endurance",
                    'type': "Modular spaceship",
                    'purpose': "travelling through wormhole"}

print("The spaceship is called {ship_name}. "
      "It is a {ship_type} used for {ship_purpose}."
      .format(ship_name=space_ship['name'],
              ship_type=space_ship['type'],
              ship_purpose=space_ship['purpose']))

# print("The spaceship is called {ship[name]}. "
#      "It is a {ship[type]} used for {ship[purpose]}"
# .format(ship=space_ship))
