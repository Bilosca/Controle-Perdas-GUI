import tkinter as tk
from tkinter import ttk

from perdasGuiBd import PerdasDB
import datetime as dt

perdas = PerdasDB("controle_perdas.db")

tituloFont = ("Times New Roman", 20, "bold")
textoFont = ("Lucida Grande", 14)
textoEntry = ("Helvetica", 12)

tabelaFont=("Dotum", 12)
tabelaHeadingFont=("Dotum", 13, "bold")

def queryExecuter(operacao=0, entryProduto= "", entrySetor="", entryValidade="", id=0):
    try:
        produto = entryProduto.get().title()
        setor = entrySetor.get().title()
        validade = entryValidade.get_date()

        if operacao == 0:
            if not produto == "" and not setor == "":
                perdas.insereRemessa(produto, setor, validade)
            else:
                raise NameError("Campos Vazios")

        elif operacao == 1:
            perdas.procuraRemessa(produto)
        elif operacao == 2:
            pass
        elif operacao == 3:
            pass

    except NameError:
        print("os campos estao vazios")

# Cria Janela pra Inserimento de uma nova Remessa

def VisualizaTabela(janela):

    style = ttk.Style()
    style.configure("mystyle.Treeview",
                     font=tabelaFont,
                     background="#F0F0F0",
                     foreground="#212121",
                     rowheight=int(tabelaFont[1] * 2.5))# Configura as rows da tabela, fonte, borda, cor de fundo, e altura

    style.configure("mystyle.Treeview.Heading",
                     font=tabelaHeadingFont,
                     relief="flat",#retira as bordas dos headers
                     foreground="#333333",
                     background="#8C8C8C")# Configura o header da tabela

    style.layout("mystyle.Treeview", [("mystyle.Treeview.treearea",{"sticky":"nswe"})])#Remove as bordas

    tabela = ttk.Treeview(janela, style="mystyle.Treeview")
    scrollBar = ttk.Scrollbar(tabela, orient="vertical")


    scrollBar.configure(command=tabela.yview)
    scrollBar.place(x=995,y=242, anchor="center", height=490)
    tabela.config(yscrollcommand=scrollBar.set)

    tabela["columns"] = ("primeira", "segunda", "terceira", "quarta")
    tabela.column("#0", width=100, minwidth=100, stretch=tk.NO, anchor=tk.W)
    tabela.column("primeira", width=400, minwidth=400, stretch=tk.NO, anchor=tk.W)
    tabela.column("segunda", width=250, minwidth=250, stretch=tk.NO, anchor=tk.W)
    tabela.column("terceira", width=150, minwidth=150, stretch=tk.NO, anchor=tk.W)
    tabela.column("quarta", width=90, minwidth=90, stretch=tk.NO, anchor=tk.W)

    tabela.heading("#0", text="ID", anchor=tk.CENTER)
    tabela.heading("primeira", text="PRODUTO", anchor=tk.CENTER)
    tabela.heading("segunda", text="SETOR", anchor=tk.CENTER)
    tabela.heading("terceira", text="VALIDADE", anchor=tk.CENTER)
    tabela.heading("quarta", text="DIAS", anchor=tk.CENTER)

    dicionariosProdutos = perdas.displayItems()

    tabela.tag_configure("10Dias", background="#DAAFA9")
    tabela.tag_configure("30Dias", background="#AFDBC1")

    for tupla in dicionariosProdutos:
        ident = tupla[0]
        produto = tupla[1]
        setor = tupla[2]
        validade = tupla[3]
        dias = tupla[4]

        if dias <=10:
            tabela.insert("", "end", text=ident,values=(produto, setor, validade, dias), tags=("10Dias",))
        
        elif dias > 10 and dias <= 30:
            tabela.insert("", "end", text=ident,values=(produto, setor, validade, dias), tags=("30Dias",))
        
        else:
            tabela.insert("", "end", text=ident,values=(produto, setor, validade, dias))


    tabela.place(x=485,y=250, anchor="center", width=1000, height=490)

def atualizaDias():
    perdas.atualizaDias()

