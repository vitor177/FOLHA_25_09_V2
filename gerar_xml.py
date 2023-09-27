import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

class Generate_XML():

    # Função para gerar o XML do LAN
    def gerar_xml_lan(self,codcoligada, idlan, numerodocumento, classificacao, pagrec, statuslan, datavencimento, dataemissao, valororiginal, valorbaseirrf, codcolcfo, codcfo
                    ,codcolcxa, codcxa, codtdo, codfilial, seriedocumento, codmoevaloriginal, idformapagto, insseoutraempresa, percentbaseinss, codreceita, insseditado,
                    irrfeditado, reutilizacao):

        # Criar o elemento LAN
        lan = ET.Element("FLAN")

        # Preencher os elementos do LAN
        ET.SubElement(lan, "CODCOLIGADA").text = codcoligada
        ET.SubElement(lan, "IDLAN").text = idlan
        ET.SubElement(lan, "NUMERODOCUMENTO").text = numerodocumento
        ET.SubElement(lan, "CLASSIFICACAO").text = classificacao
        ET.SubElement(lan, "PAGREC").text = pagrec
        ET.SubElement(lan, "STATUSLAN").text = statuslan
        ET.SubElement(lan, "DATAVENCIMENTO").text = datavencimento
        ET.SubElement(lan, "DATAEMISSAO").text = dataemissao
        ET.SubElement(lan, "VALORORIGINAL").text = valororiginal
        ET.SubElement(lan, "VALORBASEIRRF").text = valorbaseirrf
        ET.SubElement(lan, "CODCOLCFO").text = codcolcfo
        ET.SubElement(lan, "CODCFO").text = codcfo
        ET.SubElement(lan, "CODCOLCXA").text = codcolcxa
        ET.SubElement(lan, "CODCXA").text = codcxa
        ET.SubElement(lan, "CODTDO").text = codtdo
        ET.SubElement(lan, "CODFILIAL").text = codfilial
        ET.SubElement(lan, "SERIEDOCUMENTO").text = seriedocumento
        ET.SubElement(lan, "CODMOEVALORORIGINAL").text = codmoevaloriginal
        ET.SubElement(lan, "IDFORMAPAGTO").text = idformapagto
        ET.SubElement(lan, "INSSEMOUTRAEMPRESA").text = insseoutraempresa
        ET.SubElement(lan, "PERCENTBASEINSS").text = percentbaseinss
        ET.SubElement(lan, "CODRECEITA").text = codreceita
        ET.SubElement(lan, "INSSEDITADO").text = insseditado
        ET.SubElement(lan, "IRRFEDITADO").text = irrfeditado
        ET.SubElement(lan, "REUTILIZACAO").text = reutilizacao

        return lan

    def gerar_xml_ratccusto(self, idratccu_rat, codcoligada_rat, idlan_rat, codccusto_rat, nome_rat, valor_rat, percentual_rat, codcolnatfinanceira_rat, codnatfinanceira_rat, descricao_rat):
        # Criar o elemento RATCCUSTO
        ratccusto = ET.Element("FLANRATCCU")

        # Preencher os elementos do RATCCUSTO
        ET.SubElement(ratccusto, "IDRATCCU").text = idratccu_rat
        ET.SubElement(ratccusto, "CODCOLIGADA").text = codcoligada_rat
        ET.SubElement(ratccusto, "IDLAN").text = idlan_rat
        ET.SubElement(ratccusto, "CODCCUSTO").text = codccusto_rat
        ET.SubElement(ratccusto, "NOME").text = nome_rat
        ET.SubElement(ratccusto, "VALOR").text = valor_rat
        ET.SubElement(ratccusto, "PERCENTUAL").text = percentual_rat
        ET.SubElement(ratccusto, "CODCOLNATFINANCEIRA").text = codcolnatfinanceira_rat
        ET.SubElement(ratccusto, "CODNATFINANCEIRA").text = codnatfinanceira_rat
        ET.SubElement(ratccusto, "DESCRICAO").text = descricao_rat

        return ratccusto

    #  SALÁRIO = LAN + RATCCUSTO
    def gerar_xml_salario(self, codcoligada, idlan, numerodocumento, classificacao, pagrec, statuslan, datavencimento, dataemissao, valororiginal, valorbaseirrf, codcolcfo, codcfo
                    ,codcolcxa, codcxa, codtdo, codfilial, seriedocumento, codmoevaloriginal, idformapagto, insseoutraempresa, percentbaseinss, codreceita, insseditado,
                    irrfeditado, reutilizacao, idratccu_rat, codcoligada_rat, idlan_rat, codccusto_rat, nome_rat, valor_rat, percentual_rat, codcolnatfinanceira_rat, codnatfinanceira_rat, descricao_rat):
        

        xml_lan = self.gerar_xml_lan(codcoligada, idlan, numerodocumento, classificacao, pagrec, statuslan, datavencimento, dataemissao, valororiginal, valorbaseirrf, codcolcfo, codcfo
                    ,codcolcxa, codcxa, codtdo, codfilial, seriedocumento, codmoevaloriginal, idformapagto, insseoutraempresa, percentbaseinss, codreceita, insseditado,
                    irrfeditado, reutilizacao)
        
        xml_ratccusto = self.gerar_xml_ratccusto(idratccu_rat, codcoligada_rat, idlan_rat, codccusto_rat, nome_rat, valor_rat, percentual_rat, codcolnatfinanceira_rat, "3.03.01.04", "Salário")
        
        # Adicionar o XML do RATCCUSTO abaixo do XML do LAN
        xml_lan.append(xml_ratccusto)
        
        return xml_lan

    # BENEFICIOS = LAN + 3 RATCCUSTO
    def gerar_xml_beneficios(self, codcoligada, idlan, numerodocumento, classificacao, pagrec, statuslan, datavencimento, dataemissao, valororiginal, valorbaseirrf, codcolcfo, codcfo
                    ,codcolcxa, codcxa, codtdo, codfilial, seriedocumento, codmoevaloriginal, idformapagto, insseoutraempresa, percentbaseinss, codreceita, insseditado,
                    irrfeditado, reutilizacao, idratccu_rat, codcoligada_rat, idlan_rat, codccusto_rat, nome_rat, valor_rat, percentual_rat, codcolnatfinanceira_rat, codnatfinanceira_rat, descricao_rat):

        xml_lan = self.gerar_xml_lan(codcoligada, idlan, numerodocumento, classificacao, pagrec, statuslan, datavencimento, dataemissao, valororiginal, valorbaseirrf, codcolcfo, codcfo
                    ,codcolcxa, codcxa, codtdo, codfilial, seriedocumento, codmoevaloriginal, idformapagto, insseoutraempresa, percentbaseinss, codreceita, insseditado,
                    irrfeditado, reutilizacao)
        
        
        return xml_lan

    # Gerar Lançamento completo
    def gerar_lancamento(self, codcoligada, idlan, numerodocumento, classificacao, pagrec, statuslan, datavencimento, dataemissao, valororiginal, valorbaseirrf, codcolcfo, codcfo
                    ,codcolcxa, codcxa, codtdo, codfilial, seriedocumento, codmoevaloriginal, idformapagto, insseoutraempresa, percentbaseinss, codreceita, insseditado,
                    irrfeditado, reutilizacao, idratccu_rat, codcoligada_rat, idlan_rat, codccusto_rat, nome_rat, valor_rat, percentual_rat, codcolnatfinanceira_rat, codnatfinanceira_rat, descricao_rat):
        xml_salarios = self.gerar_xml_salario(codcoligada, idlan, numerodocumento, classificacao, pagrec, statuslan, datavencimento, dataemissao, valororiginal, valorbaseirrf, codcolcfo, codcfo
                    ,codcolcxa, codcxa, codtdo, codfilial, seriedocumento, codmoevaloriginal, idformapagto, insseoutraempresa, percentbaseinss, codreceita, insseditado,
                    irrfeditado, reutilizacao, idratccu_rat, codcoligada_rat, idlan_rat, codccusto_rat, nome_rat, valor_rat, percentual_rat, codcolnatfinanceira_rat, codnatfinanceira_rat, descricao_rat)
        xml_beneficios = self.gerar_xml_beneficios(codcoligada, idlan, str(int(numerodocumento)+1), classificacao, pagrec, statuslan, datavencimento, dataemissao, valororiginal, valorbaseirrf, codcolcfo, codcfo
                    ,codcolcxa, codcxa, codtdo, codfilial, seriedocumento, codmoevaloriginal, idformapagto, insseoutraempresa, percentbaseinss, codreceita, insseditado,
                    irrfeditado, reutilizacao, idratccu_rat, codcoligada_rat, idlan_rat, codccusto_rat, nome_rat, valor_rat, percentual_rat, codcolnatfinanceira_rat, codnatfinanceira_rat, descricao_rat)

        xml_salarios.append(xml_beneficios)

        tree = ET.ElementTree(xml_salarios)

        return tree

    # Salvar em um arquivo XML
    def save_to_xml(self, xml):
        xml.write("output.xml", encoding="utf-8", xml_declaration=True)


""" tree = gerar_lancamento()

save_to_xml(tree)

    print("XML gerado com sucesso!")
 """