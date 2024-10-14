'''from tkinter import filedialog, messagebox
import os


mensagem = messagebox.askyesno(title='Adcionar linha?', message='Gostaria de selecionar um par de origem e destino?')

with open(os.path.join('input', 'diretorios.csv'), 'w') as dircsv:
    dircsv.write('origem,destino\n')

    while mensagem:
        origem = filedialog.askdirectory()
        destino = filedialog.askdirectory()
        dircsv.write(f'{origem}, {destino}\n')
        mensagem = messagebox.askyesno(title='Adcionar linha?', message='Gostaria de selecionar um par de origem e destino?')

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

root.mainloop()