import Q1a_module_ListFunction as mod1 
list1 = [x for x in range(10)]  
list2 = [x * x for x in range(10)]
list3 = [x for x in range(1, 11)] 

# Using the module
print("List1:", list1)
print("Maximum value in List1:", mod1.max_value(list1))
print("Minimum value in List1:", mod1.min_value(list1))
print("Sum of List1:", mod1.sum_value(list1))
print("Average of List1:", mod1.average_value(list1))
print("Median of List1:", mod1.median_value(list1))

print("\nList2:", list2)
print("Maximum value in List2:", mod1.max_value(list2))
print("Minimum value in List2:", mod1.min_value(list2))
print("Sum of List2:", mod1.sum_value(list2))
print("Average of List2:", mod1.average_value(list2))
print("Median of List2:", mod1.median_value(list2))

print("\nList3:", list3)
print("Maximum value in List3:", mod1.max_value(list3))
print("Minimum value in List3:", mod1.min_value(list3))
print("Sum of List3:", mod1.sum_value(list3))
print("Average of List3:", mod1.average_value(list3))
print("Median of List3:", mod1.median_value(list3))
