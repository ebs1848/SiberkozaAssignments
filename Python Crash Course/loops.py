# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_ebs = ['Joseph', 'Jonathan', 'Anastasia', 'Irene']

# break
for person_ebs in people_ebs:
    if person_ebs == 'Joseph':
        break
    print(f'Current Person: {person_ebs}')

# countinue
for person_ebs in people_ebs:
    if person_ebs == 'Joseph':
        continue
    print(f'Current Person: {person_ebs}')
 
#range
for i_ebs in range(0,10):
    print(f'Number: {i_ebs}')

# While loops execute a set of statements as long as a condition is true.

count_ebs = 0
while count_ebs < 10:
    print(f'Count: {count_ebs}')
    count_ebs += 1