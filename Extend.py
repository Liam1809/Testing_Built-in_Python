#  extend ( list )
#  Extend list l by appending list elements.
#  Note the difference from append( object ), which treats the argument as a single list object.
list1 = [1, 2, 3]
list1.extend([4, 5, 6])
list1.extend(["My", ["Name", ["is", "Liam"]]])

print(list1)