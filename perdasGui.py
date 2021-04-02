import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

# Import das funcoes e classe
from perdasGuiMetodos import insereWin, buscaWin, VisualizaTabela


class Janela:

    def __init__(self, main):

        # Configuracao de font
        minhaFont = tkFont.Font(family="Helvetica", size=14)

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
        #900x500 | fundo cinza claro
        self.tableFrame = tk.Frame(self.main, width=1050, height=490)
        self.tableFrame.config(bg="white")
        self.tableFrame.place(x=910,y=270, anchor="center")

        VisualizaTabela(self.tableFrame)

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
        command=lambda: insereWin(self.main))

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
                                    command= lambda : buscaWin(self.main))

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


root = tk.Tk()

app = Janela(root)

root.mainloop()