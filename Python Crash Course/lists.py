# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers_ebs = [1, 2, 3, 4, 5]
fruits_ebs = ['Apples', 'Oranges', 'Grapes', 'Pears',]

# Use a constructor 
# numbers2_ebs = list((1, 2, 3, 4, 5))

# Get a value
print(fruits_ebs[1])

# Get lenght
print(len(fruits_ebs))

# Append to list
fruits_ebs.append('Mangos')

# Remove from list
fruits_ebs.remove('Apples')

# Insert into list
fruits_ebs.insert(2, 'Strawberries')

# Change value
fruits_ebs[0] = 'Blueberries'

# Remove with pop
fruits_ebs.pop(2)

# Reverse list
fruits_ebs.reverse()

# Sort list
fruits_ebs.sort()

# Reverse sort
fruits_ebs.sort(reverse=True)

print(fruits_ebs)