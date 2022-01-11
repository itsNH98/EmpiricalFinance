e2f = dict(dog =  'chien',
cat = 'chat',
walrus =  'morse')

print(e2f)

print(e2f['walrus'])

f2e = {}
for i in e2f.items():
    f2e.update( {i[1] : i[0]} )

print(f2e)

print(f2e['chien'])

print(set(f2e.values()))

life = dict(animals = dict(cats = {'Henri', 'Grumpy', 'Lucy'}, 
octopi = {0}, emus = {0}), plants = {0}, other = {0})

print(life)

print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])

squares = {i: i**2 for i in range(10)}
print(squares)

odd = {i for i in range(10) if i % 2 != 0}
print(type(odd))
print(odd)

l = [i for i in range(10)]
gen = (i for i in l)

for index in l:
    print('Got ' + str(next(gen)))

new_dict = {}
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
for k, v in zip(keys, values):
    new_dict[k] = v
print(new_dict)


new_dict2 = {}
keys = ['titles', 'plot']
values = [['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane'],
['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']]

for k,v in zip(keys, values):
    new_dict2[k] = v
print(new_dict2)    








