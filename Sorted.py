# A second way of sorting a list is to use sorted. sorted is different from .sort() in several ways:

# It comes before a list, instead of after.
# It generates a new list.
# Let’s return to our list of names:

# names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# Using sorted, we can create a new list, called sorted_names:

# sorted_names = sorted(names)
# print(sorted_names)
# This yields the list sorted alphabetically:

# ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
# Note that using sorted did not change names:

# >>> print(names)
# ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
# games list will stay as inital
print(games)
# games_sorted comes before games list that means it will not affect the order of orginal list
print(games_sorted)
