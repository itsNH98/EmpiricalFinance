guess_me = 7
number = 1 

while number < guess_me:
    print(str(number) + ' is too low')
    number += 1
    if number == guess_me:
        print(str(number) + ' is the right number')
    