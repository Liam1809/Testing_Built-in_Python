list2 = [ 10, 20, 30, 40, 50, 60, 70 ]

# remove requires argument(value) --> remove the wanted value
list2.remove(60)
list2.remove(40)
list2.remove(10)
for element in list2:
    print(element, end = " ")