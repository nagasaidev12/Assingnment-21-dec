sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
sample_list = list(set(sample_list))
print("unique items", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Min: ", min(t))
print("Max: ", max(t))
