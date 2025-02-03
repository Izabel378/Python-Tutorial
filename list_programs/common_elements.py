x = input('Enter elements of list 1 separated by ,\t').split(',')
y = input('Enter elements of list 2 separated by ,\t').split(',')

print(f'List 1:\t{x}')
print(f'List 2:\t{y}')


for i in x:
    if i in y:
        z=i;

print(f'Common elements are {z}.')
