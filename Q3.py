# (3) Write a program to create functions that can accept multiple dictionaries as arguments using ‘*args’, and     perform various operations on them.
# (a) Write a function, say, ‘merging_Dict(*args)’ that takes multiple dictionaries and merge them.
# (b) Write a function which can find common keys in multiple dictionaries.
# (c) Create a function to invert a dictionary, swapping keys and values. If multiple keys have the same value, group these keys in a list in the inverted dictionary. Implement and demonstrate this with examples.
# (d)Write a function to find common key-value pairs across multiple dictionaries.

def merging_Dict(*args):
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def common_keys(*args):
    if not args:
        return set()
    common_keys = set(args[0].keys())
    for d in args[1:]:
        common_keys &= set(d.keys())
    return common_keys

def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = key
        else:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
    return inverted_dict

def common_key_value_pairs(*args):
    if not args:
        return {}
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs &= set(d.items())
    return dict(common_pairs)

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'a': 1, 'b': 2, 'e': 6}


merged = merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)


common_keys_result = common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys_result)


inverted = invert_dict(dict1)
print("Inverted Dictionary:", inverted)


common_pairs = common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_pairs)
