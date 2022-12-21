roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
dict1 = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
roll_number[:] = [item for item in roll_number if item in dict1.values()]
print("after removing unwanted elements from list:", roll_number)
