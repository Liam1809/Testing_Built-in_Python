list2 = [ 10, 20, 30, 40, 50, 60, 70 ]

# without argument --> pop the last element
list2.pop()
for element in list2:
    print(element, end = " ")
print("\n")
# with argument(index) --> pop the element at index
list2.pop(0)
list2.pop(4)
list2.pop(2)
for element in list2:
    print(element, end = " ")