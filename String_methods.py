# Python comes with built-in string methods that gives you the power to perform complicated tasks on strings very quickly and efficiently. 
# These string methods allow you to change the case of a string, split a string into many smaller strings, join many small strings together into a larger string, and allow you to neatly combine changing variables with string outputs.
# In the previous lesson, you worked len(), which was a function that determined the number of characters in a string. 
# This, while similar, was NOT a string method. String methods all have the same syntax:
# py string_name.string_method(arguments)
# Unlike len(), which is called with a string as it’s argument, a string method is called at the end of a string and each one has its own method specific arguments.

# These methods will not affect special characters, which are any non-alphabetical and non-numeric characters and
# will only apply to case-based characters, which include essentially all the alphabetical characters.

# # FORMATTING STRING METHODS
# .lower() returns the string with all lowercase characters.
# .upper() returns the string with all uppercase characters.
# .title() returns the string in title case, which means the first letter of each word is capitalized.

favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song)
print(favorite_song_lowercase)

poem_title = "spring storm"
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author = "William Carlos Williams"
poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

