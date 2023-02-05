# If/ Else conditions are used to decide to do something based on something being true or false

x_ebs = 9
y_ebs = 6 

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_ebs > y_ebs:
     print(f'{x_ebs} is greater than {y_ebs}')

# IF/else
if x_ebs > y_ebs:
     print(f'{x_ebs} is greater than {y_ebs}')

else: 
     print(f'{y_ebs} is greater than {x_ebs}')

# elif
if x_ebs > y_ebs:
     print(f'{x_ebs} is greater than {y_ebs}')

elif x_ebs == y_ebs: 
     print(f'{x_ebs} is equal to {y_ebs}')

else:
     print(f'{y_ebs} is greater than {x_ebs}')

# Nested if
if x_ebs > 2:
    if x_ebs <= 10:
         print(f'{x_ebs} is greather than 2 and less than or equal than 10')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_ebs > 2 and x_ebs <=10:
    print(f'{x_ebs} is greather than 2 and less than or equal than 10')

# or
if x_ebs > 2 or x_ebs <=10:
    print(f'{x_ebs} is greather than 2 or less than or equal than 10')

# not
if not x_ebs == y_ebs:
    print(f'{x_ebs} is not equal to {y_ebs}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_ebs = [1, 2, 3, 4, 5]

# in
if x_ebs in numbers_ebs:
    print(x_ebs in numbers_ebs)

# not in
if x_ebs not in numbers_ebs:
    print(x_ebs not in numbers_ebs)  

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

#is
if x_ebs is y_ebs:
    print(x_ebs is y_ebs)

#is not
if x_ebs is not y_ebs:
    print(x_ebs is not y_ebs)