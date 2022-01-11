## 9.1 
def good(list = ['Harry', 'Ron', 'Hermione']):
    return list

def get_odds():
    for i in range(10):
        if i % 2 != 0:
            yield i 

## 9.2 
count = 0 
for j in get_odds():
    count += 1 
    if count == 3:
        print(j)
        
## 9.3 
def my_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper 

def hi_there():
    print("Hi there!")
    
hi_there = my_decorator(hi_there)
hi_there()

## 9.4 
class OopsException(Exception):
    print('Oops, there is an exception')
a = [1,2,3,4,5]
for i in a:
    print(i)
    if i == 3:
        raise OopsException

