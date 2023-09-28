import pandas as pd





def valida_codcfo(cpf):
    dtype_dict = {'CODCOLIGADA': str, 'CODCFO': str, 'NOMEFANTASIA': str, 'CGCCFO': str}
    fornecedores_cadastrados_totvs = pd.read_excel('fornecedores_homolog.XLSX', dtype=dtype_dict)

    return str(fornecedores_cadastrados_totvs[fornecedores_cadastrados_totvs['CGCCFO'] == cpf]['CODCOLIGADA']).split( )[1]
    

print(valida_codcfo('105.933.284.18'))