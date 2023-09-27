# Falta terminar
from datetime import datetime, timedelta
import random

class PreenchimentoSalario():

    # CODCOLIGADA
    def valida_codcoligada(self, nome_empresa):
        if nome_empresa == "GENNESIS":
            return "1"
        if nome_empresa == "ENGPAC":
            return "2"
        if nome_empresa == "T2":
            return "3"
        return "0"
    
    # Feito no próprio laço do valida_contas.py pela variável contador_id_lan_xml
    def valida_idlan():
        pass

    # Gera um número aleatório de 12 dígitos
    def valida_numerodocumento(self):
        return str(random.randint(10**11, (10**12)-1))
    
    # Sei lá o que é isso mas tá no XML
    def valida_classificacao(self):
        return "5"
    
    # A pagar ou A receber
    def valida_pag_rec(self):
        # Todos os lançamentos são a pagar
        return "2"

    def valida_statuslan(self):
        return "0"
    
    def valida_data_vencimento(self):
        # Obter a data atual
        data_atual = datetime.now()

        # Adicionar 1 mese à data atual
        data_vencimento = data_atual + timedelta(days=30)

        # Formatar a data no formato desejado
        data_vencimento_formatada = data_vencimento.strftime("%Y-%m-%dT%H:%M:%S-03:00")

        return str(data_vencimento_formatada)
    

    def valida_data_emissao(self):
        # Obter a data atual
        data_atual = datetime.now()

        # Formatar a data no formato desejado
        data_formatada = data_atual.strftime("%Y-%m-%dT%H:%M:%S-03:00")

        return str(data_formatada)
    
    def valida_valor_original(self, valor_original):
        return "{:.4f}".format(valor_original)
    
    def valida_valor_base_irrf(self):
        return "100.0000"
    
    def valida_codcolcfo(self):
        return "0"



    def valor_base_irrf(self):
        return "100.0000"

    def codcolcfo(self):
        return "0"

    def valida_codcolcfo(self):
        return "0"
    
    # TO DO
    def valida_codcfo(self):
        return "000000630"

    # TO DO
    def valida_codcolcxa(self):
        return "2"

    # TO DO
    def valida_codcxa(self):
        return "99230-6"


    def valida_codtdo(self):
        return "9999"

    # TO DO
    def valida_codfilial(self):
        return "1"

    def valida_seriedocumento(self):
        return "U"

    def valida_codmoevalororiginal(self):
        return "R$"

    # TO DO
    def valida_idformapagto(self):
        return "1"

    def valida_inssemoutraempresa(self):
        return "0.0000"

    def valida_percentbaseinss(self):
        return "0.0000"

    def valida_codreceita(self):
        return "0561"

    def valida_insseeditado(self):
        return "0"

    def valida_irrfeditado(self):
        return "0"

    def valida_reutilizacao(self):
        return "0"
    
    #######################################
    #######################################
    #######################################
    #######################################
    #######################################

    # RATCCUSTO

    def valida_idratccu(self):
        return "-1"

    def valida_idlan(self):
        return "-1"

    # TO DO 
    def valida_codccusto(self):
        return "02.02.01.02.001"

    def valida_nome(self):
        return "Departamento Pessoal"

    def valida_valor(self, valor):
        return "{:.4f}".format(valor)

    def valida_percentual(self):
        return "0.0000"

    def valida_codcolnatfinanceira(self):
        return "0"

    # TO DO
    def valida_codnatfinanceira(self):
        return "3.03.01.04"

    # TO DO
    def valida_descricao(self):
        return "Acrescimo"