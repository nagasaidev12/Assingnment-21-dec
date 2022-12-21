keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = dict()

for i in range(len(keys)):
    dict.update({keys[i]: values[i]})
print(dict)
