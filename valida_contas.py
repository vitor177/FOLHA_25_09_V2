import pandas as pd
from preenchimento_salario import PreenchimentoSalario
from gerar_xml import Generate_XML
import xml.etree.ElementTree as ET


data_frame_folha = pd.read_excel('CG - FOLHA DE PAGAMENTO 10_2023.xlsx', sheet_name="FOLPAG ENGPAC")


contador_id_lan = 0
finlan = ET.Element("FinLAN")
# Lançamento salários
for indice, linha in data_frame_folha.iloc[:-1].iterrows():

    #print(linha['NOME'])

    contador_id_lan += 1

    # Dados
    nome_pessoa = linha['NOME']
    empresa_pessoa = linha['EMPRESA']
    polo_pessoa = linha['POLO']

    # Informações bancárias
    banco_pessoa = linha['BANCO']
    tipoconta_pessoa = linha['TIPO DE CONTA']
    agencia_pessoa = linha['AGÊNCIA']
    operacao_pessoa = linha['OPERAÇÃO']
    conta_pessoa = linha['CONTA']

    # Salário
    total_liquido_pessoa = linha['LIQUIDO']
    # Vale Transporte
    vale_transporte_pessoa = linha['VT']
    # Vale Alimentação
    vale_alimentacao_pessoa = linha['VA']
    # Acréscimos
    acrescimo_pessoa = linha['ACRESCIMO/DIÁRIA']


    usuario_instancia = PreenchimentoSalario()

    # Como os valores devem ser escritos no arquivo XML
    # Lançamentos para a tag <LAN>
    empresa_xml_lan = usuario_instancia.valida_codcoligada(empresa_pessoa)
    contador_id_lan_xml_lan = "-"+str(contador_id_lan)
    numerodocumento_xml_lan = usuario_instancia.valida_numerodocumento()
    classificacao_xml_lan = usuario_instancia.valida_classificacao()

    pag_rec_xml_lan = usuario_instancia.valida_pag_rec()
    statuslan_xml_lan = usuario_instancia.valida_statuslan()

    data_vencimento_xml_lan = usuario_instancia.valida_data_vencimento()
    data_emissao_xml_lan = usuario_instancia.valida_data_emissao()
    valor_original_xml_lan = usuario_instancia.valida_valor_original(total_liquido_pessoa)
    valor_base_irrf_xml_lan = usuario_instancia.valida_valor_base_irrf()

    codcolcfo_xml_lan = usuario_instancia.valida_codcolcfo()
    codcfo_xml_lan = usuario_instancia.valida_codcfo()
    codcolcxa_xml_lan = usuario_instancia.valida_codcolcxa()
    codcxa_xml_lan = usuario_instancia.valida_codcxa()
    codtdo_xml_lan = usuario_instancia.valida_codtdo()
    codfilial_xml_lan = usuario_instancia.valida_codfilial()
    seriedocumento_xml_lan = usuario_instancia.valida_seriedocumento()
    codmoevalororiginal_xml_lan = usuario_instancia.valida_codmoevalororiginal()
    idformapagto_xml_lan = usuario_instancia.valida_idformapagto()
    inssemoutraempresa_xml_lan = usuario_instancia.valida_inssemoutraempresa()
    percentbaseinss_xml_lan = usuario_instancia.valida_percentbaseinss()
    codreceita_xml_lan = usuario_instancia.valida_codreceita()
    insseeditado_xml_lan = usuario_instancia.valida_insseeditado()
    irrfeditado_xml_lan = usuario_instancia.valida_irrfeditado()
    reutilizacao_xml_lan = usuario_instancia.valida_reutilizacao()

    # Lançamentos para a tag <RATCCUSTO>
    idratccu_xml_rat = usuario_instancia.valida_idratccu()
    codcoligada_xml_rat = usuario_instancia.valida_codcoligada(empresa_pessoa)

    idlan_xml_rat = usuario_instancia.valida_idlan()
    codccusto_xml_rat = usuario_instancia.valida_codccusto()
    nome_xml_rat = usuario_instancia.valida_nome()
    valor_xml_rat = usuario_instancia.valida_valor()
    percentual_xml_rat = usuario_instancia.valida_percentual()
    codcolnatfinanceira_xml_rat = usuario_instancia.valida_codcolnatfinanceira()
    codnatfinanceira_xml_rat = usuario_instancia.valida_codnatfinanceira()
    descricao_xml_rat = usuario_instancia.valida_descricao()


    lancamento_salario = Generate_XML()

    tree = lancamento_salario.gerar_lancamento(empresa_xml_lan, contador_id_lan_xml_lan, numerodocumento_xml_lan, classificacao_xml_lan, pag_rec_xml_lan, statuslan_xml_lan, data_vencimento_xml_lan, data_emissao_xml_lan, valor_original_xml_lan, valor_base_irrf_xml_lan, codcolcfo_xml_lan, codcfo_xml_lan
                ,codcolcxa_xml_lan, codcxa_xml_lan, codtdo_xml_lan, codfilial_xml_lan, seriedocumento_xml_lan, codmoevalororiginal_xml_lan, idformapagto_xml_lan, inssemoutraempresa_xml_lan, percentbaseinss_xml_lan , codreceita_xml_lan, insseeditado_xml_lan,
                irrfeditado_xml_lan,  reutilizacao_xml_lan, 
                idratccu_xml_rat, codcoligada_xml_rat, idlan_xml_rat, codccusto_xml_rat, nome_xml_rat, valor_xml_rat, percentual_xml_rat, codcolnatfinanceira_xml_rat, codnatfinanceira_xml_rat, descricao_xml_rat)
    finlan.append(tree.getroot())


tree = ET.ElementTree(finlan)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)
