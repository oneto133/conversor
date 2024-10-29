#arquivo main.py
from pdf2docx import Converter as pdf
from tkinter import *
import Funções
from Funções import Funcao, Graficos
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import dnd, ttk, Button
from threading import Thread


class MeuAplicativo():
    def __init__(self, janela):
        self.janela = janela
        self.janela.configure(bg='white')
        self.janela.resizable(True, True)
        self.janela.title("Minha janela")
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_programa)

        #centralizar a janela
        largura_da_janela = self.janela.winfo_screenwidth() #obtem a largura da janela
        altura_da_janela = self.janela.winfo_screenheight() # A Altura
        janela_width = 500 #Definindo a largura e altura da janela
        janela_height = 500
        x = (largura_da_janela - janela_width) // 2 
        y = (altura_da_janela - janela_height) // 2
        self.janela.geometry(f'{janela_width}x{janela_height}+{x}+{y}')
        self.janela.resizable(False, False)
        self.Tipo_de_Arquivo()



    def Tipo_de_Arquivo(self):
        self.botão_arquivo = Button(
                                    self.janela,text='selecionar arquivo', 
                                    command=self.abrir_gerenciador, width=15, height=1
                                    )
        self.botão_arquivo.place(x=200, y=300)
        self.frame = Frame(self.janela, bg='black', width=500, height=200, bd=2, relief='groove')
        self.frame.place(x=0, y=60)
        


    def abrir_gerenciador(self):
        self.funcao = Funcao()
        self.funcao.abrir_gerenciador_de_arquivos()
        self.arquivo = self.funcao.ler_arquivo_em_cache()
        if self.arquivo == None:
            pass

        else:
            self.caminho = Entry(self.janela, width=34)
            self.caminho.place(x=80, y=175)
            self.caminho.insert(0, 'Escolher destino')
            self.buscar = Button(self.janela, text='Buscar destino', bg='blue', fg='white', command=self.salvar_arquivo)
            self.buscar.place(x=350, y=170)
            imagem = Graficos()
            self.foto = imagem.Adicionar_imagens_nas_telas("pdf.png", 50, 60)
            self.rotulo = Label(self.janela, image=self.foto, bg='black')
            self.rotulo.place(x=120, y=100)


    def salvar_arquivo(self, event=None):
        self.arquivo_docx = filedialog.asksaveasfilename(title = 'Salvar arquivo como',
        defaultextension='.docx', filetypes=[("Document Files", "*.docx"), ("All Files", "*")])
        if self.arquivo_docx:
            self.caminho.delete(0, END)
            self.caminho.insert(0, self.arquivo_docx)
            self.buscar.config(text='Converter para Docx', command=self.nao_travar)

    def nao_travar(self):
        Thread(target=self.converter_arquivo).start()
        

    def converter_arquivo(self):
        if not self.arquivo:
            print("Por favor, selecione um arquivo PDF antes de converter.")
            return

        if not self.arquivo_docx:
            print("Por favor, escolha um destino para o arquivo Word.")
            return

        try:
            cv = pdf(self.arquivo)
            cv.convert(self.arquivo_docx, start=0, end=None)
            cv.close()
            self.mensagem = Label(self.janela, text="Conversão concluída com sucesso!", bg='black', fg='white').place(x=120, y=220)
        except Exception as e:
            self.mensagem['text'] = "Erro durante a conversão: {e}"

    def fechar_programa(self):
        self.janela.quit()
        self.janela.destroy()



if __name__=='__main__':
    janela = Tk()
    MeuAplicativo(janela)
    janela.mainloop()