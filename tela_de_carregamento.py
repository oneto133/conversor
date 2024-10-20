from tkinter import *
from tkinter.ttk import Progressbar
from time import sleep
from threading import Thread
import Tela_login




class TelaDeCarregamento:
    def __init__(self, janela, titulo='Conversor'):
        self.janela = janela
        self.janela.title(titulo)
        self.barra_de_progresso = Progressbar(self.janela, orient=HORIZONTAL, length=250, mode='determinate')
        self.barra_de_progresso.place(x=20, y=120)
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_programa)
    

        #centralizar a tela no meio

        largura_da_janela = self.janela.winfo_screenwidth()
        altura_da_janela = self.janela.winfo_screenheight()

        largura = 300
        altura = 200

        x = (largura_da_janela - largura) // 2
        y = (altura_da_janela - altura) //2

        self.janela.geometry(f'{largura}x{altura}+{x}+{y}')
        self.janela.resizable(False, False)


        self.continuar = True
        self.nao_travar(self.Carregamento)



    def Carregamento(self):
        valor = 12
        for c in range(1,9):
            self.barra_de_progresso['value'] = valor
            self.janela.update_idletasks()
            sleep(0.2)
            valor += 13
        self.janela.after(0, self.abrir_tela_de_login)

    

    def nao_travar(self, alvo):
        self.continuar = True
        #Aqui ta executando o programa em uma thread separada
        if self.continuar:
            Thread(target=alvo).start()
            

    def abrir_tela_de_login(self):
        self.janela.withdraw()
        tela_de_login = Toplevel(self.janela)
        tela_de_login.protocol("WM_DELETE_WINDOW", self.fechar_programa)
        Tela_login.Tela_De_Login(tela_de_login)
    
    def fechar_programa(self):
        self.continuar=False
        self.janela.quit()
        self.janela.destroy()




if __name__ == "__main__":
    janela = Tk()
    TelaDeCarregamento(janela, 'Conversor de Pdf')
    janela.mainloop()

