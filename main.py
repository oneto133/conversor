
#arquivo main.py

from pdf2docx import Converter as pdf
from tkinter import *
import sys
sys.path.append(r'C:\Users\PortifolioUnopar')
import Funções
from random import choice

class MeuAplicativo():
    def __init__(self, janela):
        self.janela = janela
        self.janela.configure(bg='white')
        self.janela.geometry('500x500')
        self.janela.resizable(True, True)
        self.janela.title("Minha janela")
        self.Tipo_de_Arquivo()



    def Tipo_de_Arquivo(self):
        print('teste')
        qual_o_tipo = Label(self.janela,text = "Qual o tipo de arquivo que você quer converter? ", bg= 'white', fg = 'black', font='bold')
        qual_o_tipo.pack()
        print('teste')
        self.tipo_de_arquivo = Entry(self.janela)
        self.tipo_de_arquivo.pack()
        self.botão_arquivo = Button(self.janela,text='Ok', command=self.obter_valor, width=6, height=1)
        self.botão_arquivo.pack()
        self.mensagem_ok = Label(self.janela, text='', bg='white', fg='black')
        self.mensagem_ok.pack
        
    def obter_valor(self):
        valor = self.tipo_de_arquivo.get()
        encontrado = False
        with open('arquivos.txt', 'r') as arquivo:
            for linha in arquivo:
                if linha.strip() == valor:
                    self.mensagem_ok['text'] = f"Ok! {linha}"
                    print('ok')
                    self.Código()
                    encontrado = True
                    break
        if not encontrado:
            self.mensagem_ok['text'] = f"Arquivo no formato '{valor}' não encontrado, insira novamente..."
        

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
