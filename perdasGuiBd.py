import sqlite3
import datetime as dt


class PerdasDB:
    def __init__(self, arquivoDb):
        self.conex = sqlite3.connect(arquivoDb)
        self.cursor = self.conex.cursor()
        self.cursor1 = self.conex.cursor()

        criaTabelaQuery = "CREATE TABLE IF NOT EXISTS remessa(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        produto TEXT,\
        setor TEXT,\
        validade TEXT,\
        dias INTEGER)"

        self.cursor.execute(criaTabelaQuery)
        self.conex.commit()
    
    def insereRemessa(self, produto, setor, validade):
        insertQuery = "INSERT INTO remessa(produto, setor, validade, dias) VALUES (?,?,?,?)"

        atual = dt.date.today()

        diasRestantes = int((validade - atual).days)

        validade = validade.strftime("%d/%m/%Y")

    
        self.cursor.execute(insertQuery,(produto, setor, validade, diasRestantes))
        self.conex.commit()
    
        
    def displayItems(self):
        lista = []
        displayQuery = "SELECT * FROM remessa"
        self.cursor.execute(displayQuery,)

        for items in self.cursor.fetchall():
            lista.append(items)

        return lista

    def atualizaDias(self):
        pegaDadosQuery = "SELECT * FROM remessa" #Query para selecionar os items no banco de dados
        updateDiasQuery = "UPDATE remessa SET dias = ? WHERE id = ?" #Query para atualizar os dias no banco de dados
        deletaQuery = "DELETE FROM remessa WHERE id = ?" #Query para deletar item do banco de dados

        self.cursor.execute(pegaDadosQuery,)

        # data atual
        atual = dt.date.today()

        # a cada item o id e a data sao distribuidos para as variaveis (ident, data)
        for item in self.cursor.fetchall():
            ident = item[0]
            data = item[3]

            # Converte a data para o tipo de date para poder achar a diferenca
            data = dt.datetime.strptime(data, "%d/%m/%Y").date()

            # Diferenca de dias
            diasRestantes = int((data - atual).days)

            self.cursor1.execute(updateDiasQuery, (diasRestantes, ident))

            # Exclui item caso esteja os dias seja menor ou igual a 0
            if diasRestantes <= 0:
                self.cursor.execute(deletaQuery, (ident,))
