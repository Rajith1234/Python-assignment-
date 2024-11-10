# Example dictionary
my_dict = {'banana': 3, 'apple': 4, 'orange': 2, 'mango': 1}

# Sort the dictionary by keys
sorted_dict_by_key = {k: my_dict[k] for k in sorted(my_dict)}

print("Sorted by Keys:", sorted_dict_by_key)
