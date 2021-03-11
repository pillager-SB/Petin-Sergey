def odd_generator(num):
    for num in range(1, num + 1, 2):
        yield num


for i in odd_generator(9):
    print(i)
