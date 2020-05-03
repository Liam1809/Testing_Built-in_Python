list2 = [ 10, 20, 30, 40, 50, 60, 70 ]
# del list[start:end] start: inclusive end: exclusive
del list2[1:3]
for element in list2:
    print(element, end = " ")
# delete all elements in list
del list2[:]
for element in list2:
    print(element, end = " ")