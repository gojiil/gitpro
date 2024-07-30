from random import randint

i = 0
while True:
    i += 1
    k = randint(1, 10)
    if k == 7:
        print(f'Hello, World! {i} times')
        break
