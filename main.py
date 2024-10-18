#arquivo main.py
from pdf2docx import Converter as pdf
from tkinter import *
import Funções
from Funções import Funcao, Graficos
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import dnd, ttk


class MeuAplicativo():
    def __init__(self, janela):
        self.janela = janela
        self.janela.configure(bg='white')
        self.janela.geometry('500x500')
        self.janela.resizable(True, True)
        self.janela.title("Minha janela")
        self.Tipo_de_Arquivo()



    def Tipo_de_Arquivo(self):
        self.botão_arquivo = Button(
                                    self.janela,text='selecionar arquivo', 
                                    command=self.abrir_gerenciador, width=15, height=1
                                    )
        self.botão_arquivo.place(x=200, y=50)
        self.frame = Frame(self.janela, bg='black', width=500, height=200, bd=2, relief='groove')
        self.frame.place(x=0, y=150)
        


    def abrir_gerenciador(self):
        funcao = Funcao()
        funcao.abrir_gerenciador_de_arquivos()
        arquivo = funcao.ler_arquivo_em_cache()
        if arquivo == "vazio":
            pass
        else:
            self.mensagem_ok = Label(
                                    self.janela, text=f'Selecione o arquivo de destino ->',
                                    bg='black', fg='white', font=('Arial', 10, 'bold')
                                    )
            self.mensagem_ok.place(x=140, y=170)
            imagem = Graficos()
            self.foto = imagem.Adicionar_imagens_nas_telas(r"C:\conversorpdf\conversor\pdf.png", 50, 60)
            self.rotulo = Label(self.janela, image=self.foto, bg='black')
            self.rotulo.place(x=70, y=160)

            opções = [
                'PDF',
                'DOCX'
            ]
            self.combobox = ttk.Combobox(

                self.janela, values=opções, 
                background='black', foreground='black'
            
            )
            self.combobox.set('Selecionar')
            self.combobox.place(x=350, y=170)
            

            

    def Código(self):
        self.arquivo = input("Qual o nome do arquivo em pdf? ")
        try:
            resultado = Funções.Verificar_se_existe_o_arquivo(self.arquivo)
        except KeyboardInterrupt:
            print("Execução interrompida...")

        if arquivo_em_pdf[-4:] == '.pdf':
            arquivo_em_pdf = arquivo_em_pdf

        else:
            arquivo_em_pdf = f"{arquivo_em_pdf}.pdf"

        arquivo_word = input("Nome do novo arquivo word? ")
        if arquivo_word[-4:] == 'docx':
            arquivo_word = arquivo_word

        else:
            arquivo_word = f"{arquivo_word}.docx"

        cv = pdf(arquivo_em_pdf)
        cv.convert(arquivo_word)
        cv.close()


if __name__=='__main__':
    janela = Tk()
    MeuAplicativo(janela)
    janela.mainloop()
