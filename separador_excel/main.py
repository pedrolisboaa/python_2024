"""
Script Python que separa tabela em várias, conforme dados da coluna informada.
"""

import pandas as pd
from time import sleep

# Carregue a planilha

nome_do_arquivo = input('Nome do arquivo: ')
nome_da_coluna = input('Informe o nome da coluna: ')
dados = pd.read_excel(nome_do_arquivo)

# Obtenha os valores únicos na coluna "PA"
valores_pa_unicos = dados[nome_da_coluna].unique()

for i in range(3):
    sleep(1)
    print(f'Os arquivos seráo gerados em {i + 1}')

# Itere sobre os valores únicos na coluna "PA" e escreva em arquivos Excel separados
for valor_pa in valores_pa_unicos:
    dados_filtrados = dados[dados[nome_da_coluna] == valor_pa]
    nome_arquivo = f'dados_PA_{valor_pa}.xlsx'
    dados_filtrados.to_excel(nome_arquivo, index=False)

sleep(2)
print('Encerrando sistema')