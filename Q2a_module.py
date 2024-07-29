# (2) Write a Python program to create a module that performs various set operations.
# a. Write a function to add an element to a set, ensuring no errors if the element is already present.
# b. Write a function to remove an element from a set, ensuring no errors if the element is not present.
# c. Write a function to return the union and intersection of two sets, handling empty sets correctly.
# d. Write a function to return the difference S1−S2, handling empty sets correctly.
# e. Write a function to check if set S1 is a subset of set S2, handling empty sets correctly.
# f. Write a function to find the length of a set without using the len() function.
# g. Write a function to compute the symmetric difference of two sets.
# h. Write a function to compute the power set of a given set.
# i. Write a function to get all unique subsets of a given set.
# Implement this module and demonstrate it by using adequate examples.

def add_element(set, element):
    set.add(element)
 
def remove_element(set, element):
    set.discard(element)

def union_intersection(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    return union, intersection

def difference(set1, set2):
    return set1 - set2

def is_a_subset(set1, set2):
    if set1 <= set2:
        print(f"Yes , {set1} is a subset of {set2}")
    else:
        print(f"No , {set1} is not a subset of {set2}")

def length_of_set(set):
    count = 0
    for _ in set:
        count += 1
    return count

def symmetric_difference(set1, set2):
    return set1 ^ set2
 