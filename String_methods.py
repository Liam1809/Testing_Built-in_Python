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



highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")

# print(highlighted_poems_list)

highlighted_poems_stripped = [element.strip() for element in highlighted_poems_list]

# print(highlighted_poems_stripped)

highlighted_poems_details = [element.split(":") for element in highlighted_poems_stripped]

# print(highlighted_poems_details)

titles = []
poets = []
dates = []

titles = [element[0] for element in highlighted_poems_details]
poets = [element[1] for element in highlighted_poems_details]
dates = [element[2] for element in highlighted_poems_details]

for i in range(len(titles)):
  title, poet, date = titles[i], poets[i], dates[i]
  print("The poem {t} was published by {p} in {d}".format(t = title, p = poet, d = date))