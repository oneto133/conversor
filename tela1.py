from tkinter import *
from PIL import ImageTk, Image
import connection_with_db as conn
import main2

class App:
    def __init__(self):
        self.janela = Tk()
        self.tela_login = TelaDeLogin(self.janela)
        self.janela.mainloop()

class TelaDeLogin:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Conversor de PDF")
        self.janela.iconbitmap('Icone.ico')

        # Centralizar a janela
        largura = self.janela.winfo_screenwidth()
        altura = self.janela.winfo_screenheight()
        janela_width, janela_height = 250, 200
        x = (largura - janela_width) // 2
        y = (altura - janela_height) // 2
        self.janela.geometry(f'{janela_width}x{janela_height}+{x}+{y}')
        self.janela.resizable(False, False)

        self.criar_elementos()

    def criar_elementos(self):
        Label(self.janela, text='Login', font=('Sixtyfour Convergence', 16, 'bold')).place(x=60, y=5)
        Label(self.janela, text='Usuário:', font=('Arial', 11)).place(x=30, y=50)
        Label(self.janela, text='Senha:', font=('Arial', 11)).place(x=30, y=100)

        # Imagem no topo
        imagem = Image.open('Icone.ico').resize((60, 30))
        self.foto = ImageTk.PhotoImage(imagem)
        Label(self.janela, image=self.foto).place(x=140, y=5)

        # Entrada de usuário e senha
        self.usuario_entry = Entry(self.janela)
        self.usuario_entry.place(x=100, y=53)

        self.senha_entry = Entry(self.janela, show='*')
        self.senha_entry.place(x=100, y=103)

        # Checkbox para mostrar senha
        self.mostrar_senha_var = BooleanVar()
        Checkbutton(self.janela, text='Mostrar senha', variable=self.mostrar_senha_var, command=self.mostrar_senha).place(x=95, y=125)

        # Mensagem de alerta
        self.alerta_label = Label(self.janela, text='', font=("Arial", 8, "bold"), fg='red')
        self.alerta_label.place(x=95, y=143)

        # Botão de login
        Button(self.janela, text='Entrar', fg='white', bg='blue', width=9, command=self.clicar_botao).place(x=95, y=160)

        # Bind para pressionar Enter
        self.usuario_entry.bind("<Return>", lambda event: self.senha_entry.focus_set())
        self.senha_entry.bind("<Return>", lambda event: self.clicar_botao())

    def mostrar_senha(self):
        if self.mostrar_senha_var.get():
            self.senha_entry.config(show='')
        else:
            self.senha_entry.config(show='*')

    def clicar_botao(self):
        usuario = self.usuario_entry.get()
        consulta = conn.Query()
        senha_armazenada = consulta.consultar_senha_por_usuario(usuario)

        if senha_armazenada == self.senha_entry.get():
            self.alerta_label['text'] = "Login bem-sucedido!"
            self.janela.withdraw()  # Esconde a janela de login
            self.abrir_tela_principal()
        else:
            self.alerta_label['text'] = 'Senha incorreta!'

    def abrir_tela_principal(self):
        nova_janela = Toplevel(self.janela)  # Nova janela como Toplevel
        main2.MeuAplicativo(nova_janela)

if __name__ == '__main__':
    App()
