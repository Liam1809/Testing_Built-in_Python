from random import randint
# randint(a,b) a: inclusive b: inclusive
elements = ['Hydrogen', 'Helium', 'Carbon', 'Oxygen', 'Nitrogen']
randlist_1 = []

while len(randlist_1) < len(elements):
    index = randint(0, len(elements) - 1)
    if elements[index] not in randlist_1:
       randlist_1.append(elements[index])  
print(randlist_1)
    
    
from random import randrange
# randrange(a,b) a: inclusive b exclusive
randlist_2 = []
while len(randlist_2) < len(elements):
	index = randrange(0, len(elements))
	if elements[index] not in randlist_2:
		randlist_2.append(elements[index])
  
print(randlist_2)