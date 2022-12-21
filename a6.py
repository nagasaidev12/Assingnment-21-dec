set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
intersection = set1.intersection(set2)
print("Intersection is ", intersection)
for item in intersection:
    set1.remove(item)

print("First Set after removing common element ", set1)
 
