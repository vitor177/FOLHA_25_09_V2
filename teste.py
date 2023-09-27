import pandas as pd


fornecedores_cadastrados_totvs = pd.read_excel('fornecedores.XLSX')


resultado = fornecedores_cadastrados_totvs[fornecedores_cadastrados_totvs['CGCCFO'] == '014.802.214-65']['CODCFO']




def valida_codcfo(cpf):
    dtype_dict = {'CODCFO': str, 'NOMEFANTASIA': str, 'CGCCFO': str}
    fornecedores_cadastrados_totvs = pd.read_excel('fornecedores.XLSX', dtype=dtype_dict)

    return str(fornecedores_cadastrados_totvs[fornecedores_cadastrados_totvs['CGCCFO'] == cpf]['CODCFO']).split( )[1]
    

print(valida_codcfo('014.802.214-65').split( )[1])