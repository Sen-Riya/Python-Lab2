import Q2a_module as mod2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


mod2.add_element(set1, 6)
print("Set1 after the addition of 6 in it:", set1)


mod2.remove_element(set1, 6)
print("Set1 after removing 6 from it:", set1)


union,intersection = mod2.union_intersection(set1, set2)
print("Union of Set1 and Set2:", union)
print("Intersection of Set1 and Set2:", intersection)


difference = mod2.difference(set1, set2)
print("Set1 - Set2:", difference)

print("Is Set1 a subset of Set2?")
is_a_subset = mod2.is_a_subset(set1, set2)

length = mod2.length_of_set(set1)
print("Length of Set1 is:", length)


sym_diff = mod2.symmetric_difference(set1, set2)
print("Symmetric difference of Set1 and Set2 is :", sym_diff)

