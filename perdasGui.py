import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image


# Import das funcoes e classe
import perdasGuiMetodos as pgm

minhaFont=("Dotum", 14,)


class Janela:


    def __init__(self, main):

        #Janela Principal:
        #fundo branco, 1400x800 
        self.main = main
        self.main.config(bg="#FFFFFF")
        self.main.geometry("1400x800")
        self.main.resizable(width=False, height=False)

        #Janela lateral aonde ficara os botoes
        #350x800 | fundo "cinza" | posicionado no lado esquerdo superior
        self.lateral = tk.Frame(self.main, width=300, height=800)
        self.lateral.config(bg = "#808080")
        self.lateral.grid(sticky="NW")
        self.lateral.grid_propagate(0)

        #Janela no qual estarao os dados dos produtos
        #1050x490 | fundo cinza claro
        self.tableFrame = tk.Frame(self.main, width=1050, height=490)
        self.tableFrame.config(bg="white")
        self.tableFrame.place(x=843,y=250, anchor="center")

        tabela = pgm.VisualizaTabela(self.tableFrame)


        # Frame para visualizar os outputs e mensagens do sistema
        # 985x220 | fundo cinza claro | desabilitado | e tipo flat
        self.outPutBox = tk.Text(self.main,
                                 background="#F0F0F0",
                                 relief="flat",
                                 font= minhaFont)
        self.outPutBox.place(x=810, y=685, anchor="center", width=985, height=200)

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
        entryProduto.place(x=320, y=525, anchor="nw", width=250, height=30)
        entrySetor.place(x=583, y=525, anchor="nw", width=200, height=30)
        entryValidade.place(x=795, y=525, anchor="nw", width=200, height=30)
        entryId.place(x=1008, y=525, anchor="nw", width=80, height=30)

       #Config dos botoes laterais

        largura = 18
        altura = 2

        #--- BotOes do menu Principal ---

        self.btnProcuraArquivo = tk.Button(self.lateral, 
                                           text="Abrir Arquivo", 
                                           width=largura, 
                                           height=altura,
                                           borderwidth=0,
                                           font=minhaFont,
                                           bg="white",
                                           fg="#262626",
                                           command = lambda: pgm.IniciaArquivo(self.main,
                                                                              tabela))
        self.btnProcuraArquivo.place(relx=0.5, rely=0.55, anchor="center")

        #Adicionar a Imagem para editar item
        imagemLapis = tk.PhotoImage(file="perdasGui/assets/Lapis.png")
 
        #botao para editar remessa
        self.editarBtn = tk.Button(self.main,
                                       image=imagemLapis,
                                       relief="flat",
                                       highlightthickness=0,
                                       command=lambda:[pgm.queryExecuter(operacao=1,
                                                                        entryProduto= entryProduto,
                                                                        entrySetor= entrySetor,
                                                                        entryValidade=entryValidade,
                                                                        identEntry=entryId),
                                                        pgm.resetaDados(entryProduto,
                                                                         entrySetor,
                                                                         idString,
                                                                         tabela)])
        self.editarBtn.image = imagemLapis
        self.editarBtn.place(x=1185, y=515, anchor="nw", width=50, height=50)

        #Adicionar a Imagem para Excluir o item
        imagemLixo = tk.PhotoImage(file="perdasGui/assets/lixeira.png")
        
        self.excluirBtn = tk.Button(self.main,
                                       image=imagemLixo,
                                       relief="flat",
                                       highlightthickness=0,
                                       command= lambda:[pgm.queryExecuter(operacao=2,
                                                                        entryProduto=entryProduto,
                                                                        entrySetor=entrySetor,
                                                                        entryValidade=entryValidade,
                                                                        identEntry= entryId),
                                                         pgm.resetaDados(entryProduto,
                                                                         entrySetor,
                                                                         idString,
                                                                         tabela)])
        self.excluirBtn.image = imagemLixo
        self.excluirBtn.place(x=1243, y=515, anchor="nw", width=50, height=50)

        # Adicionar Imagem de Inserimento de item
        imagemAdicao = tk.PhotoImage(file="perdasGui/assets/sum.png")
        
        self.InserirBtn = tk.Button(self.main,
                                       image=imagemAdicao,
                                       relief="flat",
                                       highlightthickness=0,
                                       command= lambda:[pgm.queryExecuter(0,entryProduto, entrySetor, entryValidade),
                                                        pgm.resetaDados(entryProduto,
                                                                        entrySetor,
                                                                        idString,
                                                                        tabela)])
        self.InserirBtn.image = imagemAdicao
        self.InserirBtn.place(x=1125, y=515, anchor="nw", width=50, height=50)

        # Adicionar a Imagem de logo no corpo lateral
        imagemLogo = Image.open("perdasGui/assets/logo.png")
        logo = ImageTk.PhotoImage(imagemLogo)

        self.labelLogo = tk.Label(self.lateral, image=logo, borderwidth=0)
        self.labelLogo.image = logo
        
        self.labelLogo.place(relx=0.49, rely=0.3, anchor="center")
        
        tabela.bind("<Double-1>", lambda event : pgm.selecionaItem(event,
                                                                   entryProduto=entryProduto,
                                                                   entrySetor=entrySetor,
                                                                   entryValidade=entryValidade,
                                                                   idVar=idString))
        
        pgm.IniciaArquivo(self.main,
                          tabela)


root = tk.Tk()

app = Janela(root)

root.mainloop()