
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict:
    if value <= 2:
        new_dict = value

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    if value <= 2:
        new_dict[key] = value

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict:
     if value <= 2:
         new_dict = value

