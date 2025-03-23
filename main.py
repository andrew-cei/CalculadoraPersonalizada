import tkinter as tk
# Ventana principal
root = tk.Tk()
# Configuración de la ventana principal
root.title('Calculadora Física')
root.geometry('800x600')
root.minsize(400,300)
root.maxsize(1600, 1200)
root.resizable(True, False)
root.iconbitmap('./assets/albert_einstein_avatar_icon_263209.ico')

# Widgets
titulo = tk.Label(root, text="Calculadora física")
titulo.grid(row = 0, column=1)
btn1 = tk.Button(root, text='Celsius a Farenheit')
btn1.grid(row=1,column=0)

# Bucle principal
root.mainloop()