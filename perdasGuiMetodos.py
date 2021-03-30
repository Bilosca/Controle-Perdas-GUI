import tkinter as tk
from tkcalendar import DateEntry
from perdasGuiBd import PerdasDB
import datetime as dt


perdas = PerdasDB("controle_perdas.db")

tituloFont = ("Times New Roman", 20, "bold")
textoFont = ("Lucida Grande", 14)
textoEntry = ("Helvetica", 12)

def insereDados(entryProduto, entrySetor, entryValidade):
    produto = entryProduto.get()
    setor = entrySetor.get()
    validade = entryValidade.get_date()

    perdas.insereRemessa(produto, setor, validade)

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
     text="Validade",
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

    entrySetor = tk.Entry(window,
     bg="#E6E6E6",
     bd=0,
     font=textoEntry,
     width=20)

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
     command=lambda : insereDados(entryProduto, entrySetor, entryValidade))
    btnConfirmar.place(x= 380, y= 175, anchor="nw", width=80, height= 21)