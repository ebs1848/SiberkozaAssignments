# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON_ebs = '{"first_name": "Johnny", "last_name": "Joestar", "age": 30}'

# Parse to dict
user_ebs = json.loads(userJSON_ebs)

print(user_ebs)
print(user_ebs['first_name'])

car_ebs = {'make': 'Ford', 'model': 'Mustang', 'Year': 1970}

carJSON_ebs = json.dumps(car_ebs)

print(carJSON_ebs)