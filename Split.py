# .split() is performed on a string, takes one argument, and returns a list of substrings found between the given argument (which in the case of .split() is known as the delimiter). The following syntax should be used:

# string_name.split(delimiter)
# If you do not provide an argument for .split() it will default to splitting at spaces.

string= "a a  a   a"
words = string.split()

print(words)
# ['a', 'a', 'a', 'a']

string = "a a  a   a"
words = string.split(" ")

print(words)
# ['a', 'a', '', 'a', '', '', 'a']

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one)
print(line_one_words)

# If we provide an argument for .split() we can dictate the character we want our string to be split on. This argument should be provided as a string itself.

# Consider the following example:

# >>> greatest_guitarist = "santana"
# >>> greatest_guitarist.split('n')
# ['sa', 'ta', 'a']
# We provided 'n' as the argument for .split() so our string “santana” got split at each 'n' character into a list of three strings.

# What do you think happens if we split the same string at 'a'?

# >>> greatest_guitarist.split('a')
# ['s', 'nt', 'n', ' ']
# Notice that there is an unexpected extra '' string in this list. When you split a string on a character that it also ends with, you’ll end up with an empty string at the end of the list.

# You can use any string as the argument for .split(), making it a versatile and powerful tool.

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

# create a list called author_names containing each individual author name as it’s own string.
author_names = authors.split(",")
print(author_names)
author_last_names = []

# Create another list called author_last_names that only contains the last names of the poets in the provided string.
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)

# This code is splitting the multi-line string at the newlines (\n) which exist at the end of each line and saving it to a new list called chorus_lines. Then it prints chorus_lines which will produce the output

# ['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to better suit your mood', "Because you're so smooth"]
# The new list contains each line of the original string as it’s own smaller string. Also, notice that Python automatically escaped the ' character when it created the new list.
smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines)

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)