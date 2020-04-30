# Testing append list Function
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
empty_list = []

for element in list:
    empty_list.append(element)
print(empty_list)

# append ( object )
# Update list l by appending object to end of the list.

# append only 1 object at a time
empty_list.append(10)
print(empty_list)

# append several data types
# Number
empty_list.append(20)
# String
empty_list.append("My")
empty_list.append("name")
# list
empty_list.append(["is", "Liam"])
# boolean
empty_list.append(True)
print(empty_list)