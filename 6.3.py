guess_me = 5 

for i in range(10):
    if i < guess_me:
        print(str(i) + ' is too low')
    elif i == guess_me:
        print(str(i) + ' is right')
    elif i > guess_me: 
        print('oops')

