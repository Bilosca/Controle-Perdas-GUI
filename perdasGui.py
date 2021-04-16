import tkinter as tk

from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image

# Import das funcoes e classe
import perdasGuiMetodos as pgm

minhaFont=("Dotum", 14,)



class Janela:

    pgm.atualizaDias()

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

        tabela = pgm.VisualizaTabela(self.tableFrame)

        # Frame para visualizar os outputs e mensagens do sistema
        # 985x220 | fundo cinza claro | desabilitado | e tipo flat
        self.outPutBox = tk.Text(self.main,
                                 background="#F0F0F0",
                                 relief="flat",
                                 font= minhaFont)
        self.outPutBox.place(x=858, y=685, anchor="center", width=985, height=200)

        # Entrys e Labels dos Campos
        entryProduto = tk.Entry(self.main,
                                fg="#333333",
                                bg="#F0F0F0",
                                highlightthickness=0,
                                bd=0,
                                font=pgm.textoEntry,
                                width=20,)
        entryProduto.insert(0, "Produto")

        # Campo de input de Setor 
        entrySetor = ttk.Combobox(self.main,
                                  values=["Biscoitos",
                                          "Cereais",
                                          "Enlatados",
                                          "Farinhas",
                                          "Laticinios",
                                          "Oleos",
                                          "Bebidas",
                                          "Gelados",
                                          "Outros"],
                                  font=pgm.textoEntry,)                               
        entrySetor.current(0)

        # Campo de input para a data de validade
        entryValidade = DateEntry(self.main,
                                  font=pgm.textoEntry)

        # Campo de input para o Id

        idString = tk.StringVar()
        idString.set("ID")

        entryId = tk.Entry(self.main,
                           fg="#333333",
                           bg="#F0F0F0",
                           highlightthickness=0,
                           bd=0,
                           font=pgm.textoEntry,
                           justify="right",
                           textvariable=idString)
        entryId.configure(state="readonly", readonlybackground="#F0F0F0")

        # Estilo do entry Setor
        setorStyle= ttk.Style(self.main)
        setorStyle.map("TCombobox", fieldbackground=[("readonly","#F0F0F0")])
        setorStyle.configure("my.TCombobox",
                             foreground="#333333",
                             borderwidth=0,
                             relief="flat",)

        entrySetor.configure(style="my.TCombobox", state="readonly")

        # Estilo do entry validade
        validadeStyle= ttk.Style(self.main)
        validadeStyle.configure("my.DateEntry",fieldbackground="#F0F0F0", foreground="#333333", borderwidth=0, relief="flat")
        entryValidade.configure(style="my.DateEntry")
        
        # Posicionamentos dos entries e redimensao das suas propriedades
        entryProduto.place(x=365, y=520, anchor="nw", width=250, height=30)
        entrySetor.place(x=630, y=520, anchor="nw", width=250, height=30)
        entryValidade.place(x=895, y=520, anchor="nw", width=250, height=30)
        entryId.place(x=1160, y=520, anchor="nw", width=100, height=30)

       #Config dos botoes laterais

        largura = 18
        altura = 2

        #--- BotOes do menu Principal ---
        self.btnInsere = tk.Button(self.lateral, 
                                    text="Inserir Remessa", 
                                    width=largura, 
                                    height=altura,
                                    borderwidth=0,
                                    font=minhaFont,
                                    bg="white",
                                    fg="#262626",

                                    # Command executa a funcao lambda que executa a funcao insereWin
                                    command=lambda: [pgm.queryExecuter(0,entryProduto, entrySetor, entryValidade),
                                    entryProduto.delete(0, "end"),
                                    entryProduto.insert(0,"Produto"),
                                    tabela.delete(*tabela.get_children()),
                                    pgm.adicionaItem()])
        self.btnInsere.place(relx= 0.5, rely=0.55, anchor="center")

        self.btnEdita = tk.Button(self.lateral,
                                    text="Editar Remessa", 
                                    width=largura, 
                                    height=altura,
                                    borderwidth=0,
                                    font=minhaFont,
                                    bg="white",
                                    fg="#262626",
                                    )
        self.btnEdita.place(relx= 0.5, rely=0.65, anchor="center")

        self.btnDeleta = tk.Button(self.lateral,
                                    text="Deletar Remessa", 
                                    width=largura,
                                    height=altura,
                                    borderwidth=0,
                                    font=minhaFont,
                                    bg="white",
                                    fg="#262626")
        self.btnDeleta.place(relx= 0.5, rely=0.75, anchor="center")

        # Adicionar a Imagem de logo no corpo lateral
        imagem = Image.open("perdasGui/logo.png")
        logo = ImageTk.PhotoImage(imagem)

        self.labelLogo = tk.Label(self.lateral, image=logo, borderwidth=0)
        self.labelLogo.image = logo
        
        self.labelLogo.place(relx=0.49, rely=0.3, anchor="center")
        
        tabela.bind("<Double-1>", lambda event : pgm.selecionaItem(event,
                                                                   entryProduto=entryProduto,
                                                                   entrySetor=entrySetor,
                                                                   entryValidade=entryValidade,
                                                                   idVar=idString))
        

root = tk.Tk()

app = Janela(root)

root.mainloop()