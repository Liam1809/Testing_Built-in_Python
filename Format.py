# Python also provides a handy string method for including variables in strings. This method is .format(). .format() takes variables as an argument and includes them in the string that it is run on. You include {} marks as placeholders for where those variables will be imported.

# Consider the following function:

# def favorite_song_statement(song, artist):
#   return "My favorite song is {} by {}.".format(song, artist)
# The function favorite_song_statement takes two arguments, song and artist, then returns a string that includes both of the arguments and prints a sentence. Note: .format() can take as many arguments as there are {} in the string it is run on, which in this case in two.

# Here’s an example of the function being run:

# >>> favorite_song_statement("Smooth", "Santana")
# "My favorite song is Smooth by Santana"
# Now you may be asking yourself, I could have written this function using string concatenation instead of .format(), why is this method better? The answer is legibility and reusability. It is much easier to picture the end result .format() than it is to picture the end result of string concatenation and legibility is everything. You can also reuse the same base string with different variables, allowing you to cut down on unnecessary, hard to interpret code.

def poem_title_card(poet, title):
      return "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

# .format() can be made even more legible for other people reading your code by including keywords. Previously with .format(), you had to make sure that your variables appeared as arguments in the same order that you wanted them to appear in the string, which just added unnecessary complications when writing code.

# By including keywords in the string and in the arguments, you can remove that ambiguity. Let’s look at an example.

# def favorite_song_statement(song, artist):
#     return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)
# Now it is clear to anyone reading the string what it supposed to return, they don’t even need to look at the arguments of .format() in order to get a clear understanding of what is supposed to happen. You can even reverse the order of artist and song in the code above and it will work the same way. This makes writing AND reading the code much easier.

def poem_description(publishing_date, author, title, original_work):
      poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
      return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)

string = "{}, {a}, {}".format(20, 30, a=40)

# First, the positional arguments 20 and 30
# replace the {} in order.
# Then the keyword argument is placed at {a}.

# This will result in:
print(string) # 20, 40, 30