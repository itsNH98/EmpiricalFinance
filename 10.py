## 10.1

class Thing():
    pass
example = Thing()

print(Thing())
print(example)

## 10.2 

class Thing2():
    def __init__(self):
        self.letters = 'abc'
a = Thing2()
print(a.letters)

## 10.3 

class Thing3():
    def __init__(self, letters):
        self.letters = letters
b = Thing3('xyz')
print(b.letters)

## 10.4 

class Element():
    def __init__(self, name, symbol, number):
        self._name = name 
        self._symbol = symbol
        self._number = number
        
    
    @property
    def name(self):
        return self._name 
    
    
c = Element('Hydrogen', 'H', 1)
print(c.name)

## 10.5
 
d = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(d['name'], d['symbol'], d['number'])

# print(hydrogen.symbol) 

## 10.6

# hydrogen.dump()

## 10.7

print(hydrogen)

## 10.8 

print(hydrogen.name)







