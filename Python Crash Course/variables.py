# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x_ebs = 25             #int
# y_ebs = 7.5           #float
# name_ebs = 'Emir'     #str
# is_cool_ebs = True    #bool

# Multiple assignment
x_ebs, y_ebs, name_ebs, is_cool_ebs = (25, 7.5, 'Emir', True)

# Basic math
a_ebs = x_ebs + y_ebs

# Casting
x_ebs = str(x_ebs)
y_ebs = int(y_ebs)
z_ebs = float(y_ebs)

print(type(z_ebs), z_ebs)
