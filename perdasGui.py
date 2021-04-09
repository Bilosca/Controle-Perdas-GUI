import tkinter as tk
import tkinter.scrolledtext as st

from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image

# Import das funcoes e classe
from perdasGuiMetodos import (queryExecuter, VisualizaTabela, atualizaDias, tituloFont, textoEntry, textoFont) 

minhaFont=("Dotum", 14,)



class Janela:

    atualizaDias()

    def __init__(self, main):

        #Janela Principal:
        #fundo branco, 1400x800 
        self.main = main
        self.main.config(bg="#FFFFFF")
        self.main.geometry("1400x800")
        self.main.resizable(width=False, height=False)

        #Janela lateral aonde ficara os botoes
        #350x800 | fundo "cinza" | posicionado no lado esquerdo superior
        self.lateral = tk.Frame(self.main, width=350, height=800)
        self.lateral.config(bg = "#808080")
        self.lateral.grid(sticky="NW")
        self.lateral.grid_propagate(0)

        #Janela no qual estarao os dados dos produtos
        #1050x490 | fundo cinza claro
        self.tableFrame = tk.Frame(self.main, width=1050, height=490)
        self.tableFrame.config(bg="white")
        self.tableFrame.place(x=890,y=250, anchor="center")

        VisualizaTabela(self.tableFrame)

        # botao para atualizar a tabela apos uma modificacao no banco de dados
        self.btnRefreshTable = tk.Button(self.main,
                                         text="Atualizar",
                                         bg="#963645",
                                         activebackground="#A33B4A",
                                         activeforeground="white",
                                         fg="white",
                                         bd= 0,
                                         font=minhaFont,
                                         command=lambda: VisualizaTabela(self.tableFrame))
        self.btnRefreshTable.place(x=1285, y=530, anchor="center", width=130, height=40)

        self.primeiraCor = tk.Button(self.main,
                                         text="1a cor",
                                         bg="white",
                                         fg="#333333",
                                         bd= 0,
                                         font=minhaFont,
                                         command=lambda: VisualizaTabela(self.tableFrame))
        self.primeiraCor.place(x=412, y=530, anchor="center", width=95, height=40)

        self.segundaCor = tk.Button(self.main,
                                         text="2a cor",
                                         bg="white",
                                         fg="#333333",
                                         bd= 0,
                                         font=minhaFont,
                                         command=lambda: VisualizaTabela(self.tableFrame))
        self.segundaCor.place(x=520, y=530, anchor="center", width=95, height=40)

        # Frame para visualizar os outputs e mensagens do sistema
        # 985x220 | fundo cinza claro | desabilitado | e tipo flat
        self.notificacaoBox = st.ScrolledText(self.main,
                                              background="#F0F0F0",
                                              relief="flat",
                                              font= minhaFont)
        self.notificacaoBox.configure(state="disabled")
        self.notificacaoBox.place(x=858, y=675, anchor="center", width=985, height=220)

        #Config dos botoes laterais

        largura = 18
        altura = 2

        #--- Botao Insere Remessa ---
        self.btnInsere = tk.Button(self.lateral, 
                                    text="Inserir Remessa", 
                                    width=largura, 
                                    height=altura,
                                    borderwidth=0,
                                    font=minhaFont,

        # Command executa a funcao lambda que executa a funcao insereWin
        command=lambda: self.insereWin())

        self.btnInsere["bg"] = "white"
        self.btnInsere["fg"] = "#262626"
        self.btnInsere.place(relx= 0.5, rely=0.5, anchor="center")

        #--- Botao Procura Remessa ---
        self.btnProcura = tk.Button(self.lateral,
                                    text="Buscar Remessa", 
                                    width=largura, 
                                    height=altura,
                                    borderwidth=0,
                                    font=minhaFont,
                                    command= lambda : self.buscaWin())

        self.btnProcura["bg"] = "white"
        self.btnProcura["fg"] = "#262626"
        self.btnProcura.place(relx= 0.5, rely=0.6, anchor="center")

        #--- Botao Edita Remessa ---
        self.btnEdita = tk.Button(self.lateral,
                                    text="Editar Remessa", 
                                    width=largura, 
                                    height=altura,
                                    borderwidth=0,
                                    font=minhaFont)

        self.btnEdita["bg"] = "white"
        self.btnEdita["fg"] = "#262626"
        self.btnEdita.place(relx= 0.5, rely=0.7, anchor="center")

        #--- Botao Deleta Remessa ---
        self.btnDeleta = tk.Button(self.lateral,
                                    text="Deletar Remessa", 
                                    width=largura,
                                    height=altura,
                                    borderwidth=0,
                                    font=minhaFont)

        self.btnDeleta["bg"] = "white"
        self.btnDeleta["fg"] = "#262626"
        self.btnDeleta.place(relx= 0.5, rely=0.8, anchor="center")

        # Adicionar a Imagem de logo no corpo lateral
        imagem = Image.open("perdasGui/logo.png")
        logo = ImageTk.PhotoImage(imagem)

        self.labelLogo = tk.Label(self.lateral, image=logo, borderwidth=0)
        self.labelLogo.image = logo
        
        self.labelLogo.place(relx=0.49, rely=0.3, anchor="center")
    
    def insereWin(self):
        window = tk.Toplevel(self.main)
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
                                command=lambda : [queryExecuter(
                                operacao=0,entryProduto=entryProduto, entrySetor=entrySetor, entryValidade=entryValidade),
                                entryProduto.delete(0,"end")])

        btnConfirmar.place(x= 380, y= 175, anchor="nw", width=80, height= 21)

    def buscaWin(self):
        window = tk.Toplevel(self.main)
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
                                command= lambda: [queryExecuter(operacao=1, entryProduto= entryProduto), window.destroy()])
        btnConfirmar.place(x= 270, y=180, anchor="nw", width=90, height= 30)


root = tk.Tk()

app = Janela(root)

root.mainloop()