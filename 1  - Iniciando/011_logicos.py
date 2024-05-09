# AND

entra = input('Deseja [S]air ou [E]ntradar: ')
senha = input('Digite sua senha: ')

senha_correta = '1234'

if entra == 'E' or entra == 'e' and senha == senha_correta:
    print(f'Entrou!')
else:
    print('Saiu')
    
    
