# insert ( index , object )
# Update list l by inserting object before position index .
#  If index is greater than len( list ), the object is simply appended.
#   If index is less than zero, the object is prepended.

#  insert(a, x) :- This function inserts an element at the position mentioned in its arguments. 
#  It takes 2 arguments, position and element to be added at respective position.

list1 = ["My", "is"]
list1.insert(1, "name")
list1.insert(0, "Liam")

print(list1)