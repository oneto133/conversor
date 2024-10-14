
import sys
sys.path.append(r'C:\Users\PortifolioUnopar')

from tkinter import *
from pdf2docx import Converter
import Funções

class MeuAplicativo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Conversor de PDF")
        self.janela.geometry('500x500')
        self.janela.configure(bg='white')
        self.janela.resizable(True, True)

        self.criar_elementos()

    def criar_elementos(self):
        Label(
            self.janela,
            text="Qual o tipo de arquivo que você quer converter?",
            bg='white', fg='black', font='bold'
        ).pack(pady=10)

        self.tipo_de_arquivo_entry = Entry(self.janela)
        self.tipo_de_arquivo_entry.pack(pady=5)

        Button(
            self.janela, text='Ok', command=self.obter_valor, width=6, height=1
        ).pack(pady=5)

        self.mensagem_label = Label(self.janela, text='', bg='white', fg='black')
        self.mensagem_label.pack(pady=10)

    def obter_valor(self):
        valor = self.tipo_de_arquivo_entry.get()
        encontrado = False

        with open('arquivos.txt', 'r') as arquivo:
            for linha in arquivo:
                if linha.strip() == valor:
                    self.mensagem_label['text'] = f"Ok! {linha}"
                    self.converter_pdf()
                    encontrado = True
                    break

        if not encontrado:
            self.mensagem_label['text'] = f"Formato '{valor}' não encontrado. Tente novamente."

    def converter_pdf(self):
        arquivo_pdf = input("Nome do arquivo PDF: ")
        if not arquivo_pdf.endswith('.pdf'):
            arquivo_pdf += '.pdf'

        arquivo_word = input("Nome do arquivo Word: ")
        if not arquivo_word.endswith('.docx'):
            arquivo_word += '.docx'

        cv = Converter(arquivo_pdf)
        cv.convert(arquivo_word)
        cv.close()

if __name__ == '__main__':
    root = Tk()  # Mantemos Tk() apenas no script principal
    MeuAplicativo(root)
    root.mainloop()
