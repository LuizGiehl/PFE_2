tuple1 = (14, 89, 12, 15, 98)
tuple2 = (-6, -7, -99, 568, 123, 43)

while True:
    print('\nDigite 1 - tamanho das tuples')
    print('Digite 2 - maior e menor elemento das tuples')
    print('Digite 3 - soma dos elementos de cada tuple')
    print('Digite 4 - junção das tuples')
    print('Digite 5 - verifica se um elemento digitado está na tuple')
    print('Digite 0 - sair')
    i = int(input('Digite um número: '))

    if i == 0:
        print('o programa foi finalizado')
        break
    if i == 1:
        print(f'\nO tamanho da tuple 1 é: {len(tuple1)}')
        print(f'O tamanho da tuple 2 é: {len(tuple2)}')
    if i == 2:
        concat_tuples = tuple1 + tuple2
        print(f'\nO maior número dentro das tuples é {max(concat_tuples)}')
        print(f'O menor número dentro das tuples é {min(concat_tuples)}')
    if i == 3:
        print(f'\nA soma dos números das tuples é de {sum(tuple1 + tuple2)}')
    if i == 4:
        print(f'\nA junção das tuples fica: {tuple1 + tuple2}')
    if i == 5:
        element = int(input('\nDigite um número: '))
        concat_tuples = tuple1 + tuple2

        if element in concat_tuples:
            print('\nO número está na tuple\n')
        else:
            print('O número não está na tuple\n')