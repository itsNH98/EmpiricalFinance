places = ['McDonalds', "KFC", "Burger King", "Taco Bell",
     "Wendys", "Arbys", "Pizza Hut"]

def pick():
    import random
    return random.choice(places)

print(pick())

import sys 
for place in sys.path:
    print(place)
    
## 11.1 
import zoo

zoo.hours()

## 11.2

import zoo as menagerie 

menagerie.hours()

## 11.3 

## 11.4 
from zoo import hours

hours()

## 11.5 
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

## 11.6 
from collections import OrderedDict

fancy = OrderedDict(plain)
print(fancy)

## 11.7 
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])