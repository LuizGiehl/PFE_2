tuple_a = ('c', 'a', 'r', 'e', 't')
tuple_b = ('a', 'e', 'i', 'o', 'u')

print(f'\nA união das tupels fica {tuple_a + tuple_b}')
print(f'\nOs elementos em comum das tuples é: {set(tuple_a).intersection(set(tuple_b))}')
print(f'\nOs elementos diferentes são: {set(tuple_a).symmetric_difference(set(tuple_b))}')
