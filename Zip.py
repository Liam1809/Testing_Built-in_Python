# The zip() function will only iterate over the smallest list passed. 
# If given lists of different lengths, the resulting combination will only be as long as the smallest list passed
list1 = ["Cat", "Dog", "Bird", "Snake", "Elephant", "Tiger", "Giraffe"]
list2 = [1, 2, 3, 4, 5, 6, 7]
# zip each element of both list into a list
empty1 = zip(list1, list2)
# only print out its address
print(empty1)
# should parse it into a list 
# list with tuples
empty2 = list(zip(list1, list2))
print(empty2)
# list with lists
empty3 = list([list1,list2] for (list1, list2) in zip(list1, list2))
print(empty3)