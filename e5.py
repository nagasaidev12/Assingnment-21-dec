Dict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: Dict[k] for k in keys}
print(newDict)
