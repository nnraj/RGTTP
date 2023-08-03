"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}


# INSERT YOUR CODE HERE

versions: dict = {'Stein': 15, 'Train': 16, 'Wallaby': 17}
print("{Stein}, {Train}, {Wallaby}".format(**versions))


# 2. Print {} around the version numbers.

# INSERT YOUR CODE HERE
#versions2: dict = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

print("{{{Stein}}}, {{{Train}}}, {{{Wallaby}}}".format(**versions))

# 3. Print numbers in decimal, byte and hexadecimal form.

# INSERT YOUR CODE HERE


print("{Stein:.1f}, {Train:.1f}, {Wallaby:.1f}".format(**versions))
print("{Stein:b}, {Train:b}, {Wallaby:b}".format(**versions))
print("{Stein:X}, {Train:X}, {Wallaby:X}".format(**versions))
