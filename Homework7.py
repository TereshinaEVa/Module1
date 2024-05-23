my_dict = {'Masha': 1985, 'Irina':1990, 'Ivan':1976}
print(my_dict)
print(my_dict['Irina'])
print(my_dict.get('Vasia'))
my_dict.update({'Kate':1978,
                'Mikhail':1991})
minus = my_dict.pop('Ivan')
print(minus)
print(my_dict)

print('\n')

my_set = {2, 5, 'apple', 10, 5, 2, True, 2.5, 'apple', 'orange'}
print(my_set)
my_set.add((1,2,3))
my_set.add(28.3)
my_set.discard(2)
print(my_set)