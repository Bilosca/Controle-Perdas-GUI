import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from perdasGuiBd import PerdasDB
import datetime as dt


perdas = PerdasDB("controle_perdas.db")

tituloFont = ("Times New Roman", 20, "bold")
textoFont = ("Lucida Grande", 14)
textoEntry = ("Helvetica", 12)

def queryExecuter(operacao=0, entryProduto= "", entrySetor="", entryValidade="", id=0):
    try:
        produto = entryProduto.get().title()
        setor = entrySetor.get().title()
        validade = entryValidade.get_date()
    except AttributeError:
        pass

    if operacao == 0:
        perdas.insereRemessa(produto, setor, validade)

    elif operacao == 1:
        perdas.procuraRemessa(produto)
    elif operacao == 2:
        pass
    elif operacao == 3:
        pass

# Cria Janela pra Inserimento de uma nova Remessa
def insereWin(janela):
    window = tk.Toplevel(janela)
    window.title("Inserir Dados")
    window.geometry("600x300")
    window.config(bg="white")

    titulo = tk.Label(window,
                     text="Insira os Dados",
                     fg="#333333",
                     bg="white",
                     font=tituloFont)
    titulo.place(x=300,y=20, anchor="center")

    labelProduto = tk.Label(window,
                           text="PRODUTO",
                           fg="#333333",
                           bg="white",
                           font=textoFont)

    labelSetor = tk.Label(window,
                         text="SETOR",
                         fg="#333333",
                         bg="white",
                         font=textoFont)

    labelValidade = tk.Label(window,
                            text="VALIDADE",
                            fg="#333333",
                            bg="white",
                            font=textoFont)

    labelProduto.place(x=150, y=70,anchor="nw")
    labelSetor.place(x=150, y=120,anchor="nw")
    labelValidade.place(x=150, y=170,anchor="nw")

    entryProduto = tk.Entry(window,
     bg="#E6E6E6",
     bd=0,
     font=textoEntry,
     width=20,)

    entrySetor = ttk.Combobox(window, values=["Biscoitos", "Cereais", "Enlatados", "Farinhas", "Laticinios", "Oleos"])
    entrySetor.current(0)

    entryValidade = DateEntry(window,
     font=textoEntry
     )

    entryProduto.place(x=260, y=75, anchor="nw", width=200)
    entrySetor.place(x=260, y=125, anchor="nw", width=200)
    entryValidade.place(x=260, y=175, anchor="nw", width=110)

    btnConfirmar = tk.Button(window,
                            text = "Inserir",
                            bg = "#963645",
                            activebackground= "#A33B4A",
                            activeforeground= "white",
                            bd = 0,
                            fg="white",
                            command=lambda : queryExecuter(
                            operacao=0,entryProduto=entryProduto, entrySetor=entrySetor, entryValidade=entryValidade))

    btnConfirmar.place(x= 380, y= 175, anchor="nw", width=80, height= 21)

def buscaWin(janela):
    window = tk.Toplevel(janela)
    window.title("Buscar Remessa")
    window.geometry("600x300")
    window.config(bg="white")

    titulo = tk.Label(window,
                      text="Buscar Remessa",
                      bg="white",
                      fg="#333333",
                      font=tituloFont)
    titulo.place(x=300, y=20, anchor="center")

    labelProduto = tk.Label(window,
                            text="NOME DO PRODUTO",
                            bg="white",
                            fg="#333333",
                            font=textoFont)
    labelProduto.place(x=110, y=120, anchor="nw")

    entryProduto = tk.Entry(window,
                            bg="#E6E6E6",
                            bd=0,
                            font=textoEntry,
                            width=20,)
    entryProduto.place(x=320, y=122, anchor="nw")

    btnConfirmar = tk.Button(window,
                            text="Buscar",
                            bg="#963645",
                            activebackground= "#A33B4A",
                            activeforeground= "white",
                            bd = 0,
                            fg="white",
                            command= lambda: queryExecuter(operacao=1, entryProduto= entryProduto))
    btnConfirmar.place(x= 270, y=180, anchor="nw", width=90, height= 30)