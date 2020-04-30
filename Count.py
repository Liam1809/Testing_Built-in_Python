# Suppose we have a list called letters that represents the letters in the word “Mississippi”:

# letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
# If we want to know how many times i appears in this word, we can use the function count:

# num_i = letters.count('i')
# print(num_i)
# This would print out:

# 4

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 
         'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 
         'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 
         'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count("Jake")
print(jake_votes)

# if wanted element to count not in the list, return 0
print(votes.count("Liam"))