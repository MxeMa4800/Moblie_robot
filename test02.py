num = int(float(input('x = ')))
for x in range(num):
    for y in range(num-x):
        print('*', end='')
    print('')