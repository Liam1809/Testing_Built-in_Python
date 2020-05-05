# Now that you’ve learned to break strings apart using .split(), let’s learn to put them back together using .join(). .join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter. The syntax of .join() is:

# 'delimiter'.join(list_you_want_to_join)
# Now this may seem a little weird, because with .split() the argument was the delimiter, but now the argument is the list. This is because join is still a string method, which means it has to act on a string. The string .join() acts on is the delimiter you want to join with, therefore the list you want to join has to be the argument.

# This can be a bit confusing, so let’s take a look at an example.

# >>> my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
# >>> ' '.join(my_munequita)
# 'My Spanish Harlem Mona Lisa'
# We take the list of strings, my_munequita, and we joined it together with our delimiter, ' ', which is a space. The space is important if you are trying to build a sentence from words, otherwise, we would have ended up with:

# >>> ''.join(my_munequita)
# 'MySpanishHarlemMonaLisa'

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)
reapers_line_two = reapers_line_one.split()
print(reapers_line_two)
reapers_line_three = " ".join(reapers_line_two)
print(reapers_line_three)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)