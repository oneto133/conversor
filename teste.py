'''from tkinter import filedialog, messagebox
import os


mensagem = messagebox.askyesno(title='Adcionar linha?', message='Gostaria de selecionar um par de origem e destino?')

with open('diretorios.csv', 'w') as dircsv:
    dircsv.write('origem,destino\n')

    while mensagem:
        origem = filedialog.askdirectory()
        destino = filedialog.askdirectory()
        dircsv.write(f'{origem}, {destino}\n')
        mensagem = messagebox.askyesno(title='Adcionar linha?', message='Gostaria de selecionar um par de origem e destino?')

'''
'''
root = tk.Tk()
canvas = tk.Canvas(root, width=50, height=50)
canvas.pack()

x0 = 15
y0 = 15
r = 2
angle = 0

def animate():
    global angle
    canvas.delete("all")  # Limpa o canvas a cada iteração
    x = x0 + r * math.cos(angle)
    y = y0 + r * math.sin(angle)
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")
    angle += 0.1
    root.after(10, animate)  # Chama a função novamente após 10ms

animate()

root.mainloop()'''
'''
Integrando a Barra de Progresso tqdm em uma Interface Tkinter
Entendendo o Problema:

Você deseja exibir uma barra de progresso criada com a biblioteca tqdm em uma interface gráfica construída com Tkinter. A tqdm é excelente para exibir o progresso no terminal, mas para integrá-la a uma interface gráfica, precisamos de um pouco mais de trabalho.

Solução:

A ideia principal é executar a tarefa que gera a barra de progresso em uma thread separada, enquanto a interface Tkinter continua respondendo. Isso permite atualizar a barra de progresso sem travar a interface.

Código Completo:
'''
'''
import tkinter as tk
from tqdm import tqdm
import threading
import time

def progress_bar():
    for i in tqdm(range(100), desc="Processando...", unit="it"):
        # Simulação de uma tarefa demorada
        time.sleep(0.1)
        # Atualiza a interface Tkinter (opcional)
        tk.Label(text={i}).pack()
        root.update_idletasks()

def start_progress():
    thread = threading.Thread(target=progress_bar)
    thread.start()

root = tk.Tk()
root.title("Barra de Progresso com Tkinter")

# Botão para iniciar a barra de progresso
button = tk.Button(root, text="Iniciar", command=start_progress)
button.pack()

root.mainloop()'''
