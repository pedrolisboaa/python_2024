primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um segundo valor: ')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior segundo valor {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é menor segundo valor {segundo_valor}')
else:
    print(f'Os valore são iguais.')