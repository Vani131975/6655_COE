list1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
set1 = set()
unique_list = [x for x in list1 if not (x in set1 or set1.add(x))]
print("the list after removing duplicates is: ", (unique_list))
