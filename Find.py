# Another interesting string method is .find(). .find() takes a string as an argument and searching the string it was run on for that string. It then returns the first index value where that string is located.

# Here’s an example:

# >>> 'smooth'.find('t')
# '4'
# We searched the string 'smooth' for the string 't' and found that it was at the fourth index spot, so .find() returned 4.

# You can also search for larger strings, and .find() will return the index value of the first character of that string.

# >>>"smooth".find('oo')
# '2'
# Notice here that 2 is the index of the first o.

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")

print(disown_placement)

# if not find the argumnt in the string, find() will return -1