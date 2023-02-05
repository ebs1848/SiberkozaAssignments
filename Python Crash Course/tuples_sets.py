# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits_ebs = ('Apples', 'Oranges', 'Grapes')
# fruits2_ebs = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs traling comma
fruits2_ebs = ('Apples')

# Get value
print(fruits_ebs[1])

# Can't change value
# fruits_ebs[0] = 'Pears'

# Delete tuple
del fruits2_ebs

# Get lenght
print(len(fruits_ebs))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set_ebs ={'Apples', 'Oranges', 'Grapes'}

# Add to set
fruits_set_ebs.add('Mango')

# Remove from set
fruits_set_ebs.remove('Apples')

# Add duplicate
fruits_set_ebs.add('Oranges')

# Clear set
# fruits_set_ebs.clear()

# Delete
# del fruits_set_ebs

print(fruits_set_ebs)