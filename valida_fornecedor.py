# Gerar arquivo de fornecedores que não estão cadastrados

import pandas as pd
import re

def remove_caracteres_especiais(texto):
    return re.sub(r'\D', '', texto)

def valida_fornecedor():

    fornecedores_cadastrados_totvs = pd.read_excel('fornecedores_homolog.XLSX')
    data_frame_folha = pd.read_excel('CG - FOLHA DE PAGAMENTO 10_2023.xlsx', sheet_name="FOLPAG ENGPAC")
    
    with open('fornecedores_nao_cadastrados.txt', 'w') as arquivo_saida:
        arquivo_saida.write("Relatório de Fornecedores não cadastrados\n\n")
        for indice, tupla in data_frame_folha.iterrows():
            if remove_caracteres_especiais(str(tupla['CPF'])) not in remove_caracteres_especiais(str(fornecedores_cadastrados_totvs['CGCCFO'].to_list())):
                mensagem = f"O Fornecedor: {tupla['NOME']} não está cadastrado no TOTVS. Por favor, cadastre o Fornecedor de CPF: {tupla['CPF']}\n"
                arquivo_saida.write(mensagem)
            else:
                print(remove_caracteres_especiais(str(tupla['CPF'])))

valida_fornecedor()

