#Arquivo telalogin.py
from tkinter import *
from PIL import ImageTk, Image
import connection_with_db as conn
import main


class app():
    def __init__(self):
        self.janela = Tk()
        self.tela_de_validação = Tela_De_Login(self.janela)
        self.janela.mainloop()


class Tela_De_Login:
    def __init__(self, janela):
        
        #Configuraçãoes da janela
        self.janela = janela
        self.janela.title("Conversor de pdf")
        self.janela.iconbitmap('Icone.ico')
        
        # Obter a largura e altura da janela
        largura_da_janela = self.janela.winfo_screenwidth()
        altura_da_janela = self.janela.winfo_screenheight()
        
        # Calcular as coordenadas para centralizar a janela
        janela_width = 250
        janela_height = 200
        x = (largura_da_janela - janela_width) // 2
        y = (altura_da_janela - janela_height) // 2
        
        # Configuração da janela
        self.janela.geometry(f'{janela_width}x{janela_height}+{x}+{y}')
        self.janela.resizable(False, False)
        
        self.Elementos_Da_Tela()


    def Mostrar_Senha(self):
        if self.verificar_senha.get():
            self.Password_Entry.config(show='')
        else:
            self.Password_Entry.config(show='*')


    def mover_foco(self, event):
        self.Password_Entry.focus_set()
        self.Mensagem_de_alerta['text'] = 'Digite uma senha.'
        

    def Pegar_dados(self, event):
        self.clicar_botao()
        self.janela.update()

    def abre_a_tela_principal(self):
        self.tela_principal = Toplevel(self.janela)
        self.tela_principal.protocol("WM_DELETE_WINDOW", self.fechar_programa)
        main.MeuAplicativo(self.tela_principal)
    

    def fechar_programa(self):
        self.janela.quit()
        self.janela.destroy()

        
    def clicar_botao(self):
        dado = self.Users_Entry.get()
        consulta = conn.Query()
        self.janela.update()
        self.senha = consulta.consultar_senha_por_usuario(dado)
        self.janela.update()
        if self.senha == self.Password_Entry.get():
            self.Mensagem_de_alerta['text'] = "tudo certo"

            self.janela.withdraw()
            self.abre_a_tela_principal()

        else:
            self.Mensagem_de_alerta['text'] = 'senha incorreta!' 
        print('Botão clicado...')
    

    def Elementos_Da_Tela(self):
        #Labels
        self.Login = Label(text='Login', font=('Sixtyfour Convergence', 16, 'bold')).place(x=60, y=5)
        self.Users = Label(text='Usuário:', font=('Arial', 11, 'bold')).place(x=30, y=50)
        self.Password = Label(text='Senha:', font=('Arial', 11, 'bold')).place(x=30, y=100)
        self.imagem = Image.open('Icone.ico')
        self.imagem = self.imagem.resize((60, 30))
        self.foto= ImageTk.PhotoImage(self.imagem)
        self.rotulo = Label(self.janela, image=self.foto)
        #Mostrar senha
        self.verificar_senha = BooleanVar()
        self.Checkbutton = Checkbutton(text='Mostrar senha', variable=self.verificar_senha, command=self.Mostrar_Senha)
        self.Mensagem_de_alerta = Label(self.janela, text='', font=("Arial", 8, "bold"), fg='red')

        #Entradas de dados    
        self.Users_Entry = Entry(self.janela)
        self.janela.update()
        self.Password_Entry = Entry(self.janela, show='*')

        #Posicionamento
        self.Users_Entry.place(x=100, y=53)
        self.Password_Entry.place(x=100, y=103)
        self.Mensagem_de_alerta.place(x= 95, y= 143)
        self.rotulo.place(x=140, y= 5)
        self.Checkbutton.place(x=95, y = 125)

        #Botões
        self.Botão_Login = Button(text='Entrar', fg='white', bg='blue', relief='raised', width=9, height=1, command=self.clicar_botao).place(x=95, y=160)

        #Bind
        self.Users_Entry.bind("<Return>", self.mover_foco)
        self.Password_Entry.bind("<Return>", self.Pegar_dados)


 


if __name__ == '__main__':
    app()
