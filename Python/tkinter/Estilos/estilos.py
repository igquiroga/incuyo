from tkinter import *
from tkinter import ttk
from tkinter import messagebox

colorVerde = "#8ed492"
colorVerde2 = "#3f8b49"
colorRojo = "#c33333"
colorRojo2= "#990808"
colorNegro = "gray22"
colorNegro2= "gray10"
letraNegra="black"
letraBlanca="white"
colorCeleste="#405C6D"
colorGris = "#4B4B4B"
fontEntry = ("Calibri",14)

#Modifique para un poquito mas alto
def centrar_ventana(anchoVentana,largoVentana):
	ancho = ventana.winfo_screenwidth()
	largo = ventana.winfo_screenheight()
	x = (ancho // 2) - (anchoVentana//2) 
	y = (largo //2) - (largoVentana//2) - 50
	ventana.geometry(f"{anchoVentana}x{largoVentana}+{x}+{y}")
def misEstilos(colorFondo,colorFondo2,colorBoton,colorLetra):
	estilos = ttk.Style()
	estilos.theme_use("alt")

	estilos.configure("titulos.TLabel",
				       background=colorFondo,
				       font = ("Calibri",20),
				       foreground= colorLetra,
				       relief=FLAT
					 )

	estilos.configure("botones.TFrame",
				       background=colorFondo
					 )
	estilos.configure("contenido.TFrame",
				       background=colorFondo
					 )


	estilos.configure("boton.TButton",
				       background=colorBoton,
				       foreground=colorLetra,
				       font=("Calibri",15),
				       relief=FLAT
					 )
	estilos.map("boton.TButton",
                       background = [("pressed",colorBoton),("active",colorBoton)]
					 )
	estilos.configure("botonPresionado.TButton",
				       background=colorCeleste,
				       foreground=colorLetra,
				       font=("Calibri",15),
				       relief=FLAT
					 )
	estilos.map("botonPresionado.TButton",
                       background = [("pressed",colorCeleste),("active",colorCeleste)]
					 )

def principal():
	ventana.config(bg=colorNegro)
	misEstilos(colorNegro,colorNegro2,colorNegro2,letraBlanca)
	#ventana.state("zoomed")
	centrar_ventana(1000,600)
	ventana.title("ESTILO")
	ventana.minsize(1000,600)

	frameContenido = ttk.Frame(style="contenido.TFrame")
	frameContenido.pack(fill=BOTH,expand=1)

	frameConfiguracion = ttk.Frame(frameContenido,style="contenido.TFrame")
	frameConfiguracion.pack(fill=BOTH,expand=1)

	#####Configuracion#####

	labelTituloConfiguracion = ttk.Label(frameConfiguracion,text="CONFIGURACIÓN",style="titulos.TLabel")
	labelTituloConfiguracion.pack()

	frameEstilos = ttk.Frame(frameConfiguracion,style="contenido.TFrame")
	frameEstilos.pack(fill=X,pady=10)

	def estiloRojo():
		ventana.config(bg=colorRojo)
		misEstilos(colorRojo,colorRojo2,colorRojo2,letraBlanca)
	botonEstiloRojo = ttk.Button(frameEstilos,text="Estilo Rojo",command=estiloRojo,style="boton.TButton")
	botonEstiloRojo.pack(side=LEFT,padx=10)
	def estiloVerde():
		ventana.config(bg=colorVerde2)
		misEstilos(colorVerde,colorVerde2,colorVerde2,letraBlanca)
	botonEstiloVerde = ttk.Button(frameEstilos,text="Estilo Verde",command=estiloVerde,style="boton.TButton")
	botonEstiloVerde.pack(side=LEFT,padx=10)
	def estiloNegro():
		ventana.config(bg=colorNegro2)
		misEstilos(colorNegro,colorNegro2,colorNegro2,letraBlanca)
	botonEstiloNegro = ttk.Button(frameEstilos,text="Estilo Negro",command=estiloNegro,style="boton.TButton")
	botonEstiloNegro.pack(side=LEFT,padx=10)
	#####Configuracion#####


def run():
	global ventana
	ventana = Tk()
	principal()
	ventana.mainloop()

run()

