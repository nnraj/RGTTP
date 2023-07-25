"""
  Lesson 1: ex2.py
"""

# Here is my shopping list:
#
# 2.99 Apples
# 1.79 Milk
# 3.49 Bread
# 6.99 Chicken
# 2.49 Pasta

# 1. Make a python list of the 5 items above and print it out.

# INSERT YOUR CODE HERE
shop_list: list = ["Apples", "Milk", "Bread", "Chicken", "Pasta"]
print(shop_list)



# 2. Use python as your calculator and print out the total cost of
#    all items on shopping list.

# INSERT YOUR CODE HERE
shop_list: dict = {
    'Apples': 2.99, 
    'Milk': 1.79, 
    'Bread': 3.49, 
    'Chicken': 6.99, 
    'Pasta': 2.49
}
print(sum(shop_list.values()))



# 3. I have decided that we need 5 cartons of milk, can you recalculate
#    it and print it out again?

# INSERT YOUR CODE HERE
shop_list: dict = {
    'Apples': 2.99, 
    'Milk': 1.79, 
    'Bread': 3.49, 
    'Chicken': 6.99, 
    'Pasta': 2.49
}
total_value: float = shop_list['Apples'] 
                     + shop_list['Milk']*5 
                     + shop_list['Bread'] 
                     + shop_list['Chicken'] 
                     + shop_list['Pasta']
print(total_value)

# 4. Print out every item of your shopping list on a new line.

# INSERT YOUR CODE HERE
shop_list: dict = {
    'Apples': 2.99, 
    'Milk': 1.79, 
    'Bread': 3.49, 
    'Chicken': 6.99, 
    'Pasta': 2.49
}
k: str # variable used in loop statement below
v: float # variable used in loop statement below
for k, v in shop_list.items()
    print(k, v)
    