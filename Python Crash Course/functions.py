# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name_ebs='Caesar'):
    print(f'Hello{name_ebs}')

# Return Values
def getSum(num1_ebs, num2_ebs):
    total_ebs = num1_ebs + num2_ebs
    return total_ebs


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


getSum =lambda num1_ebs, num2_ebs : num1_ebs + num2_ebs

print(getSum(15, 5))