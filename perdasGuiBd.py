import sqlite3
import datetime as dt


class PerdasDB:
    def __init__(self, arquivoDb):
        self.conex = sqlite3.connect(arquivoDb)
        self.cursor = self.conex.cursor()

        criaTabelaQuery = "CREATE TABLE IF NOT EXISTS remessa(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        produto TEXT,\
        setor TEXT,\
        validade INTEGER,\
        dias INTEGER)"

        self.cursor.execute(criaTabelaQuery)
        self.conex.commit()
    
    def insereRemessa(self, produto, setor, validade):
        insertQuery = "INSERT INTO remessa(produto, setor, validade, dias) VALUES (?,?,?,?)"

        global atual
        atual = dt.date.today()

        diasRestantes = int((validade - atual).days)

        try:
            if not produto == "" and not setor == "":
                self.cursor.execute(insertQuery,(produto, setor, validade, diasRestantes))
                self.conex.commit()
                print(f"{produto}, {setor}, {validade} Inserido com sucesso. ")

            else:
                raise NameError("Campos Vazios")

        except NameError as e:
            print("Preencha os campos")
            print(e)
            pass