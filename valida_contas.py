import math
import pandas as pd
from preenchimento_salario import PreenchimentoSalario
from gerar_xml import Generate_XML
import xml.etree.ElementTree as ET


data_frame_folha = pd.read_excel('CG - FOLHA DE PAGAMENTO 10_2023.xlsx', sheet_name="FOLPAG ENGPAC")


contador_id_lan = 0
finlan = ET.Element("FinLAN")

contador_id_ratccu = 0
# Lançamento salários
for indice, linha in data_frame_folha.iloc[:-1].iterrows():

    #print(linha['NOME'])

    contador_id_lan += 1
    contador_id_ratccu += 1

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
    contador_id_ratcc_xml = "-"+str(contador_id_ratccu)

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
    codcoligada_xml_rat = usuario_instancia.valida_codcoligada(empresa_pessoa)

    idlan_xml_rat = usuario_instancia.valida_idlan()
    codccusto_xml_rat = usuario_instancia.valida_codccusto()
    nome_xml_rat = usuario_instancia.valida_nome()
    valor_xml_rat = usuario_instancia.valida_valor(total_liquido_pessoa)
    percentual_xml_rat = usuario_instancia.valida_percentual()
    codcolnatfinanceira_xml_rat = usuario_instancia.valida_codcolnatfinanceira()
    codnatfinanceira_xml_rat = usuario_instancia.valida_codnatfinanceira()
    descricao_xml_rat = usuario_instancia.valida_descricao()

    lancamento_salario = Generate_XML()
    lan_ac = None
    lan_vt = None
    lan_va = None
    tree = lancamento_salario.gerar_xml_salario(empresa_xml_lan, contador_id_lan_xml_lan, numerodocumento_xml_lan, classificacao_xml_lan, pag_rec_xml_lan, statuslan_xml_lan, data_vencimento_xml_lan, data_emissao_xml_lan, valor_original_xml_lan, valor_base_irrf_xml_lan, codcolcfo_xml_lan, codcfo_xml_lan
                ,codcolcxa_xml_lan, codcxa_xml_lan, codtdo_xml_lan, codfilial_xml_lan, seriedocumento_xml_lan, codmoevalororiginal_xml_lan, idformapagto_xml_lan, inssemoutraempresa_xml_lan, percentbaseinss_xml_lan , codreceita_xml_lan, insseeditado_xml_lan,
                irrfeditado_xml_lan,  reutilizacao_xml_lan, 
                str(int(contador_id_ratcc_xml)-1), codcoligada_xml_rat, contador_id_lan_xml_lan, codccusto_xml_rat, nome_xml_rat, valor_xml_rat, percentual_xml_rat, codcolnatfinanceira_xml_rat, codnatfinanceira_xml_rat, descricao_xml_rat)
    

    if (not math.isnan(acrescimo_pessoa)) or (not math.isnan(vale_transporte_pessoa)) or (not math.isnan(vale_alimentacao_pessoa)):
        lan_beneficio = lancamento_salario.gerar_xml_lan(empresa_xml_lan, contador_id_lan_xml_lan, str(int(numerodocumento_xml_lan)-1), classificacao_xml_lan, pag_rec_xml_lan, statuslan_xml_lan, data_vencimento_xml_lan, data_emissao_xml_lan, valor_original_xml_lan, valor_base_irrf_xml_lan, codcolcfo_xml_lan, codcfo_xml_lan
                    ,codcolcxa_xml_lan, codcxa_xml_lan, codtdo_xml_lan, codfilial_xml_lan, seriedocumento_xml_lan, codmoevalororiginal_xml_lan, idformapagto_xml_lan, inssemoutraempresa_xml_lan, percentbaseinss_xml_lan , codreceita_xml_lan, insseeditado_xml_lan,
                irrfeditado_xml_lan,  reutilizacao_xml_lan)
        finlan.append(lan_beneficio)


# self, idratccu_rat, codcoligada_rat, idlan_rat, codccusto_rat, nome_rat, valor_rat, percentual_rat, codcolnatfinanceira_rat, codnatfinanceira_rat, descricao_rat
    if not math.isnan(acrescimo_pessoa):
        contador_id_ratccu += 1
        lan_ac = lancamento_salario.gerar_xml_ratccusto("-"+str(contador_id_ratccu), codcoligada_xml_rat, contador_id_lan_xml_lan, codccusto_xml_rat, nome_xml_rat, usuario_instancia.valida_valor_original(acrescimo_pessoa), percentual_xml_rat, codcolnatfinanceira_xml_rat, "3.04.01.14", "Acrescimo")
    if not math.isnan(vale_transporte_pessoa):
        contador_id_ratccu += 1
        lan_vt = lancamento_salario.gerar_xml_ratccusto("-"+str(contador_id_ratccu), codcoligada_xml_rat, contador_id_lan_xml_lan, codccusto_xml_rat, nome_xml_rat,  usuario_instancia.valida_valor_original(vale_transporte_pessoa), percentual_xml_rat, codcolnatfinanceira_xml_rat, "3.03.01.06", "Vale Transporte")
    if not math.isnan(vale_alimentacao_pessoa):
        contador_id_ratccu += 1
        lan_va = lancamento_salario.gerar_xml_ratccusto("-"+str(contador_id_ratccu), codcoligada_xml_rat, contador_id_lan_xml_lan, codccusto_xml_rat, nome_xml_rat,  usuario_instancia.valida_valor_original(vale_alimentacao_pessoa), percentual_xml_rat, codcolnatfinanceira_xml_rat, "3.03.01.20", "Vale Alimentação")

    finlan.append(tree)

    if lan_ac is not None:
        finlan.append(lan_ac)
    if lan_vt is not None:
        finlan.append(lan_vt)
    if lan_ac is not None:
        finlan.append(lan_va)


tree = ET.ElementTree(finlan)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)
