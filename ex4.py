"""
  Lesson 1: ex4.py
"""

# 1. Create a new list with the following values:
#    Apple, Milk, Bread, Chicken and Pasta

# INSERT YOUR CODE HERE
shop_list: list = ['Apple', 'Milk', 'Bread', 'Chicken', 'Pasta']

# 2. Write a check to see if Orange is in the shopping list or not.

# INSERT YOUR CODE HERE
shop_list: list = ['Apple', 'Milk', 'Bread', 'Chicken', 'Pasta']
fruit: str = "Orange"
if fruit in shop_list:
  print(f" {fruit} is in the list")
else:
  print(f" {fruit} is NOT in the list")

# 3. Write a function "in_shopping_list" that takes a item such as
#    orange, and returns True or False.
#    Depending whether the item is in the list or not.

# INSERT YOUR CODE HERE


def in_shopping_list(fruit: str) -> bool:
    shop_list: list = ['Apple', 'Milk', 'Bread', 'Chicken', 'Pasta']
    return bool(fruit in shop_list)


print(in_shopping_list('Apple'))


# 4. Write a function "show_shopping_list" that will return a
#    shopping list and print it out on the screen.

# INSERT YOUR CODE HERE


def show_shopping_list() -> list:
    shop_list: list = ['Apple', 'Milk', 'Bread', 'Chicken','Pasta']
    return shop_list

print(show_shopping_list())


# 5. Create a list of the following values: 2.99 1.79 3.49 6.99 2.49

# INSERT YOUR CODE HERE

my_list: list = [2.99, 1.79, 3.49, 6.99, 2.49]

# 6. Create a function price_checker, and pass this list as
#    an argument and let the function return the cheapest price.#

# INSERT YOUR CODE HERE



def price_checker(pr_list: list) -> float:
    pr_list.sort()
    return pr_list[0]


my_list: list = [2.99, 1.79, 3.49, 6.99, 2.49]
print(price_checker(my_list))


    


# 7. Write another function show_price, that will call your
#    price_checker function and uses the result to
#    print the cheapest price.

# INSERT YOUR CODE HERE


def price_checker(pr_list: list) -> float:
    pr_list.sort()
    return pr_list[0]


def show_price(sh_list: list) -> None:
    print(price_checker(sh_list))  
  

my_list: list = [2.99, 1.79, 3.49, 6.99, 2.49]
show_price(my_list)