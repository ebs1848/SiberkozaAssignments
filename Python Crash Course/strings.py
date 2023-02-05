# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_ebs = 'Emir'
age_ebs = 22

# Concatenate
# print('Hello, my name is' +name_ebs+ 'and I am' +str(age_ebs)+)

# String Formatting

# Arguments by position
print('My name is {name_ebs} and I am {age_ebs}'.format(name_ebs=name_ebs, age_ebs=age_ebs))

# F-String (3.6+)
print(f'Hello, my name is {name_ebs} and I am {age_ebs}')

# String Methods

s_ebs = 'hello world'

# Capitalize string
print(s_ebs.capitalize())

# Make all uppercase
print(s_ebs.upper())

# Make all lower
print(s_ebs.lower())

# Swap case
print(s_ebs.swapcase())

# Get length
print(len(s_ebs))

# Replace
print(s_ebs.replace('world', 'everyone'))

# Count
sub_ebs = 'h'
print(s_ebs.count(sub_ebs))

# Starts with
print(s_ebs.startswith('hello'))

# Ends with
print(s_ebs.endswith('goodbye'))

# Split into a list
print(s_ebs.split())

# Find position
print(s_ebs.find('r'))

# Is all alphanumeric
print(s_ebs.isalnum())

# Is all alphabetic
print(s_ebs.isalpha())

# Is all numeric
print(s_ebs.isnumeric())