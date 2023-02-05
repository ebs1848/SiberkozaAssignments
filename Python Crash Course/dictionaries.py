# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person_ebs = {
    'first_name': 'Emir',
    'second_name': 'Behic',
    'last_name': 'Saglam',
    'age': 22 
}

# Use constructor
# person2_ebs = dict(first_name_ebs='Emir', second_name_ebs='Behic', last_name_ebs='Saglam')

# Get value
print(person_ebs['first_name'])
print(person_ebs.get('last_name'))

# Add key/value
person_ebs['phone'] = '5555555555'

# Get dict keys
print(person_ebs.keys())

# Get dict items
print(person_ebs.items())

# Copy dict 
person2_ebs = person_ebs.copy()
person2_ebs['city'] = 'Ankara'

# Remove item
del(person_ebs['age'])
person_ebs.pop('phone')

# Clear
person_ebs.clear()

#Get lenght
print(len(person2_ebs))

# List of dict
people_ebs = [
    {'name': 'Jotaro', 'age': 35},
    {'name': 'Jolyne', 'age': 45}
]

print(people_ebs[2]['name'])