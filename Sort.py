# Sometimes, we want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

# We can sort a list in place using .sort(). Suppose that we have a list of names:

# names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# print(names)
# This would print:

# ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# Now we apply .sort():

# names.sort()
# print(names)
# And we get:

# ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
# Notice that sort goes after our list, names. If we try sort(names), we will get a NameError.

# sort does not return anything. So, if we try to assign names.sort() to a variable, our new variable would be None:

# sorted_names = names.sort()
# print(sorted_names)
# This prints:

# None
# Although sorted_names is None, the line sorted_names = names.sort() still edited names:

# >>> print(names)
# ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()
print(addresses)
### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(sorted_cities)
print(cities)

# we can sort in reverse order within sort() by using reverse parameter
list1 = [14, 45, 98, 23, 77, 32, 15, 22, 8, 33, 21, 64]
list1.sort()
print(list1)
# [8, 14, 15, 21, 22, 23, 32, 33, 45, 64, 77, 98]

ist1 = [14, 45, 98, 23, 77, 32, 15, 22, 8, 33, 21, 64]
list1.sort(reverse=True)
print(list1)
# [98, 77, 64, 45, 33, 32, 23, 22, 21, 15, 14, 8]

# sort list in list
# use key parameter 
def f(x):
    return x[1]
    
names_and_age = [["Sam" , 23], ["Vik", 30], ["Phil", 26], ["John", 18]]
names_and_age.sort(key = f)
print(names_and_age)

# use key parameter with lambda to define function in one line
names_and_age.sort(key = lambda x : x[1])
print(names_and_age)