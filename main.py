import tkinter as tk
from Parabola import Parabola
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# Objeto tipo parábola
movement = Parabola(vo=50,alpha=45)

# Cálculo de resultados
def resultados(objeto, angulo, g, vo):
    # Actualización de valores
    objeto.set_g(g)
    objeto.set_vo(vo)
    objeto.set_alpha(angulo)
    objeto.tiempo_vuelo()
    objeto.alcance()
    objeto.altura_maxima()

# Creación de la gráfica
def plot(objeto, angulo, g, vo):
    resultados(objeto, angulo, g, vo)
    x, y =objeto.trayectoria()
    # Figura que contendrá el plot
    fig = Figure(figsize = (5, 5), dpi = 100) 
   
    # Se añade un subplot
    plot1 = fig.add_subplot(111) 
  
    # Se dibuja la gráfica
    plot1.plot(x, y)
  
    # Tkinter canvas 
    # Figura Matplotlib
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw() 
  
    # Canvas dentro de Tkinter window 
    canvas.get_tk_widget().grid(row=4,column=1) 
  
    # Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, root) 
    toolbar.update() 
  
    # Toolbar dentro de Tkinter window 
    canvas.get_tk_widget().grid(row=5,column=1) 

# Ventana principal
root = tk.Tk()
# Configuración de la ventana principal
root.title('Calculadora Física')
root.geometry('800x600')
root.minsize(400,300)
root.maxsize(1600, 1200)
root.resizable(False, True)
root.iconbitmap('./assets/albert_einstein_avatar_icon_263209.ico')

# Variables para widgets
angulo = tk.DoubleVar(value=0)
gravedad = tk.DoubleVar(value=9.81)
rapidez = tk.DoubleVar(value=0)

# Textos Renglón 1
titulo = tk.Label(root, text="Calculadora física")
titulo.grid(row = 0, column=1)
texto1 = tk.Label(root, text="Gravedad [m/s^2]")
texto1.grid(row = 1, column=0)
texto2 = tk.Label(root, text="Rapidez inicial [m/s]")
texto2.grid(row = 1, column=1)
texto3 = tk.Label(root, text="Ángulo de disparo [grados]")
texto3.grid(row = 1, column=2)
# Entradas de texto Renglón 2
gravedad_w = tk.Entry(root, textvariable=gravedad)
gravedad_w.grid(row=2,column=0)
rapidez_w = tk.Entry(root, textvariable=rapidez)
rapidez_w.grid(row=2,column=1)
angulo_w = tk.Entry(root, textvariable=angulo)
angulo_w.grid(row=2, column=2)
# Botón de cálculo Renglón 3
btn1 = tk.Button(root, text='Cálculo', command= lambda: plot(movement, float(angulo.get()), float(gravedad.get()), float(rapidez.get())))
btn1.grid(row=3,column=1)
# Variables de resultado
alcance = tk.DoubleVar()
altura = tk.DoubleVar()
tiempo = tk.DoubleVar()
# Títulos de resultado
#resultado1 = tk.Label(root, text="Alcance [m]")
#resultado1.grid(row = 6, column=0)
#resultado2 = tk.Label(root, text="Altura máxima [m]")
#resultado2.grid(row = 6, column=1)
#resultado3 = tk.Label(root, text="Tiempo de vuelo [s]")
#resultado3.grid(row = 6, column=2)
# Resultados
#alcance_r = tk.Label(root, text=movement.alcance())
#altura_r = tk.Label(root, text=movement.altura_maxima()) 
#tiempo_r = tk.Label(root, text=movement.tiempo_vuelo()) 
#alcance_r.grid(row=7,column=0)
#altura_r.grid(row=7,column=1)
#tiempo_r.grid(row=7,column=2)

# Bucle principal
root.mainloop()