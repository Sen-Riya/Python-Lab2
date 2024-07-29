# (1)

#(a) Develop a module called module_ListFunction that includes the following functions:
# i. A function to find the maximum value in a given list.
# ii. A function to find the minimum value in a given list.
# iii. A function to calculate the sum of all elements in a list.
# iv. A function to compute the average of the list.
# v. A function to determine the median of a list.
# Additionally, create lists using Python comprehension for various scenarios and demonstrate the use of the module functions with these lists.

#(b) Create another script named ‘main_ListOpeartions.py’ and Imports the
# ‘module_ListFunction’ to it.

#(c) Demonstrate the execution of each function with suitable examples.


def max_value(list):
    if not list:
        return None
    else:
        return max(list)

def min_value(list):
    if not list:
        return None
    return min(list)

def sum_value(list):
    return sum(list)

def average_value(list):
    if not list:
        return None
    return sum(list) / len(list)

def median_value(list):
    if not list:
        return None
    sorted_list = sorted(list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]
