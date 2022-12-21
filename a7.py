set1 = {57, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
print("First set is subset of second set -", set1.issubset(set2))
print("Second set is subset of First set - ", set2.issubset(set1))
print("First set is Super set of second set - ", set1.issuperset(set2))
print("Second set is Super set of First set - ", set2.issuperset(set1))
if set1.issubset(set2):
    set1.clear()
elif set2.issubset(set1):
    set2.clear()
print("First Set ", set1)
print("Second Set ",set2)
 
