years_list = [1998, 1999, 2000, 2001, 2002]

third_birthday = years_list[2]

oldest = years_list[-1]

things = ["mozzarella", "cinderella", "salmonella"]

print(things[1].capitalize()) # doesn't change the list 

print(things)

print(things[0].upper())

things.remove('salmonella')
print(things)

surprise = ["Groucho", "Chico", "Harpo"]

print(surprise[-1].lower()[::-1].capitalize())

even = [i for i in range(10) if i % 2 == 0]
print(even)

#####################

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"

for element, first in zip(start1, rhymes):
    print(element.capitalize() + '! ', sep=' ', end='', flush=True)
    tuple_index = 0
    print(first[tuple_index].capitalize() + '! ', sep=' ', end='', flush=True)
    tuple_index += 1

for t in rhymes:
    print(start2 + '', t[1])





